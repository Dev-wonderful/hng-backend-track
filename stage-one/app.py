"""A simple flask app to handle a get request"""
from flask import Flask, jsonify, request
from datetime import datetime
from os import getenv

# environment variables for the flexibility of the hosting environment
HOST = getenv("host")
PORT = getenv("port")

app = Flask(__name__)


@app.route("/api", strict_slashes=False)
def index():
    """accept get request with query params"""
    date = datetime.now()
    base = 'https://github.com/Dev-wonderful/hng-backend-track'
    file = 'blob/main/stage-one/app.py'
    response = {
        'slack_name': request.args.get('slack_name'),
        'current_day': date.strftime('%A'),
        'track': request.args.get('track'),
        'utc_time': date.isoformat(),
        'github_file_url': base,
        'github_repo_url': f'{base}/{file}',
        'status_code': 200
    }

    return jsonify(response), 200
    

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
