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