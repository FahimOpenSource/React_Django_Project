document.addEventListener('DOMContentLoaded', () => {
    const url = window.location.href
    if (url.includes("sign-in")) {
        SignIn()
    }

    if (url.includes("sign-up")) {
        SignUp()
    }
    

    
});

function SignUp(e) {
    document.querySelector('h1').textContent = "Sign Up"
    document.getElementById('signup').style.display = 'flex'
    document.getElementById('submit_btn').textContent = 'Sign Up'
    const btn = document.getElementById("btn")
    btn.textContent = 'Sign in instead'
    btn.onclick = () => Route('sign-in')
    if (e) {
        if (e.type === 'click') {
            console.log(e.type)
            history.back()
            btn.onclick = () => Route('sign-in')
        }
    }else {
        btn.onclick = () => Route('sign-in')
    }

    document.querySelector('form').onsubmit = () => {
        const first_name = document.getElementById('first_name').value
        const last_name = document.getElementById('last_name').value
        const username = document.getElementById('username').value
        const password = document.getElementById('password').value

        const data = {
            username : username,
            password : password,
            first_name : first_name,
            last_name : last_name,
        }

        fetch('/accounts/api/signup', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        
        .then(response => response.json())
        .then(data => console.log(data));
        
        return false
    }
    

}


function SignIn (e) {
    document.querySelector('h1').textContent = "Sign In"
    document.getElementById('submit_btn').textContent = 'Sign in'
    document.getElementById('signup').style.display = 'none'
    const btn = document.getElementById("btn")
    btn.textContent = 'Sign Up instead'
    if (e) {
        if (e.type === 'click') {
            console.log(e.type)
            history.back()
            btn.onclick = () => Route('sign-up')
        }
    }else {
        btn.onclick = () => Route('sign-up')
    }

    document.querySelector('form').onsubmit = () => {
        const username = document.getElementById('username').value
        const password = document.getElementById('password').value

        const data = {
            username : username,
            password : password,
        }

        fetch('/accounts/api/signin', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        
        .then(response => response.json())
        .then(data => console.log(data));
        
        return false
    }




}

function Route (url_name) {
    if (url_name) {
        history.pushState({}, "", url_name);
        const url = window.location.href
        if (url.includes("sign-in")) {
            SignIn()
        }
    
        if (url.includes("sign-up")) {
            SignUp()
        }
        
    }

}


