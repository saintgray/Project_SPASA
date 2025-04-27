class AccountService {

    static sign_up = (id, pw) => {
        const data = new FormData();
        data.append('user', JSON.stringify({ "id": id, "password":pw }));
        return axios.post('/api/sign-up/', data);
    }
    
    static sign_in = (id, pw) => {
        console.log(id);
        console.log(pw);
        const data = new FormData();
        data.append('user', JSON.stringify({ "id": id, "password":pw }));
        return axios.post('/api/sign-in/', data);
    }

    static sign_out = () => {
        return axios.post('/api/sign-out');
    }
}

export { AccountService }