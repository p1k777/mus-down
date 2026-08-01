# MusDown

An incredibly lightweight CLI utility for downloading music from the Internet. So far, only Youtube Music, SoundCloud and VK music are supported[^1] (Spotify is not planned)

## Requirements

### Python libs

- `yt-dlp`
- `mutagen`

Installed via `pip`:
```
python -m pip install mutagen yt-dlp
```
If VK source support required use
```
python -m pip install mutagen "yt-dlp @ git+https://github.com/DarkCat09/yt-dlp.git@vkmusic"
```

### Other

- `ffmpeg`:

Ubuntu:
```
sudo apt install ffmpeg
```
Windows:
```
winget install --id Gyan.FFmpeg
```
Mac:
```
brew install ffmpeg
```

- `git` is also required to install the VK-compatible yt-dlp fork

## Usage

The program is not pre-compiled, there is only the source code, but the use is not difficult (you can use the standard python interpreter)

```
python src/main.py [-h] [-u URL] [--input INPUT] [-o OUTPUT]
```
**Options:**
- `-h`, `--help` – display 'help' information
- `-u`, `--url` – set *only one* track URL (Youtube Music, SoundCloud, VK)
- `--input` – set file path that must contain URLs (1 line = 1 url)
- `-o, --output` – set downloads folder

**Important:** If both --url and --input are specified, --url takes precedence, if neither are specified, interactive mode will be launched (each URL is entered separately), to exit the intercative mode, enter `QUIT` or `Q` in an arbitrary case in the URL field.

## Examples

### Only one URL
```
python src/main.py -u 'https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8'
```
or
```
python src/main.py --url 'https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8'
```

### List of URLs
```
python src/main.py --input downloads/urls.txt
```
`urls.txt`:
```
https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8
https://music.youtube.com/watch?v=oqFRIjWo2I4&si=7Hq4uG_36QtVhU5z
https://music.youtube.com/watch?v=DmOaxyilm4g&si=HwZd-8O-fcPu08al
```

### Interactive mode
```
python src/main.py
```
then just insert URL into field URL!

[^1]: VK support requires an unofficial yt-dlp fork and may be unstable.
