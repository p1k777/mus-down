import argparse
from yt_dlp import YoutubeDL
from mutagen.id3 import ID3, TIT2, TPE1

def set_metainfo(path: str, title: str, arists: list[str]):
    tags = ID3(path)

    tags.delall("TIT2")
    tags.delall("TPE1")

    tags.add(TIT2(
        encoding=3,
        text=[title],
    ))

    tags.add(TPE1(
        encoding=3,
        text=', '.join(arists),
    ))

    tags.save(path, v2_version=4)

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

        title = info["title"]
        artists = info["creators"]
        path = info["requested_downloads"][0]["filepath"]

        set_metainfo(path, title, artists)

        print(f'"{title}" {artists} -> {path}')



def main():
    parser = argparse.ArgumentParser("Загрузка треков")

    parser.add_argument(
        "-u",
        "--url",
        help="URL трека для загрузки (пока только Youtube Music)",
        default=""
    )

    parser.add_argument(
        "--input",
        help="Путь к файлу с перечисленными URL (по одному в строке)",
        default=""
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Папка для сохранения заргуженных композиций",
        default="downloads"
    )

    args = parser.parse_args()

    YDL_OPTS = args.output

    if (args.url):
        pass
    elif args.input:
        pass
    else:
        while True:
            work()


main()
