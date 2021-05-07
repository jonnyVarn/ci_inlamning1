Jag skapar först ett repository på Github som jag döper till ci_inlamning1
Sedan skapar jag en readme med instruktionerna, en answers för frågorna och en report.
Sedan försöker jag komma på ett usecase för python med flask.
Jag clonar mitt skapade repo till desktop för att försöka få någonting gjort.
git clone https://github.com/jonnyVarn/ci_inlamning1/ och cd ci_inlamning1.
Jag bestämmer mig för att börja med en Dockerfile och stöter såklart på lite problem med dockerDesktop.
Så jag stänger ner docker engiene och startar utan resultat och uppgraderar till 3.3.2 då verkar det fungera.
Jag använder alpine Latest så From: Alpine: Latest
jag testar först i terminalen
docker run -ti alpine:latest
python --version finns inte så jag lägger till apk update && apk add python3 py-pip py-flask i dockerfile
sedan gör jag en git add * git commit -m "added Dockerfile" git push
Så jag har gjort en dockerfile och någonting meningslöst i flask som visar kontainer id och /headers om den är ok kan användas för test senare
Nu går jag in på circleCi och Set Up Project ci_inlamning1 det genereas ett yml jag får tänka lite på det så jag gör en test_app.py sålänge.
Bråkar runt lite med circle ci svårt att få en alpine nu fungerade alpine med python:3-alpine nu saknas flake8 så jag lägger till den i requrements.txt
Nu verkar det som någonting händer men det är väl lite fel i koden som inte gör någonting så jag får väl snygga till lite.
#!/bin/sh -eo pipefail
flake8  --statistics
pytest -v
./app.py:1:1: F401 'os' imported but unused
./app.py:2:1: E265 block comment should start with '# '
./app.py:4:1: F401 'flask.render_template' imported but unused
./app.py:6:1: F401 'flask_api.status' imported but unused
./app.py:9:1: E265 block comment should start with '# '
./app.py:14:1: E303 too many blank lines (3)
./app.py:18:1: E304 blank lines found after function decorator
./app.py:22:1: W293 blank line contains whitespace
./app.py:23:1: E302 expected 2 blank lines, found 1
./test_app.py:14:1: W293 blank line contains whitespace
./test_app.py:20:1: E305 expected 2 blank lines after class or function definition, found 1
./test_app.py:21:20: W292 no newline at end of file
2     E265 block comment should start with '# '
1     E302 expected 2 blank lines, found 1
1     E303 too many blank lines (3)
1     E304 blank lines found after function decorator
1     E305 expected 2 blank lines after class or function definition, found 1
3     F401 'os' imported but unused
1     W292 no newline at end of file
2     W293 blank line contains whitespace

Exited with code exit status 1
CircleCI received exit code 1

fortsätter krångla pip8 problem avklarade i app.py men test_app.py genererar
#!/bin/sh -eo pipefail
flake8  --statistics
pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /root/repo
collecting ... collected 0 items / 1 error                                                    

==================================== ERRORS ====================================
_________________________ ERROR collecting test_app.py _________________________
ImportError while importing test module '/root/repo/test_app.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/local/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_app.py:1: in <module>
    import app
app.py:5: in <module>
    from flask import Response, request, Flask
E   ModuleNotFoundError: No module named 'flask'
=========================== short test summary info ============================
ERROR test_app.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================

Exited with code exit status 2
CircleCI received exit code 2

Ja försöker med requests..

#!/bin/sh -eo pipefail
flake8  --statistics
pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /root/repo
collecting ... collected 0 items / 1 error                                                    

==================================== ERRORS ====================================
_________________________ ERROR collecting test_app.py _________________________
/usr/local/lib/python3.9/site-packages/urllib3/connection.py:169: in _new_conn
    conn = connection.create_connection(
/usr/local/lib/python3.9/site-packages/urllib3/util/connection.py:96: in create_connection
    raise err
/usr/local/lib/python3.9/site-packages/urllib3/util/connection.py:86: in create_connection
    sock.connect(sa)
E   ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:
/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:699: in urlopen
    httplib_response = self._make_request(
/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:394: in _make_request
    conn.request(method, url, **httplib_request_kw)
/usr/local/lib/python3.9/site-packages/urllib3/connection.py:234: in request
    super(HTTPConnection, self).request(method, url, body=body, headers=headers)
/usr/local/lib/python3.9/http/client.py:1253: in request
    self._send_request(method, url, body, headers, encode_chunked)
/usr/local/lib/python3.9/http/client.py:1299: in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
/usr/local/lib/python3.9/http/client.py:1248: in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
/usr/local/lib/python3.9/http/client.py:1008: in _send_output
    self.send(msg)
/usr/local/lib/python3.9/http/client.py:948: in send
    self.connect()
/usr/local/lib/python3.9/site-packages/urllib3/connection.py:200: in connect
    conn = self._new_conn()
/usr/local/lib/python3.9/site-packages/urllib3/connection.py:181: in _new_conn
    raise NewConnectionError(
E   urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7f613487ceb0>: Failed to establish a new connection: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:
/usr/local/lib/python3.9/site-packages/requests/adapters.py:439: in send
    resp = conn.urlopen(
/usr/local/lib/python3.9/site-packages/urllib3/connectionpool.py:755: in urlopen
    retries = retries.increment(
/usr/local/lib/python3.9/site-packages/urllib3/util/retry.py:574: in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
E   urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='127.0.0.1', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f613487ceb0>: Failed to establish a new connection: [Errno 111] Connection refused'))

During handling of the above exception, another exception occurred:
test_app.py:5: in <module>
    class AppTester():
test_app.py:6: in AppTester
    t1 = requests.get("http://127.0.0.1")
/usr/local/lib/python3.9/site-packages/requests/api.py:76: in get
    return request('get', url, params=params, **kwargs)
/usr/local/lib/python3.9/site-packages/requests/api.py:61: in request
    return session.request(method=method, url=url, **kwargs)
/usr/local/lib/python3.9/site-packages/requests/sessions.py:542: in request
    resp = self.send(prep, **send_kwargs)
/usr/local/lib/python3.9/site-packages/requests/sessions.py:655: in send
    r = adapter.send(request, **kwargs)
/usr/local/lib/python3.9/site-packages/requests/adapters.py:516: in send
    raise ConnectionError(e, request=request)
E   requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f613487ceb0>: Failed to establish a new connection: [Errno 111] Connection refused'))
=========================== short test summary info ============================
ERROR test_app.py - requests.exceptions.ConnectionError: HTTPConnectionPool(h...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.54s ===============================

Exited with code exit status 2
CircleCI received exit code 2

mina tester fungerar inte pep8 verkar fungera..

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
#!/bin/sh -eo pipefail
flake8  --statistics
pytest -v
============================= test session starts ==============================
platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /root/repo
collecting ... collected 0 items / 1 error                                                    

==================================== ERRORS ====================================
_________________________ ERROR collecting test_app.py _________________________
test_app.py:2: in <module>
    assert AppTester.testar == "ok"
E   AssertionError: assert <function testar at 0x7fa815de1c10> == 'ok'
E    +  where <function testar at 0x7fa815de1c10> = <module 'app' from '/root/repo/app.py'>.testar
=========================== short test summary info ============================
ERROR test_app.py - AssertionError: assert <function testar at 0x7fa815de1c10...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.30s ===============================

Exited with code exit status 2
CircleCI received exit code 2

