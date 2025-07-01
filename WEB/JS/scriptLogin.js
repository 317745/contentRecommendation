//Login
const sendLogin = async (event) => {
    const url = 'http://localhost:3031/login';

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const responseLogin = document.getElementById('responseLogin');
    const buttonLogin = document.getElementById('buttonLogin');
    const formLogin = document.getElementById('formLogin');
    const pLogin = document.getElementById('responseLogin')

    if (!formLogin.checkValidity()) {
        return;
    } else {
        event.preventDefault();
    }
    
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email:`${email}`,
            password:`${password}`
        })
    });

    response = await response.json();
    pLogin.textContent = `${response.data}`;
    setTimeout(function() {
        pLogin.textContent = '';
    }, 5000);
};

//Create User

const createUSer = () => {
    
}