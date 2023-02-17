
function getFormValues() {
    let formEl = document.forms.form
    let formData = new FormData(formEl)

    let data = {
        'atendente': formData.get('id-atendente'),
        'helper': formData.get('id-helper'),
        'cliente': formData.get('id-cliente'),
        'servico': formData.get('id-servico'),
        'data-hora': formData.get('dth-limpeza'),
        'preco': formData.get('preco'),
        'situacao': formData.get('situacao'),
        'pagamento': formData.get('pagamento'),
        'nome-cliente': formData.get('nome'),
        'telefone-cliente': formData.get('telefone'),
        'logradouro-cliente': formData.get('logradouro'),
        'numero-casa-cliente': formData.get('numero'),
        'cidade-cliente': formData.get('cidade'),
        'estado-cliente': formData.get('estado')
    }
    return data
}

async function post_atendimento() {
    let url = '/principal/atendimento/save/';
    await fetchFactory('POST', url, getFormValues())
}

async function get_servicos() {
    let url = '/principal/servicos/save/';
    return (await fetchFactory('GET', url).then(dataReturned => servicoAtual = dataReturned))
}

async function get_usuario(campo_a_pesquisar, valor_a_pesquisar) {
    let url = `/principal/usuarios/get/usuario/${campo_a_pesquisar}/${valor_a_pesquisar}/`
    return (await fetchFactory('GET', url).then(dataReturned => servicoAtual = dataReturned))
}

function preencherDadosCliente(limpar, usuario) {
    if (!limpar) {
        document.getElementById('nome').value = usuario['first_name']
        document.getElementById('telefone').value = usuario['telefone']
        document.getElementById('email').value = usuario['email']
        document.getElementById('logradouro').value = usuario['logradouro']
        document.getElementById('numero').value = usuario['numero']
        document.getElementById('cidade').value = usuario['cidade']
        document.getElementById('estado').value = usuario['estado']
    } else {
        document.getElementById('nome').value = ''
        document.getElementById('telefone').value = ''
        document.getElementById('email').value = ''
        document.getElementById('logradouro').value = ''
        document.getElementById('numero').value = ''
        document.getElementById('cidade').value = ''
        document.getElementById('estado').value = ''
    }
}

async function pesquisarCadastro(tipo, valor_a_pesquisar) {
    var id
    tipo == 1 ? id = 'helper' : tipo == 2 ? id = 'atendente' : id = 'cliente';
    if (!valor_a_pesquisar) {
        document.getElementById(id).focus()
    } else {
        try {
            var campos = {
                '0': 'username', '1': 'nome', '2': 'email', '3': 'telefone'
            }
            var campo_a_pesquisar = campos[document.getElementById(`campo_` + id).value]

            var usuario = await get_usuario(campo_a_pesquisar, valor_a_pesquisar)
            document.getElementById(id).style = 'border: 2px solid lightgreen;'

            document.getElementById('id-' + id).value = usuario['id']

            if (id == 'cliente') {
                preencherDadosCliente(false, usuario)
            }
        } catch (error) {
            console.log(error)
            document.getElementById(id).style = 'border: 2px solid red; color: red'
            document.getElementById(id).value = 'Não encontrado'
            preencherDadosCliente(true, false)
        }

    }
    // var usuarios = await get_usuarios()
}

async function preencherValorServico(nome) {
    var servicos = await get_servicos()
    for (let i = 0; i < servicos.length; i++) {
        if (nome == servicos[i]['nome']) {
            document.querySelector('#preco').value = servicos[i]['valor']
            document.querySelector('#id-servico').value = servicos[i]['id']
            return
        }
    }
    document.querySelector('#preco').value = ''
}

async function preencherSelectServicos() {
    var servicos = await get_servicos()
    for (let i = 0; i < servicos.length; i++) {
        if (servicos[i]['disp']) {
            document.querySelector('#select_servico').innerHTML += `<option value="${servicos[i]['nome']}">${servicos[i]['nome']}</option>`;
        }
    }
}

function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('relogio').innerHTML = h + ":" + m + ":" + s;
    setTimeout(startTime, 1000);
}

function checkTime(i) {
    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;
}

addEventListener("load", (event) => { preencherSelectServicos(); preencherValorServico(document.querySelector('#select_servico').value); startTime() });