import yt_dlp
import os

def download_video(url):
    output = "downloads/%(title)s.%(ext)s"

    ydl_opts = {
        "outtmpl": output,
        "format": "best"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    return os.path.abspath(filename)
