# MusDown

An incredibly lightweight CLI utility for downloading music from the Internet. So far, only Youtube music is supported, there is a chance that SoundCloud support will appear later (Spotify is not planned)

## Requirements

- `argparse`
- `yt-dlp`
- `mutagen`

They are installed using `pip`:
```
pip install [lib]
```

## Usage

The program is not pre-compiled, there is only the source code, but the use is not difficult (you can use the standard python interpreter)

```
python main.py [-h] [-u URL] [--input INPUT] [-o OUTPUT]
```
**Options:**
- `-h`, `--help` – display 'help' information
- `-u`, `--url` – set *only one* track URL (Youtube Music)
- `--input` – set file path that must contain URLs (1 line = 1 url)
- `-o, --output` – set downloads folder

**Important:** `--url` and `--input` are mutually exclusive (if both are specified, a branch with `--url` will be executed), if no argument is specified, interactive mode will be launched (each URL is entered separately), to exit the intercative mode, enter `QUIT` or `Q` in an arbitrary case in the URL field.

## Examples

### Only one URL
```
python main.py -u 'https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8'
```
or
```
python main.py --url 'https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8'
```

### List of URLs
```
python main.py --input downloads/urls.txt
```
`urls.txt`:
```
https://music.youtube.com/watch?v=oxv5WWJ0oAo&si=2TJkSPZGvG5l9Gx8
https://music.youtube.com/watch?v=oqFRIjWo2I4&si=7Hq4uG_36QtVhU5z
https://music.youtube.com/watch?v=DmOaxyilm4g&si=HwZd-8O-fcPu08al
```

### Interactive mode
```
python main.py
```
then just insert URL into field URL!
