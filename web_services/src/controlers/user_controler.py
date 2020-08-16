from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
import services.user_service as userService
from dto.user_dto import UserDto

# crréation d'une classe qui hérite de FlaskView


class UsersControler(FlaskView):
    # définition d'une route de base
    route_base = '/api/users/'

    # dééfinition de l'extension de la route de base
    @route('/')
    def get_users(self):  
        users = userService.get_users()  
        return jsonify(users)

    @route('/<int:user_id>')
    def get_user_by_id(self, user_id):
        user = userService.get_user_by_id(user_id)
        return jsonify(user)

    @route('/',methods=['POST'])
    def create_user(self):
        nom = request.json['nom']
        prenom = request.json['prenom']
        mail = request.json['mail']
        naissance = request.json['naissance']
        login = request.json['login']
        password = request.json['password']
        user = UserDto(nom, prenom, naissance, mail, login, password)
        return userService.create_user(user)


    @route('/<int:user_id>', methods=['PUT'])
    def update_user(self, user_id):
        nom = request.json['nom']
        prenom = request.json['prenom']
        mail = request.json['mail']
        naissance = request.json['naissance']
        login = request.json['login']
        password = request.json['password']
        user = UserDto(nom, prenom, naissance, mail, login, password)
        msg = userService.update_user(user , user_id)
        return jsonify(msg)

    @route('/<int:user_id>',methods=['DELETE'])
    def delete_user(self,user_id):
        # result = [user for user in tasks if user['id'] == user_id]
        # tasks.remove(result[0])
        deluser = userService.delete_user(user_id)
        return jsonify(deluser), 200
