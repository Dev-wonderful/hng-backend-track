"""A simple flask app to handle crud operations"""
from flask import Flask, jsonify, request
from mongoengine.errors import *
from models import Users


app = Flask(__name__)


@app.route("/api", methods=['POST'], strict_slashes=False)
@app.route("/api/<user_id>", methods=['GET', 'PUT', 'DELETE'],
           strict_slashes=False)
def index(user_id=None):
    """accepts CRUD request with dynamic id params"""

    if request.method == 'GET':
        try:
            user = Users.objects.get(id=user_id)
        except DoesNotExist:
            return 'user does not exist', 404
        except ValidationError:
            return 'user id must be a string', 403
        user_dict = {
            'id': str(user.id),
            'name': user.name
        }
        return jsonify(user_dict)

    if request.method == 'POST':
        name = request.form.get('name')
        print(f'name: {name}')
        print(f'name type: {type(name)}')
        new_user = Users(name=name)
        try:
            new_user.validate()
            new_user.save()
        except ValidationError:
            return 'name must be a string', 403
        return str(new_user.id)

    if request.method == 'PUT':
        name = request.form.get('name')
        try:
            user = Users.objects.get(id=user_id)
            user.name = name
            user.validate()
        except DoesNotExist:
            return 'User does not exist', 404
        except ValidationError:
            return 'name and id must be a string', 403
        user.save()
        return 'success'

    if request.method == 'DELETE':
        try:
            user = Users.objects.get(id=user_id)
            user.delete()
        except DoesNotExist:
            return 'User does not exist', 404
        except ValidationError:
            return 'user id must be a string', 403

        return 'success'
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
