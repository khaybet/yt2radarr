import yt_dlp
import os

def download_video(url):
    download_dir = "/app/downloads"
    os.makedirs(download_dir, exist_ok=True)

    output = f"{download_dir}/%(title)s.%(ext)s"

    ydl_opts = {
        "outtmpl": output,
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return os.path.abspath(filename)
