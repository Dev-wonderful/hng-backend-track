"""A simple flask app to handle crud operations"""
from flask import Flask, jsonify, request
from models import Users


app = Flask(__name__)


@app.route("/api", methods=['GET', 'POST', 'PUT', 'DELETE'], strict_slashes=False)
def index():
    """accepts CRUD request with query params"""
    if request.method == 'GET':
        print(f"Get: {request.args.get('name')}")
        name = request.args.get('name')
        user = Users.objects.get(name=name)
        return jsonify(user)
    if request.method == 'POST':
        print(f"Post: {request.form.get('name')}")
        name = request.form.get('name')
        new_user = Users(name=name)
        new_user.save()
    if request.method == 'PUT':
        print(f"Patch: {request.form.get('name')}")
    if request.method == 'DELETE':
        print(f"Delete: {request.args.get('name')}")
        print(request)
    
    return 'ok'

    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
