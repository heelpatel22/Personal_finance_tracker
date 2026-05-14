from flask import Blueprint,render_template,url_for,request,flash,redirect
from models import db,bcrypt
from models.user import User
from flask_login import login_user,logout_user,login_required,current_user

auth = Blueprint("auth",__name__)

@auth.route("/register",methods=['Get','Post'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account Created Successfully!','success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password,password):
            login_user(user)
            return redirect(url_for('dashboard.dashboard_view'))
        else:
            flash('Invalid credentials','danger')
    return render_template('login.html')

# @auth.route('/dashboard')
# @login_required
# def dashboard():
#     return render_template('dashboard.html',user=current_user)


@auth.route('/logout')
@login_required
def logout():
    return redirect(url_for('auth.login'))
