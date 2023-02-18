
async function get_agendamentos() {
    let url = `/principal/agendamento/save/`;
    return (await fetchFactory('GET', url))
}

async function preencherTabelaMeusAgendamentos() {
    var agendamentos = await get_agendamentos()
    var t = $('#table_agendamentos').DataTable();
    $('#table_agendamentos').DataTable().clear().draw();
    for (let i = 0; i < agendamentos.length; i++) {
        t.row.add([agendamentos[i]['id_cliente'], agendamentos[i]['id'], agendamentos[i]['servico'], agendamentos[i]['data_reservada'], agendamentos[i]['data_de_criacao'], agendamentos[i]['valor']]).draw(true)
    }
}

addEventListener("load", (event) => { preencherTabelaMeusAgendamentos() });