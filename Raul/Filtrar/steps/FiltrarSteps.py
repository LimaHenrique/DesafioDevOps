@given(u'A página principal do Extra está aberta')
def step_impl(context):
    context.ObjFiltrar.home_extra()
    assert 'Extra.com.br: o site da família e a maior loja de Informática do Brasil' in context.driver.title

@when(u'È iniciado uma pesquisa por Celular')
def step_impl(context):
    context.ObjFiltrar.pesquisar()


@then(u'Os resultados de celulares deverão aparecer')
def step_impl(context):
    pass


@then(u'A página dos resultados de celulares está aberta')
def step_impl(context):
    assert 'Celular no Extra.com.br' in context.driver.title


@when(u'É clicado na opção de filtro Capa para Celular')
def step_impl(context):
    context.ObjFiltrar.filtrar1()


@then(u'Capa de Celulares aparecerão')
def step_impl(context):
    assert context.driver.page_source.find('https://buscando2.extra.com.br/busca?q=Celular&common_filter%5B1%5D=144290')


@when(u'A opção R$ 20 a R$ 30 é selecionada')
def step_impl(context):
    context.ObjFiltrar.filtrar2()


@then(u'Os resultados filtrados aparecerão')
def step_impl(context):
    assert context.driver.page_source.find('https://buscando2.extra.com.br/busca?q=Celular&common_filter%5B1%5D=144290&range_filter%5B2%5D=20:30:3')


@when(u'A opção Samsung é selecionada')
def step_impl(context):
    context.ObjFiltrar.filtrar3()


@then(u'Os resultados filtrados para capas de celulares Samsung aparecerão')
def step_impl(context):
    assert context.driver.page_source.find('https://buscando2.extra.com.br/busca?q=Celular&common_filter%5B1%5D=144290&common_filter%5B3341%5D=3528&range_filter%5B2%5D=20:30:3')