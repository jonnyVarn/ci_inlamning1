import app
import requests



class AppTester():
    t1=request.get("http://127.0.0.1")
    assert r.status_code == 200, “API did not start correctly”
