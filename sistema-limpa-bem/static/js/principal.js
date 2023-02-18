let atendimentoAtual = new Object();
let rowEditarAtual

function getFormValues() {
    let formEl = document.forms.form
    let formData = new FormData(formEl)

    let data = {
        'atendente': formData.get('id-atendente'),
        'helper': formData.get('id-helper'),
        'cliente': formData.get('id-cliente'),
        'servico': formData.get('id-servico'),
        'data_hora': formData.get('dth-limpeza'),
        'preco': formData.get('preco'),
        'situacao': formData.get('situacao'),
        'pagamento': formData.get('pagamento'),
        'nome_cliente': formData.get('nome'),
        'telefone_cliente': formData.get('telefone'),
        'logradouro_cliente': formData.get('logradouro'),
        'numero_casa_cliente': formData.get('numero'),
        'cidade_cliente': formData.get('cidade'),
        'estado_cliente': formData.get('estado'),
        'data_criacao_atendimento': (new Date().getUTCFullYear().toString()) + '-' + (new Date().getUTCMonth().toString()) + '-' + (new Date().getDate().toString()) + ' ' + (new Date().getHours().toString()) + ':' + (new Date().getMinutes().toString())
    }
    console.log(data['data_criacao_atendimento'])
    return data
}

function getFormValuesEditar() {
    let formEl = document.getElementById('form-editar')
    let formData = new FormData(formEl)

    let data = {
        'id': atendimentoAtual[0]['id'],
        'atendente': formData.get('id-atendente-editar'),
        'helper': formData.get('id-helper-editar'),
        'cliente': formData.get('id-cliente-editar'),
        'servico': formData.get('id-servico-editar'),
        'data_hora': formData.get('dth-limpeza-editar'),
        'preco': formData.get('preco-editar'),
        'situacao': formData.get('situacao-editar'),
        'pagamento': formData.get('pagamento-editar'),
        'nome_cliente': formData.get('nome-editar'),
        'telefone_cliente': formData.get('telefone-editar'),
        'logradouro_cliente': formData.get('logradouro-editar'),
        'numero_casa_cliente': formData.get('numero-editar'),
        'cidade_cliente': formData.get('cidade-editar'),
        'estado_cliente': formData.get('estado-editar'),
        'data_criacao_atendimento': (new Date().getUTCFullYear().toString()) + '-' + (new Date().getUTCMonth().toString()) + '-' + (new Date().getDate().toString()) + ' ' + (new Date().getHours().toString()) + ':' + (new Date().getMinutes().toString())
    }
    console.log(data['data_criacao_atendimento'])
    return data
}

async function get_atendimentos() {
    let url = '/principal/atendimento/save/';
    return (await fetchFactory('GET', url))
}

async function get_atendimento_by_id(id) {
    let url = `/principal/atendimento/save/${id}/`;
    return (await fetchFactory('GET', url).then(dataReturned => atendimentoAtual = dataReturned))
}

async function post_atendimento() {
    console.log('fazendo POST')
    let url = '/principal/atendimento/save/';
    await fetchFactory('POST', url, getFormValues())
}

async function patch_atendimento() {
    console.log('fazendo PATCH')
    let url = '/principal/atendimento/save/';
    await fetchFactory('PATCH', url, getFormValuesEditar())
}

async function get_servicos() {
    let url = '/principal/servicos/save/';
    return (await fetchFactory('GET', url))
}

async function get_usuario(campo_a_pesquisar, valor_a_pesquisar) {
    let url = `/principal/usuarios/get/usuario/${campo_a_pesquisar}/${valor_a_pesquisar}/`
    return (await fetchFactory('GET', url))
}

