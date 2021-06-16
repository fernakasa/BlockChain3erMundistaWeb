def test_titulo_should_be_true_when_web_title_are_equals(page):
    page.goto("http://127.0.0.1:5000/")
    titulo = page.title()
    assert "BlockChain3erMundista" == titulo