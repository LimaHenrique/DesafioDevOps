#import assertpy

@given(u'Estou na tela principal do Extra')
def step_impl(context):
    context.Extra.home_extra()

@when(u'Clico na opção localizador de lojas')
def step_impl(context):
    context.Extra.botao()

@then(u'A página de localização de loja se abrirá')
def step_impl(context):
    assert 'Extra.com.br: o site da família e a maior loja de Informática do Brasil' in  context.driver.title
    
@then(u'Estou na página de localização de loja')
def step_impl(context):
    context.driver.switch_to_window(context.driver.window_handles[1])
    assert 'Buscador de lojas' in context.driver.title
    
@when(u'insiro minha localização')
def step_impl(context):
    context.Extra.localizacao()

@when(u'clico na opção procurar')
def step_impl(context):
    context.Extra.pesquisar()

@then(u'a loja mais próxima a mim será mostrada')
def step_impl(context):
    context.driver.switch_to_window(context.driver.window_handles[1])
    assert context.driver.page_source.find("DIAS")