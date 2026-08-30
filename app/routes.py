from flask import Blueprint, render_template, request, jsonify
from youtube import download_video
from radarr import send_to_radarr

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.get_json()
        url = data.get("url")

        path = download_video(url)
        result = send_to_radarr(path)

        return jsonify({"status": "ok", "result": result})

    return render_template("index.html")
