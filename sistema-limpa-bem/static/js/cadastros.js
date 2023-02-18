

function limpar() {
    document.getElementById("form").reset();
    document.getElementById("form").querySelectorAll("[required]").forEach(function (i) {
        i.style = ''
    })
    document.getElementById('btn-editar').style = "color: rgb(45, 45, 45); display: none;"
}

function hasWhiteSpace(s) {
    return s.indexOf(' ') >= 0;
}

async function check_username() {
    let username_field = document.getElementById('username')
    if (username_field.value) {
        try {
            if(hasWhiteSpace(username_field.value)){
                throw new Error('Há espaço no nome de usuário!');
            }
            alert_editar_usuario(await getUsuario(username_field.value))
            username_field.style = 'border: 3px solid orange'
        } catch (error) {
            if (username_field.value.length >= 4 && !hasWhiteSpace(username_field.value)) {
                username_field.style = 'border: 3px solid lightgreen'
                document.getElementById('btn_cadastrar').disabled = false
            } else {
                username_field.style = 'border: 3px solid rgb(238, 79, 79)'
                document.getElementById('btn_cadastrar').disabled = true
                //data-tooltip="Nome de usuário muito curto" data-tooltip-location="bottom"
            }
        }
    } else { username_field.style = ''; document.getElementById('btn_cadastrar').disabled = false }
}

function limpar_alerts_senhas() {
    document.getElementById('senhas_diferentes').style = "display: none"
    document.getElementById('caracteres_invalidos_senha').style = "display: none"
    document.getElementById('senha_curta').style = "display: none"
}

function ativar_desativar_alerts_senhas(status, id) {
    if (status) {
        document.getElementById(id).style = "color: rgb(238, 79, 79); font-weight: bold;"
    } else { limpar_alerts_senhas() }
}

function check_senhas() {
    let senha1 = document.getElementById('senha')
    let senha2 = document.getElementById('senha2')

    if (senha1.value && senha2.value) {
        var conditions = [senha1.value != senha2.value, senha1.value.includes(" "), senha1.value.length < 4];

        var triggerer = (function () {
            let crimes = []
            for (var i = 0; i < conditions.length; i++) {
                if (conditions[i]) { crimes.push(i) };
            }
            return crimes;
        })();

        if (triggerer.length > 0) {
            limpar_alerts_senhas()
            for (i in triggerer) {
                switch (triggerer[i]) {
                    case 0:
                        senha1.style = senha2.style = 'border: 3px solid rgb(238, 79, 79)'
                        ativar_desativar_alerts_senhas(true, 'senhas_diferentes')
                        document.getElementById('btn-cadastrar').disabled = true
                        break;
                    case 1:
                        senha1.style = senha2.style = 'border: 3px solid rgb(238, 79, 79)'
                        ativar_desativar_alerts_senhas(true, 'caracteres_invalidos_senha')
                        document.getElementById('btn-cadastrar').disabled = true
                        break;
                    case 2:
                        senha1.style = senha2.style = 'border: 3px solid rgb(238, 79, 79)'
                        ativar_desativar_alerts_senhas(true, 'senha_curta')
                        document.getElementById('btn-cadastrar').disabled = true
                        break;
                    default:
                        break;
                }
            }
        } else {
            // Do something when everything is false
            senha1.style = senha2.style = 'border: 3px solid lightgreen'
            document.getElementById('btn-cadastrar').disabled = false
            limpar_alerts_senhas()
        }
    } else {
        senha1.style = senha2.style = ''
        document.getElementById('btn-cadastrar').disabled = false
        limpar_alerts_senhas()
    }

}