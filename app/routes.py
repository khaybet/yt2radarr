from flask import Blueprint, render_template, request
from youtube import download_video
from radarr import send_to_radarr

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        path = download_video(url)
        result = send_to_radarr(path)
        return render_template("index.html", result=result)

    return render_template("index.html")
