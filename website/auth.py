from flask import Blueprint,render_template,request,flash

auth=Blueprint('auth',__name__)

@auth.route("/login",methods=['GET','POST'])
def login():
    data=request.form
    email=data.get('email')
    pwd=data.get('password')
    return render_template("login.html")

@auth.route("/logout",methods=['GET','POST'])
def logout():
    return render_template("home.html")

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method=='POST':
        data=request.form
        email=data['email']
        name =data['name']
        pwd1= data['password1']
        pwd2= data['password2']

        if len(email)<4:
            flash("email must be valid",category="error")
        elif len(name)<2:
            flash("name should be greater than 1 character",category="error")
        elif len(pwd1)<7:
            flash("length of password must be greater than 6 characters",category="error")
        elif pwd1 != pwd2:
            flash("password should be same",category="error")
        else:
            flash("account created",category="success")
    return render_template("signup.html")