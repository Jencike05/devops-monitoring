from monitor import app

def test_root_endpoint():
    tester = app.test_client()
    response = tester.get('/')
    text = response.data.decode('utf-8')
    assert response.status_code == 200
    assert "CPU használat" in text
