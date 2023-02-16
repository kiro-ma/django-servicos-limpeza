
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