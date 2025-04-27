import { AccountService } from "./account_service.js";

class CommonService {
    
    static load = () => {
        addEventListener('beforeunload', () => {
            alert('!!!');
            alert(document.cookie);
        
        })

        const icon = document.getElementById('log-out');
        if (!icon) return;
        icon.addEventListener('click', () => {
            if (!confirm('로그아웃 하시겠습니까?')) return;
            AccountService.do_sign_out()
            .then(resp => {
                alert('정상적으로 로그아웃되었습니다');
                window.open('/view/main', '_self');
            })
            .error(err => {
                console.log(err);
                alert('시스템 오류가 발생하였습니다.')
            })
        })
        
    }

    static do_sign_out = () => {
        
    }
}

export { CommonService }


