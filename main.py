from flask import Flask, render_template

app = Flask(__name__)
author = "Gábor"

hirek = [
    {'cim': "Minta hír", 'dt': "2021-03-17", 'szerzo': "Gábor", 'id':'5324113'},
    {'cim': "Minta hír2", 'dt': "2021-03-16", 'szerzo': "Gábor", 'id':'423423423'},
    {'cim': "Minta hír3", 'dt': "2021-03-16", 'szerzo': "Gábor",'id':'9896323'}
]

hir_szoveg = [
    {'id':'5324113', "szoveg":"Ez az első mintahír, jöjjenek vissza késöbb többért"},
    {'id':'423423423', "szoveg":"Ez a második minthahír, ebben már van <h2>html tag is.</h2> Itt a <a href='http://www.google.hu'>Google</a> linkje." },
    {'id':'9896323', "szoveg":"Nincs még feltöltött hír"}
]

@app.route("/")
def index():
    return render_template("index.html", name=author)
@app.route("/blog")
def blog():
    return render_template("blog.html",hirek =hirek , today="2021-03-17", name=author)
@app.route("/hirek/<string:hir_id>")
def getHir(hir_id):
    aktualis_hir = {}
    for hir in hirek:
        if(hir['id'] == hir_id):
            aktualis_hir = hir
    content = getHirById(aktualis_hir['id'])

    return render_template("hirek.html", name=author, hir=aktualis_hir, szoveg=content)
def getHirById(id):
    for hir in hir_szoveg:
        if hir['id'] == id:
            return hir["szoveg"]




if __name__ == "__main__":
    app.run()