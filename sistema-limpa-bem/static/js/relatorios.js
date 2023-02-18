
async function get_atendimentos_dia(param) {
    let url = `/principal/atendimento/save/${param}/`;
    return (await fetchFactory('GET', url))
}

async function get_atendimentos() {
    let url = `/principal/atendimento/save/`;
    return (await fetchFactory('GET', url))
}

async function preencherTabelaRelatorios(param) {
    if (param == 1) {
        var atendimentos = await get_atendimentos_dia('dia')
    } else if (param == 2) {
        var atendimentos = await get_atendimentos_dia('mes')
    } else {
        var atendimentos = await get_atendimentos()
    }

    var t = $('#table_relatorios').DataTable();
    console.log(atendimentos)
    $('#table_relatorios').DataTable().clear().draw();
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

addEventListener("load", (event) => { preencherTabelaRelatorios(0) });