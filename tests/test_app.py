
import app.app as app_module

def test_health():
    client = app_module.app.test_client()
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json.get('status') == 'ok'
