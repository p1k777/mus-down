from yt_dlp import YoutubeDL

YDL_OPTS = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

def work():
    url = input("url: ")

    if url.lower() == "q":
        print("[FINISHED]")
        exit(0)

    print(f'Got "{url}"')

    with YoutubeDL(YDL_OPTS) as ydl:
        info = ydl.extract_info(url, download=True)
        print("[AVAILABLE KEYS]", info.keys())
        print(
            f'"{info["title"]}" {info["creators"]} -> {info["requested_downloads"][0]["filepath"]}'
        )



while True:
    work()
    