from flask_sqlalchemy import SQLAlchemy
from models.user import User

db = SQLAlchemy()

# récupération des données dans la base de données


def get_users():
    users = User.query.all()
    return users


def get_user_by_id(user_id):
    user = User.query.get(user_id)
    return user


def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user.id


def update_user(userData, user_id):
    db.session.query(User).filter(User.id==user_id).update({
        "nom":userData.nom ,
        "prenom": userData.prenom,
        "naissance": userData.naissance,
        "mail": userData.mail,
        "login": userData.login,
        "password": userData.password
    }) 
    db.session.commit()
    return "Utilisateur mis a jour"


def delete_user(user_id):
    user = db.session.query(User).filter(User.id==user_id).first()
    db.session.delete(user)
    db.session.commit()
    return "utilisateur supprimé"