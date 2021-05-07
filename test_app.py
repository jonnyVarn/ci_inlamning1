import app
import requests


class AppTester():
    t1 = requests.get("http://127.0.0.1")
    assert t1.status_code == 200, 'No Work'

    t2 = app.testar
    assert t2 == "ok", 'working'
