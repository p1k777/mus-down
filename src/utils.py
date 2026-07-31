from dataclasses import dataclass
from typing import Protocol

from mutagen.id3 import ID3, TIT2, TPE1
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


@dataclass
class DownloadResult:
    title: str
    artists: list[str]
    path: str


def set_metainfo(result: DownloadResult):
    title = result.title
    artists = result.artists
    path = result.path


    tags = ID3(path)

    tags.delall("TIT2")
    tags.delall("TPE1")

    tags.add(TIT2(
        encoding=3,
        text=[title],
    ))

    tags.add(TPE1(
        encoding=3,
        text=', '.join(artists),
    ))

    tags.save(path, v2_version=4)




class BaseSource(Protocol):
    def supports(self, url: str) -> bool: return False
    def download(self, url: str) -> DownloadResult: pass


class YoutubeSource:
    def supports(self, url: str) -> bool:
        return ("music.youtube.com" in url)

    def download(self, url: str) -> DownloadResult:
        with YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(url, download=True)
            return DownloadResult(
                title=info["title"],
                artists=info["creators"],
                path=info["requested_downloads"][0]["filepath"]
            )


class SoundcloudSource:
    def supports(self, url: str) -> bool:
        return ("soundcloud.com" in url)

    def download(self, url: str) -> DownloadResult:
        with YoutubeDL(YDL_OPTS) as ydl:
            info = ydl.extract_info(url, download=True)
            return DownloadResult(
                title=info["title"],
                artists=info["artists"],
                path=info["requested_downloads"][0]["filepath"]
            )