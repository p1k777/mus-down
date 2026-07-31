import argparse
from yt_dlp.utils import DownloadError

import utils


DOWNLOADERS: list[utils.BaseSource] = [
    utils.YoutubeSource(),
    utils.SoundcloudSource(),
    utils.VkSource()
]


def finish(code: int = 0):
    print("[FINISHED]")
    exit(code)


def download(url: str = ""):
    if not url:
        url = input("URL: ")

        if url.lower() == "q" or url.lower() == "quit":
            finish()

    print(f'Got "{url}"')

    try:
        for downloader in DOWNLOADERS:
            if (downloader.supports(url)):
                res = downloader.download(url)
                utils.set_metainfo(res)
                print("[DOWNLOAD COMPLETE]:", res.title, "->", res.path)
                return
        print("URL is not supported yet :(")
    except DownloadError as e:
        print("Can not download this track due to error, try another service or try again later")
    except Exception as e:
            print(f'Error occured: "{str(e)}"')



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--url",
        help="track URL (Youtube Music, SoundCloud, VK)",
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

    utils.YDL_OPTS["outtmpl"] = f'{args.output}/%(title)s.%(ext)s'

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
