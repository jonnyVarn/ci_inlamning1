import app
# import requests


class AppTester():
    t2 = app.testar
    assert t2 == "ok", 'working'

#    t1 = requests.get("http://127.0.0.1:80")
#    assert t1.status_code == 200, 'No Work'

   
