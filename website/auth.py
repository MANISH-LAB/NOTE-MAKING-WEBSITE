from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,logout_user,current_user,login_required
auth=Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
  if request.method=='POST':
    data=request.form
    email=data.get('email')
    pwd=data.get('password')
    user= User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password,pwd):
            flash("logged in successfully",category="success")
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
        else:
            flash("wrong password",category='error')
    else:
        flash("user doesnot exist",category='error')
  return render_template("login.html",user=current_user)

@auth.route("/logout",methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method=='POST':
        data=request.form
        email=data['email']
        name =data['name']
        pwd1= data['password1']
        pwd2= data['password2']
        user= User.query.filter_by(email=email).first()
        if user:
            flash("email already exists",category='error')
        elif len(email)<4:
            flash("email must be valid",category="error")
        elif len(name)<2:
            flash("name should be greater than 1 character",category="error")
        elif len(pwd1)<7:
            flash("length of password must be greater than 6 characters",category="error")
        elif pwd1 != pwd2:
            flash("password should be same",category="error")
        else:
            new_user= User(email=email,password=generate_password_hash(pwd1,method='sha256'),name=name)
            db.session.add(new_user)
            db.session.commit()
            flash("account created",category="success")
            return redirect(url_for('views.home'))
    return render_template("signup.html",user=current_user)