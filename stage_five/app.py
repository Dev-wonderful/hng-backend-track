from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, current_app, send_file, request, redirect, url_for
from config import App_Config
from models import Videos
import base64
import os
import re
from io import BytesIO


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(App_Config)
if app.config["SQLALCHEMY_DATABASE_URI"]:
    print(f"using db: {app.config['SQLALCHEMY_DATABASE_URI']}")

# Initialize CORS
CORS(app, supports_credentials=True)

# Initialize SQLAlchemy
db.init_app(app)

@app.route('/api/video/upload', methods=['POST'])
def upload_video():
    """uplaod video test"""
    file = request.files.get('video')
    # print(file.__dict__)
    text = base64.b64encode(file.read())
    new_video = Videos(name=file.filename, data=text)
    new_video.insert()
    with open("video.mp4", "wb") as video:
        video.write(base64.b64decode(text))

    return redirect(url_for("get_video"))


@app.route('/api/video')
def get_video():
    """get a video"""
    headers = request.headers

    video_path = os.path.abspath("video.mp4")
    size = os.stat(video_path)
    size = size.st_size

    chunk_size = (1024) * 3 #1000kb makes 1mb * 3 = 3mb (this is based on your choice)
    if not "Range" in headers:
        start = 0
    else:
        start = int(re.sub("\D", "", headers["Range"]))
    end = min(start + chunk_size, size - 1)

    content_length = end - start + 1

    def get_chunk(video_path, start, chunk_size):
        with open(video_path, "rb") as f:
            f.seek(start)
            chunk = f.read(chunk_size)
        return chunk

    headers = {
        "Content-Range": f"bytes {start}-{end}/{size}",
        "Accept-Ranges": "bytes",
        "Content-Length": content_length,
        "Content-Type": "video/mp4",
    }

    return current_app.response_class(get_chunk(video_path, start,chunk_size), 206, headers)


@app.route("/api/video/download", methods=["GET"])
def download():
    """check if download is possible"""
    video_path = os.path.abspath("video_base.txt")
    with open(video_path, "rb") as file:
        binary_data = file.read()
    
    return send_file(BytesIO(base64.b64decode(binary_data)),
                     download_name="video.mp4", as_attachment=True)


# create db tables from models if not exists
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
