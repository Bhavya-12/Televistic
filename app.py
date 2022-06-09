from flask import *
import sqlite3
app=Flask(__name__)
@app.route("/")
def Home():
    database=sqlite3.connect("dba.db")
    cursor=database.cursor()
    query = "select poster ,name from {n} limit 6".format(n='Movies')
    cursor.execute(query)
    list1=cursor.fetchall()
    database=sqlite3.connect("dba.db")
    cursor=database.cursor()
    query = "select poster ,name from {n} limit 6".format(n='Series')
    cursor.execute(query)
    list2=cursor.fetchall()
    database=sqlite3.connect("dba.db")
    cursor=database.cursor()
    query = "select poster ,name from {n} limit 6".format(n='Shows')
    cursor.execute(query)
    list3=cursor.fetchall()       
    return render_template('index.html',img1=list1,img2=list2,img3=list3)
 
@app.route('/<pg>')
def open(pg):
    database=sqlite3.connect("dba.db")
    cursor=database.cursor()
    query = "select poster ,name from {n} limit 6".format(n=pg)
    cursor.execute(query)
    list=cursor.fetchall()
    cursor=database.cursor()
    query = "select poster ,name from {n} order by poster desc limit 6".format(n=pg)
    cursor.execute(query)
    list1=cursor.fetchall()
    cursor=database.cursor()
    query = "select poster ,name from {n} limit 6".format(n=pg)
    cursor.execute(query)
    list1=cursor.fetchall()
    cursor=database.cursor()
    query = "select Movies.poster from Movies,Movie_Director where year_ = '2021' and Movie_Director.movie_id = Movies.movie_id"
    cursor.execute(query)
    list2=cursor.fetchall()
    cursor=database.cursor()
    query = "select Movies.poster from Movies,Movie_Director where year_ = '2019' and Movie_Director.movie_id = Movies.movie_id"
    cursor.execute(query)
    list3=cursor.fetchall()
    query = "select Movies.poster from Movies,Movie_Director where year_ = '2018' and Movie_Director.movie_id = Movies.movie_id"
    cursor.execute(query)
    list4=cursor.fetchall()
    return  render_template('everything.html',title=pg,imgs=list,img2=list3,img3=list2,img4 = list4)

@app.route("/mv=<name>")
def sel(name):
    return render_template('selected.html',mv=name)


if __name__ == '__main__':
    app.run(debug=True)