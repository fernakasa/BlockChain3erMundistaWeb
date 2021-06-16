def test_mensaje_should_be_true_when_web_message_are_equals(page):
    page.goto("http://127.0.0.1:5000/validar")
    messageEmail = page.inner_text("#validateForm > div > div")
    assert "Ingrese el Codigo de Validación." == messageEmail
