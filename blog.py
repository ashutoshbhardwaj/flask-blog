from flask import Flask,render_template,request,session,\
    flash,redirect,url_for,g
from functools import  wraps
import sqlite3
import pdb

DATABASE='blog.db'
USERNAME='admin'
PASSWORD='admin'
SECRET_KEY='\xa9\x7f\xf2\x85{~\x01\xa9\xea\x1ck\xa3\xf6\x80\xa6\xd6\x8a\xfdw\xfaw7\xee\x93'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return test(*args,**kwargs)
        else:
            flash("You need to be logged in first")
            return redirect(url_for('login'))
    return wrap


@app.route('/',methods=['GET','POST'])
def login():
  #  pdb.set_trace()
    error=None
    status_code=200
   # print("Inside login method,request.method= {},request.form.user = {}\
    #    ,form.password={}".format(request.method,request.form['username'],request.form['password']))
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            print("inside if")
            error = 'Invalid Credentials. Please try again'
            status_code = 401
        else:
            print("inside else")
            session['logged_in'] = True
            return redirect(url_for('main'))
    print("outside login, before rendering")
    return  render_template('login.html',error=error), status_code


@app.route('/main')
@login_required
def main():
    flash('You  are logged  in')
    g.db=connect_db()
    cursor=g.db.execute("select * from posts")
    posts=[dict(title=row[0],post=row[1]) for row in cursor.fetchall()]
    return render_template('main.html',posts=posts)


@app.route('/logout')
def logout():
    session.pop('logged_in',    None)
    flash('You  were    logged  out')
    return  redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
