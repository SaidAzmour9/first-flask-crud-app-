from flask import Blueprint,Flask,render_template,request,redirect,url_for,flash,session
import sqlite3


views = Blueprint('views',__name__)
@views.route('/')
def home():
    con=sqlite3.connect("database.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from Livres")
    data = cur.fetchall()
    print(data)
    return render_template('home.html',datas=data)

@views.route('/add')
def add():
    return render_template('add.html')

@views.route('/edit')
def edit():
    return render_template('edit.html')