@given(u'Aparece a tela principal do Extra')
def step_impl(context):
    context.ObjLogin.home_extra()
    context.ObjLogin.url_check()

@when(u'é clicado em Entre ou Cadastre-se')
def step_impl(context):
    context.ObjLogin.botao()

@then(u'A tela de login será aberta')
def step_impl(context):
    pass

@then(u'A Tela de login aparece')
def step_impl(context):
     context.ObjLogin.url_check()

@when(u'serão insiridas as credenciais do site')
def step_impl(context):
     context.ObjLogin.email()
     context.ObjLogin.senha()
     context.ObjLogin.atraso()
     context.ObjLogin.botao_continuar()

@then(u'O Captcha aparecerá')
def step_impl(context):
     pass
     
