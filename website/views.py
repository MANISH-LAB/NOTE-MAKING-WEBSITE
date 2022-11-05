
from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import current_user,login_required
from .models import Note,User
from . import db
import json
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        note=request.form.get('note')
        if len(note)<1:
            flash("note is too short",category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("note added",category="success")


    return render_template("home.html", user=current_user)

@views.route('/deleteNote',methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteID=note['noteID']
    x=Note.query.get(noteID)
    if x:
        if x.user_id==current_user.id:
            db.session.delete(x)
            db.session.commit()
    return jsonify({})