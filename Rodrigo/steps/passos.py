@given(u'que estou na página inicial do extra.com.br')
def step_impl(context):
    context.extra_pesquisa.home()


@when(u'digio na barra de pesquisa por unm item')
def step_impl(context):
    context.extra_pesquisa.search()
    context.extra_pesquisa.search_2()

@then(u'o resultado ira retornar a lista de jogos')
def step_impl(context):
    assert 'PS4 Jogos no Extra.com.br' in context.driver.title


@when(u'seleciono o jogo days gone')
def step_impl(context):
    context.extra_pesquisa.search_3()


@then(u'entra na pagina do jogo days gone')
def step_impl(context):
    assert 'Jogo Days Gone - PS4 - Jogos Playstation 4 no Extra.com.br' in context.driver.title


@when(u'colocar o cep para o calculo do frete')
def step_impl(context):
    context.extra_pesquisa.search_4()
    context.extra_pesquisa.search_5()

@then(u'aparece os valores do frete')
def step_impl(context):
    assert 'Jogo Days Gone - PS4 - Jogos Playstation 4 no Extra.com.br' in context.driver.title