function preencherDadosCliente(limpar, usuario, editar) {
    var id_nome = 'nome'
    var id_tel = 'telefone'
    var id_email = 'email'
    var id_log = 'logradouro'
    var id_num = 'numero'
    var id_cidade = 'cidade'
    var id_estado = 'estado'

    if (editar) {
        id_nome += '-editar'
        id_tel += '-editar'
        id_email += '-editar'
        id_log += '-editar'
        id_num += '-editar'
        id_cidade += '-editar'
        id_estado += '-editar'
    }

    if (!limpar) {
        document.getElementById(id_nome).value = usuario['first_name']
        document.getElementById(id_tel).value = usuario['telefone']
        document.getElementById(id_email).value = usuario['email']
        document.getElementById(id_log).value = usuario['logradouro']
        document.getElementById(id_num).value = usuario['numero']
        document.getElementById(id_cidade).value = usuario['cidade']
        document.getElementById(id_estado).value = usuario['estado']
    } else {
        document.getElementById(id_nome).value = ''
        document.getElementById(id_tel).value = ''
        document.getElementById(id_email).value = ''
        document.getElementById(id_log).value = ''
        document.getElementById(id_num).value = ''
        document.getElementById(id_cidade).value = ''
        document.getElementById(id_estado).value = ''
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

async function preencherSelectServicos(editar) {
    var servicos = await get_servicos()
    id = 'select_servico'
    if (editar) { id += '-editar' }
    document.getElementById(`${id}`).innerHTML = '<option value="0">Nenhum</option>'
    for (let i = 0; i < servicos.length; i++) {
        if (servicos[i]['disp']) {
            document.getElementById(`${id}`).innerHTML += `<option value="${i + 1}">${servicos[i]['nome']}</option>`;
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
    document.getElementById('relogio-editar').innerHTML = h + ":" + m + ":" + s;
    setTimeout(startTime, 1000);
}

function checkTime(i) {
    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;
}

async function preencherTabelaAtendimentos() {
    var atendimentos = await get_atendimentos()
    var t = $('#table_atendimentos').DataTable();

    $('#table_atendimentos').DataTable().clear().draw();
    for (let i = 0; i < atendimentos.length; i++) {
        t.row.add([
            atendimentos[i]['id'],
            atendimentos[i]['atendente'],
            atendimentos[i]['helper'],
            atendimentos[i]['cliente'],
            atendimentos[i]['servico'],
            atendimentos[i]['data_hora'],
            atendimentos[i]['data_criacao_atendimento'],
            atendimentos[i]['preco'],
            atendimentos[i]['situacao'],
            atendimentos[i]['pagamento'],
            atendimentos[i]['nome_cliente'],
            atendimentos[i]['telefone_cliente'],
            atendimentos[i]['logradouro_cliente'],
            atendimentos[i]['numero_casa_cliente'],
            atendimentos[i]['cidade_cliente'],
            atendimentos[i]['estado_cliente']
        ]).draw(true)
    }
}

async function preencherAtendimentoEditar() {
    document.querySelector('#descricao-editar-atendimento').innerHTML = 'Editar Serviço, id = "' + atendimentoAtual[0]['id'] + '"'
    document.querySelector('#id-atendente-editar').value = atendimentoAtual[0]['atendente']
    document.querySelector('#id-helper-editar').value = atendimentoAtual[0]['helper']
    document.querySelector('#id-cliente-editar').value = atendimentoAtual[0]['cliente']
    document.querySelector('#id-servico-editar').value = atendimentoAtual[0]['servico']
    document.querySelector('#select_servico-editar').value = atendimentoAtual[0]['servico'].toString()
    document.querySelector('#preco-editar').value = atendimentoAtual[0]['preco']
    document.querySelector('#situacao-editar').value = atendimentoAtual[0]['situacao']
    document.querySelector('#pagamento-editar').value = atendimentoAtual[0]['pagamento']

    document.querySelector('#dth-limpeza-editar').value = atendimentoAtual[0]['data_hora'].substring(0, atendimentoAtual[0]['data_hora'].length - 9)

    var cliente = await get_usuario('id', atendimentoAtual[0]['cliente'])
    var atendente = await get_usuario('id', atendimentoAtual[0]['atendente'])
    var helper = await get_usuario('id', atendimentoAtual[0]['helper'])

    document.querySelector('#cliente-editar').value = cliente['username']
    document.querySelector('#atendente-editar').value = atendente['username']
    document.querySelector('#helper-editar').value = helper['username']

    preencherDadosCliente(false, cliente, true)
}

async function showEditarAtendimentos(row) {
    document.querySelector('#form').classList.add('d-none')
    document.querySelector('#form-editar').classList.remove('d-none')
    await preencherSelectServicos(true)
    await get_atendimento_by_id(row[0])

    preencherAtendimentoEditar()

    rowEditarAtual = row[3]
}

function cancelarEdição() {
    document.querySelector('#form-editar').classList.add('d-none')
    document.querySelector('#form').classList.remove('d-none')
    rowEditarAtual = ''
}

$("#table_atendimentos tbody").on('click', 'button.btnEditar', async function () {
    var t = $('#table_atendimentos').DataTable();
    await showEditarAtendimentos(t.row($(this).parents('tr')).data())
});

addEventListener("load", (event) => { preencherSelectServicos(); preencherValorServico(document.querySelector('#select_servico').value); startTime(); preencherTabelaAtendimentos() });