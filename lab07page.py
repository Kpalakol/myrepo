from flask import Flask, render_template, request, redirect, Markup
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    identifier = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(50), nullable=False)
    l_name = db.Column(db.String(50), nullable=False)
    id_email = db.Column(db.String(100), unique=True, nullable=False)
    pass_word = db.Column(db.String(100), nullable=False)

@app.route('/')
def signin():
    return render_template('signin.html', error_message="")

@app.route('/signin', methods=['POST'])
def signin_post():
    id_email = request.form.get('id_email')
    pass_word = request.form.get('pass_word')

    user = User.query.filter_by(id_email=id_email).first()

    if user and user.pass_word == pass_word:
        return redirect('/secretpage')
    else:
        error_message = 'Invalid key id_email or pass_word.'
        return render_template('signin.html', error_message=error_message)

@app.route('/signup')
def signup():
    return render_template('signup.html', error_message="")

@app.route('/signup', methods=['POST'])
def signup_post():
    f_name = request.form.get('f_name')
    l_name = request.form.get('l_name')
    id_email = request.form.get('id_email')
    pass_word = request.form.get('pass_word')
    pswrd_cnfrm  = request.form.get('pswrd_cnfrm ')
    error_message=""

    if pass_word != pswrd_cnfrm :
        error_message = 'pass_word and confirm pass_word do not match.'
        return render_template('signup.html', error_message=error_message)

    if len(pass_word) < 8:
        error_message = 'Psswrd needs to be a minimum of eight characters long.<br>'
    
    if not any(char.islower() for char in pass_word):
        error_message += "A lowercase letter should be present in psswrd.<br>"

    if not any(char.isupper() for char in pass_word):
        error_message += "A lowercase letter should be present in psswrd.<br>"

    if not pass_word[-1].isdigit():
        error_message += "pass_word should end in a number.<br>"
        
    if error_message:
        error_message = Markup(error_message)
        return render_template('signup.html', error_message=error_message)

    new_user = User(f_name=f_name, l_name=l_name, id_email=id_email, pass_word=pass_word)

    try:
        db.session.add(new_user)
        db.session.commit()
    except IntegrityError:
        error_message = 'User with the given id_email already exists.'
        return render_template('signup.html', error_message=error_message)

    return redirect('/thankyou')

@app.route('/secretpage')
def secretpage():
    return render_template('secretpage.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)