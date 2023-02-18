let servicoAtual = new Object();
let rowEditarAtual

function getFormValues() { 
    let formEl = document.forms.form
    let formData = new FormData(formEl)

    let data = {
        'nome': formData.get('nome-servico-input'),
        'valor': formData.get('valor-servico-input'),
        'disp': document.querySelector('#disponivel-servico-input').checked,
    }
    return data
}

function getFormEditarValues(id) {
    let data = {
        'nome': document.querySelector('#nome-servico-EDITAR').value,
        'valor': document.querySelector('#valor-servico-EDITAR').value,
        'disp': document.querySelector('#disponivel-servico-EDITAR').checked,
        'id': id,
    }
    return data
}

async function get_servicos() {
    let url = '/principal/servicos/save/';
    return (await fetchFactory('GET', url).then(dataReturned => atendimentoAtual = dataReturned))
}

async function post_servicos() {
    let url = '/principal/servicos/save/';
    await fetchFactory('POST', url, getFormValues())
    preencherTabelaServicos()
}

async function patch_servicos() {
    let url = '/principal/servicos/save/';
    body = getFormEditarValues(rowEditarAtual)
    await fetchFactory('PATCH', url, body)
    preencherTabelaServicos()
    cancelarEdição()
}

async function delete_servicos() {
    let url = '/principal/servicos/save/';
    body = getFormEditarValues(rowEditarAtual)
    await fetchFactory('DELETE', url, body)
    preencherTabelaServicos()
    cancelarEdição()
}

async function getServicos() {
    let url = '/principal/servicos/';
    await fetchFactory('GET', url)
}

async function preencherTabelaServicos() {
    var servicos = await get_servicos(true)
    var t = $('#table_servicos').DataTable();

    $('#table_servicos').DataTable().clear().draw();
    for (let i = 0; i < servicos.length; i++) {
        var disp = servicos[i]['disp'] ? 'Sim' : 'Não'
        t.row.add([servicos[i]['nome'], servicos[i]['valor'], disp, servicos[i]['id']]).draw(true)
    }
}

async function showEditarServicos(row) {
    document.querySelector('#row-criar-servico').classList.add('d-none')
    document.querySelector('#row-editar-servico').classList.remove('d-none')

    document.querySelector('#descricao-editar-servico').innerHTML = 'Editar Serviço "' + row[0] + '"'

    document.querySelector('#nome-servico-EDITAR').value = row[0]
    document.querySelector('#valor-servico-EDITAR').value = row[1]

    rowEditarAtual = row[3]
}

function cancelarEdição() {
    document.querySelector('#row-editar-servico').classList.add('d-none')
    document.querySelector('#row-criar-servico').classList.remove('d-none')
    rowEditarAtual = ''
}

$("#table_servicos tbody").on('click', 'button.btnEditar', async function () {
    var t = $('#table_servicos').DataTable();
    await showEditarServicos(t.row($(this).parents('tr')).data())
});

addEventListener("load", (event) => { preencherTabelaServicos() });