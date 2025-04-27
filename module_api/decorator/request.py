from datetime import datetime
from module_api.enum import UESR_KEY, ANONYMOUS_USER, PUBLIC_AUTH_LEVEL
from typing import Final

def audit(function_dml):
    def decorator(*args):
        entity = args[0]
        request = args[1]
        user = request.session.__getitem__(UESR_KEY)
        created_by = update_by = ANONYMOUS_USER if user['auth_level'] == PUBLIC_AUTH_LEVEL else user['id'] 
        create_date = update_date = datetime.now()
        if not entity.initial_data.__contains__('create_by'):
            entity.initial_data.__setitem__('create_by', created_by)
        if not entity.initial_data.__contains__('create_date'):
            entity.initial_data.__setitem__('create_date', create_date)
        entity.initial_data.__setitem__('update_by', update_by)
        entity.initial_data.__setitem__('update_date', update_date)
        return function_dml(*args)
    return decorator