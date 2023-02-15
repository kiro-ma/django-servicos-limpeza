function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

async function fetchFactory(method, url, body) {
    let dataReturned
    let init = {
        method: method,
        headers: {},
    }
    if (method == 'GET') {
        init.headers = {
            'X-CSRFToken': getCookie("csrftoken")
        }
    } else {
        init.headers = {
            'X-CSRFToken': getCookie("csrftoken"),
            'Content-Type': 'application/json'
        }
        init = Object.assign(init, { body: JSON.stringify(body) })
    }
    await fetch(url, init)
        .then(response => response.json())
        .then(dataResponse => dataReturned = dataResponse)
    return dataReturned
}

async function userValidation(data) {
    return await fetchFactory('POST', `/auth/validar/usuario/`, data)
}

async function login() {
    data = {
        'username': document.getElementById('usuario').value,
        'senha': document.getElementById('senha').value
    }
    let validation = await userValidation(data)

    if (validation.status == 'ERROR') {
        alertLoginErro()
    } else { document.getElementById('form').submit() }
}

function alertLoginErro() {
    document.getElementById('usuario').style = 'border: 3px solid rgb(238, 79, 79)'
    document.getElementById('senha').style = 'border: 3px solid rgb(238, 79, 79)'

    document.getElementById('alert-senha').style = ''
}

function limparSenhaAlert() {
    document.getElementById('usuario').style = ''
    document.getElementById('senha').style = ''

    document.getElementById('alert-senha').style = 'display: none;'
}