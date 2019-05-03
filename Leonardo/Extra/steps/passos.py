@given(u'estou na pagina inicial do Extra.com.br')
def step_impl(context):
    context.driver.get('https://www.extra.com.br/')

@when(u'didito "Xiaomi" na barra de pesquisa')
def step_impl(context):
    context.pesquisa_extra.go_pesquisa()
    context.pesquisa_extra.go_buscar()

@then(u'irá aparecer os resultados dos produtos da marca')
def step_impl(context):
    assert 'Xiaomi no Extra.com.br' in context.driver.title

@when(u'seleciono a opcao Smartphone Xiaomi mi8 lite')
def step_impl(context):
    context.pesquisa_extra.go_smartphone()

@then(u'o navegador acessa a pagina do Smartphone')
def step_impl(context):
    assert 'Smartphone Xiaomi Mi 8 Lite Dual SIM 64GB - Aurora Azul - Android no Extra.com.br' in context.driver.title

@when(u'clico em Adicionar à lista de casamento')
def step_impl(context):
    context.pesquisa_extra.go_lista()

@then(u'o item será adicionado à lista')
def step_impl(context):
    assert 'Extra.com.br: o site da família e a maior loja de Informática do Brasil' in context.driver.title