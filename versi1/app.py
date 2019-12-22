from flask import Flask, render_template
from mysql import connector

app = Flask(__name__)
db = connector.connect(
    host    ="localhost",
    user    ="root",
    passwd  ="",
    database="db_chord"
)

@app.route('/')
def halaman():
    cur = db.cursor()
    cur.execute("select * from artis")
    res = cur.fetchall()
    cur.close()
    return render_template("utama.html",hasil=res)

@app.route('/<artis>')
def artis(artis):
    cur = db.cursor()
    cur.execute("select * from lagu where artis=%s", (artis,))
    res = cur.fetchall()
    cur.close()
    return render_template("lagu.html", hasil=res)

@app.route('/chord-<lagu>')
def chord(lagu):
    cur = db.cursor()
    cur.execute("select * from chord where lagu=%s", (lagu,))
    res = cur.fetchall()
    cur.close()
    return render_template("chord.html", hasil=res)

@app.route('/kelompok')
def kelompok():
    return render_template("kelompok.html")

if __name__ == '__main__':
    app.run()
