from flask import Flask, render_template, make_response, abort, redirect, url_for
from flask.ext.bootstrap import Bootstrap
import os
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import sqlite3

app = Flask(__name__)

# Routing functions; allow for switching between pages when called

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/menu')
def menu():
    return render_template('menu.html')
    
@app.route('/cv')
def cv():
    return render_template('cv.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    

@app.route('/error')
@app.route('/errors')
def error():
    response = make_response('Oops, something goes wrong!', 404)
    return response

@app.route('/unexpected')
def unexpected():
    abort(404)
    return True

@app.route('/<path:path>')
def catch_all(path):
    return redirect('https://www.google.co.uk/search?q=' + path)
    
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'bgabrys.db'),
    SECRET_KEY='development key'
))
# Bootstrap(app)


# Form; allows data to be saved in the database

class messageForm(Form):
    name = StringField('Name:', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/view_form', methods=['GET', 'POST'])
def view_form():
    form = messageForm()
    # Uses JS validation to determine whether to run code; makes sure no fields are blank in the db
    if form.validate_on_submit(): 
        name = form.name.data
        email = form.email.data
        message = form.message.data
        with sqlite3.connect(app.config['DATABASE']) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO contact (name, email, message) VALUES (?,?,?)", [name, email, message])
            con.commit()

        return redirect(url_for('index'))
    return render_template('contact_show.html', form=form)



if __name__ == '__main__':
    Bootstrap(app)
    app.run(port=8080, host='0.0.0.0', debug=True)