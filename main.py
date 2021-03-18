from flask import Flask, render_template
import logging
app = Flask(__name__)
author = "Gábor"

hirek = [
    {'cim': "Minta hír", 'dt': "2021-03-17", 'szerzo': "1", 'id':'5324113'},
    {'cim': "Minta hír2", 'dt': "2021-03-16", 'szerzo': "1", 'id':'423423423'},
    {'cim': "Minta hír3", 'dt': "2021-03-16", 'szerzo': "1",'id':'9896323'},
    {'cim': "Minta hír4", 'dt': "2021-03-16", 'szerzo': "2",'id':'334534534'},
    {'cim': "COVID Oltás", 'dt': "2021-03-17", 'szerzo': "2",'id':'3453'},
    {'cim': "Kutya örökbefogadás", 'dt': "2021-03-17", 'szerzo': "3",'id':'234321'},
    {'cim': "Macska örökbefogadás", 'dt': "2021-03-14", 'szerzo': "3",'id':'13121'},
    {'cim': "Budapest futóversenyei", 'dt': "2021-03-13", 'szerzo': "1",'id':'123123'}
]

hir_szoveg = [
    {'id':'5324113', "szoveg":"Ez az első mintahír, jöjjenek vissza késöbb többért"},
    {'id':'423423423', "szoveg":"Ez a második minthahír, ebben már van <h2>html tag is.</h2> Itt a <a href='http://www.google.hu'>Google</a> linkje." },
    {'id':'9896323', "szoveg":"Nincs még feltöltött hír"}
]

cikkiro = [
    {'id':'1', 'nev':'Gábor', 'leiras':'szeret cikkeket írni és webprogramozni'},
    {'id':'2', 'nev':'Padlizsán', 'leiras':'Szeret Gábor cuccain ugrálni'},
    {'id':'3', 'nev':'Író Kálmán', 'leiras':'Már 20 éve ír cikkeket...'}
]

@app.route("/")
def index():
    return render_template("index.html", name=author)

@app.route("/blog")

def blog():
    hirek_db = getCikkIro()
    app.logger.warning(hirek_db)
    return render_template("blog.html",hirek = hirek_db, today="2021-03-17", name=author)

def getCikkIro():
    hirek_join = []
    for hir in hirek:
        for iro in cikkiro:
            if hir['szerzo'] == iro['id']:
                tmp_dict = iro.copy()
                tmp_dict.update(hir)
                hirek_join.append(tmp_dict)
    return hirek_join

@app.route("/hirek/<string:hir_id>")
def getHir(hir_id):
    aktualis_hir = {}
    for hir in hirek:
        if(hir['id'] == hir_id):
            aktualis_hir = hir
    content = getHirById(aktualis_hir['id'])

    return render_template("hirek.html", name=author, hir=aktualis_hir, szoveg=content)
def getHirById(id):
    szoveg = "Nincs feltöltött szöveg."
    for hir in hir_szoveg:
        if hir['id'] == id:
            szoveg = hir["szoveg"]
    return szoveg




if __name__ == "__main__":
    app.run(debug=True)