class AccountService {

    static sign_up = (id, pw) => {
        // Sign up
        // TODO psudo code
        const data = new FormData();
        data.append('id', id);
        data.append('password', pw);
        return axios.post('/api/sign-up/', data)
    }
    
    static sign_in = (id, pw) => {
        const data = new FormData();
        data.append('id', id);
        data.append('password', pw);
        return axios.post('/api/sign-in/', data)
    }
}

export { AccountService }