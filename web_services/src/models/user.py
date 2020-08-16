from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# création d'une classe qui permettra de faire des objets qui mettront en forme les informations recus depuis la BDD


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    prenom = db.Column(db.String)
    naissance = db.Column(db.String)
    mail = db.Column(db.String)
    login = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, nom, prenom, naissance, mail, login, password):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.mail = mail
        self.login = login
        self.password = password

    def __repr__(self):
        return f'<User id:{self.id} nom:{self.nom} prenom:{self.prenom} naissance:{self.naissance} mail:{self.mail} login:{self.login} password:{self.password}>'