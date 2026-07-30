import argparse
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from mutagen.id3 import ID3, TIT2, TPE1




def finish(code: int = 0):
    print("[FINISHED]")
    exit(code)


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

def download(url: str = ""):
    if not url:
        url = input("URL: ")

        if url.lower() == "q" or url.lower() == "quit":
            finish()

    print(f'Got "{url}"')

    try:
        with YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(url, download=True)
            keys = info.keys()

            title = "NO NAME"
            if ("title" in keys): title = info["title"]
            elif ("name" in keys): title = info["name"]

            artists = ["NO ARTISTS"]
            if ("creators" in keys): artists = info["creators"]
            elif ("artists" in keys): artists = info["artists"]

            path = info["requested_downloads"][0]["filepath"]

            set_metainfo(path, title, artists)

            print(f'"{title}" {artists} -> {path}')
            print("="*200)
    except DownloadError as e:
        print("Can not download this track due to error, try another service or try again later")
    except Exception as e:
            print(f'Error occured: "{str(e)}"')



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        help="track URL (Youtube Music, SoundCloud)",
        default=""
    )

    parser.add_argument(
        "--input",
        help="URLs file path (1 line = 1 url)",
        default=""
    )

    parser.add_argument(
        "-o",
        "--output",
        help="downloads folder",
        default="downloads"
    )

    args = parser.parse_args()

    YDL_OPTS["outtmpl"] = f'{args.output}/%(title)s.%(ext)s'

    try:
        if (args.url):
            print(args.url)
            download(args.url)
            finish()
        elif args.input:
            lines = []
            with open(args.input) as file:
                lines = file.readlines()

            for url in lines:
                url = url.strip()
                download(url)

            finish()
        else:
            while True:
                download()
    except Exception as e:
        print(f'Error occured: "{str(e)}"')


main()
