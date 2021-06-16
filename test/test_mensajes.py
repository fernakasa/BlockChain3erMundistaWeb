def test_mensaje_should_be_true_when_web_message_are_equals(page):
    page.goto("http://127.0.0.1:5000/registrar")
    messageEmail = page.inner_text("#registerForm > div:nth-child(1) > div")
    assert "Un email es requerido." == messageEmail
    messageMotivo = page.inner_text("#registerForm > div:nth-child(2) > div")
    assert "Debe seleccionar una opción." == messageMotivo
    messageFile = page.inner_text("#registerForm > div:nth-child(3) > div")
    assert "Seleccione un archivo." == messageFile
