from django.http import HttpRequest
from datetime import datetime
from datetime import timezone
import json
from module_api.auth.authorize_service import get_view_permissions
from module_api.enum import ACCESSIBLE_VIEW_KEY, UESR_KEY, PUBLIC_AUTH_LEVEL
from module_entity.model_session import SessionModel


def pre_handle_request(get_response):
    def authorized_user(request: HttpRequest):
        session = request.session
        anonymous = not session.__contains__(UESR_KEY) or (session.__getitem__(UESR_KEY)['auth_level'] == PUBLIC_AUTH_LEVEL)
        # flush session when sign-in user session is expired
        if not session.is_empty() and not anonymous:
            try:
                created_session=SessionModel.objects.get(session_key__exact=request.session.session_key)
                expire_date = created_session.expire_date # UTC
                now = datetime.now(timezone.utc) # convert local Time in UTC+0
                """
                this system considered as local server environmnet in Asia/Sedoul (=UTC+9)
                so, need to subtract offset diff when calculate session expired
                """
                offset_seconds = (60 * 60 * 9) # UTC +9 hours in seconds
                session_expired = expire_date.timestamp() - (now.timestamp() + offset_seconds) < 0
                if session_expired:
                    print('Session expired')
                    raise SessionModel.DoesNotExist
            except SessionModel.DoesNotExist:
                print('flush session')
                session.flush()
        # when session flushed add session anonymous user
        # this apply session attribute "modified" = True and reassigned new cookies
        if session.is_empty():
            print('assign anonymous user')
            session.__setitem__(UESR_KEY, {'auth_level': PUBLIC_AUTH_LEVEL}) # example
            session.__setitem__(ACCESSIBLE_VIEW_KEY, json.loads(json.dumps(get_view_permissions(request))))
        else:
            session.modified = True
        return get_response(request)
    return authorized_user
    
        
        