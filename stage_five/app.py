from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, current_app, send_file, request, redirect, url_for
from config import App_Config
from models import Videos
from io import BytesIO
from __init__ import create_app, db
import base64
import os
import re


app = create_app()

parent_dir = 'videos'

@app.route('/api/video/upload', methods=['POST'])
def upload_video():
    """uplaod video test"""
    
    file = request.files.get('video')
    if not os.path.isdir(parent_dir):
        os.makedirs(parent_dir)
    # print(file.__dict__)
    with open(f"{os.path.abspath(parent_dir)}/{file.filename}", "wb") as new_file:
        new_file.write(file.read())
    url = f"{os.path.abspath(parent_dir)}/{file.filename}"
    new_video = Videos(name=file.filename, url=url)
    new_video.insert()

    return redirect(url_for("get_video", video_id=new_video.id))


@app.route('/api/video/<string:video_id>')
def get_video(video_id):
    """get a video"""
    # headers = request.headers
    video = db.session.execute(db.select(Videos).filter_by(id=video_id)).scalar_one_or_none()
    print(video.url)
    # with open("video.mp4", "wb") as file:
    #     file.write(base64.b64decode(video.url))

    # video_path = os.path.abspath("video.mp4")
    # size = os.stat(video_path)
    # size = size.st_size

    # chunk_size = (1024) * 3 #1000kb makes 1mb * 3 = 3mb (this is based on your choice)
    # if not "Range" in headers:
    #     start = 0
    # else:
    #     start = int(re.sub("\D", "", headers["Range"]))
    # end = min(start + chunk_size, size - 1)

    # content_length = end - start + 1

    # def get_chunk(video_path, start, chunk_size):
    #     with open(video_path, "rb") as f:
    #         f.seek(start)
    #         chunk = f.read(chunk_size)
    #     return chunk

    # headers = {
    #     "Content-Range": f"bytes {start}-{end}/{size}",
    #     "Accept-Ranges": "bytes",
    #     "Content-Length": content_length,
    #     "Content-Type": "video/mp4",
    # }

    # return current_app.response_class(get_chunk(video_path, start,chunk_size), 206, headers)
    return send_file(f"{os.path.abspath(parent_dir)}/{video.name}", download_name=video.name)


@app.route("/api/video/download/<string:video_id>", methods=["GET"])
def download(video_id):
    """check if download is possible"""
    # video_path = os.path.abspath("video_base.txt")
    video = db.session.execute(db.select(Videos).filter_by(id=video_id)).scalar_one_or_none()
    # with open(video_path, "rb") as file:
    #     binary_data = file.read()
    
    return send_file(BytesIO(base64.b64decode(video.data)),
                     download_name="video.mp4", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
