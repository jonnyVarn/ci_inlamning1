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
