
function getFormValues() {
    let formEl = document.forms.form
    let formData = new FormData(formEl)

    let data = {
        'id_cliente': formData.get('id-cliente'),
        'servico': formData.get('id-servico'),
        'data_reservada': formData.get('dth-limpeza'),
        'data_de_criacao': (new Date().getUTCFullYear().toString()) + '-' + (new Date().getUTCMonth().toString()) + '-' + (new Date().getDate().toString()) + ' ' + (new Date().getHours().toString()) + ':' + (new Date().getMinutes().toString()),
        'valor': formData.get('preco'),
    }
    return data
}



async function get_servicos() {
    let url = '/principal/servicos/cliente/';
    return (await fetchFactory('GET', url))
}

async function delete_agendamento(row) {
    let url = '/principal/agendamento/save/';
    let data = { 'id': row[0] }
    console.log(data)
    await fetchFactory('DELETE', url, data)
}

async function get_agendamentos() {
    let url = '/principal/agendamento/save/';
    return (await fetchFactory('GET', url, getFormValues()))
}

async function post_agendamento() {
    let url = '/principal/agendamento/save/';
    await fetchFactory('POST', url, getFormValues())
}

async function preencherValorServico(nome) {
    var servicos = await get_servicos()
    for (let i = 0; i < servicos.length; i++) {
        if (nome == servicos[i]['nome']) {
            document.querySelector('#preco').value = servicos[i]['valor']
            document.querySelector('#id-servico').value = servicos[i]['id']

            valor_servico_atual = servicos[i]['valor']
            return
        }
    }
    document.querySelector('#preco').value = ''
    document.querySelector('#id-servico').value = ''
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

async function preencherTabelaMeusAgendamentos() {
    var agendamentos = await get_agendamentos()
    var t = $('#table_agendamentos').DataTable();

    $('#table_agendamentos').DataTable().clear().draw();
    for (let i = 0; i < agendamentos.length; i++) {
        t.row.add([agendamentos[i]['id'], agendamentos[i]['servico'], agendamentos[i]['data_reservada'], agendamentos[i]['data_de_criacao'], agendamentos[i]['valor']]).draw(true)
    }
}

$("#table_agendamentos tbody").on('click', 'button.btnExcluir', async function () {
    var t = $('#table_agendamentos').DataTable();
    await delete_agendamento(t.row($(this).parents('tr')).data());
    await preencherTabelaMeusAgendamentos();
});

addEventListener("load", (event) => { preencherSelectServicos(); preencherValorServico(document.querySelector('#select_servico').value); preencherTabelaMeusAgendamentos() });