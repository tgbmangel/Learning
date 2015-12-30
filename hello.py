#coding:cp936
from flask import Flask
from flask import Flask, request, session, g, redirect, url_for, abort,render_template, flash
import urllib2
import sqlite3

app=Flask(__name__)


@app.route("/hello")
@app.route("/hello/<name><part>")
def hello_world(name=None,part=None):
    return render_template('hello.html',name=name,part=part)

@app.route("/lol",methods=['POST', 'GET'])
def index(daqu=None):
    # error = None
    if request.method == 'POST':
        part=request.form['lolpartion']
        user=request.form['loluserid']

        #return hello_world(name=user,part=part)
        return Search(part,user)
    # else:
    #     error = 'Invalid username/password'
    #     # the code below is executed if the request method
    # # was GET or the credentials were invalid
    return render_template("lol.html",daqu=daqu)

def Search(part,user):
    d=urllib2.urlopen("http://www.lolhelper.cn/").read()
    data={'daqu':part,'nickname':user}
    return d


if __name__=="__main__":
    app.run(debug=True)