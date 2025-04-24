import { AccountService } from './account_service.js'

class Service {
    static load() {
        const toggle_register = document.querySelector('#toggle-register > input');
        toggle_register.addEventListener('click', (e) => {
            if (e.target.checked) {
                document.querySelectorAll('#form-groups > .input-group input').forEach(e => {
                    console.log(e);
                    e.value='';
                });
                // [1] : password input group node
                var confirm_password=document.querySelectorAll('.input-group')[1].cloneNode(true);
                var input = confirm_password.querySelector('input');
                input.id='form_check_pw';
                input.placeholder='Check password';
                document.getElementById('form-groups').appendChild(confirm_password);
            } else {
                var input_groups=document.querySelectorAll('#form-groups > .input-group');
                input_groups[input_groups.length - 1].remove();
            }
        });

        addEventListener("keypress", (e) => {
            // skip process otherwise keycode "Enter"
            if (e.keyCode !== 13) return;
            if (toggle_register.checked) this.do_sign_up();
            else this.do_sign_in();
        });
    }

    static do_sign_up = () => {
        var id = document.getElementById('form_id').value;
        var password = document.getElementById('form_pw').value;
        var check_password = document.getElementById('form_check_pw').value;
        // TODO validate password
        var validated=true;
        if (validated) {
            AccountService.sign_up(id, password)
            .then((resp) => {
                if (resp.data.status==200) {
                    alert('정상 등록되었습니다.');
                    window.open('/view/main', '_self');
                    return;
                }
                if (resp.data.status==400) {
                    alert('이미 존재하는 아이디입니다');
                    return;
                }
                alert('시스템 오류가 발생했습니다');
            })
            .catch((e) => {
                console.log(e);
                alert('시스템 오류가 발생했습니다');
            });
        }
    }
    
    static do_sign_in = () => {
        var id = document.getElementById('form_id').value;
        var password = document.getElementById('form_pw').value;
        AccountService.sign_in(id, pw)
        .then(function(resp){
            if(resp.data.status===200) window.open('/view/main', '_self');
            if(resp.data.status===404) alert('아이디 혹은 비밀번호가 일치하지 않습니다');
            if(resp.data.status===500) alert('시스템 오류가 발생하였습니다');
        })
        .catch(function(err){
            alert('시스템 오류가 발생하였습니다');
        });
    }
}



export { Service }