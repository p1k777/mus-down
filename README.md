# MusDown

A lightweight CLI utility for downloading music from:

* YouTube Music
* SoundCloud
* VK Music

> [!IMPORTANT]
> VK Music support is provided by an unofficial `yt-dlp` fork that is based on an older version of `yt-dlp`.
>
> Because installing the VK fork replaces the regular `yt-dlp` package, the project should be used with **two separate Python virtual environments**:
>
> * `.venv` — YouTube Music and SoundCloud
> * `.venv-vk` — VK Music

This keeps the regular `yt-dlp` installation up to date without breaking VK support.

## Requirements

* Python
* `ffmpeg`
* `mutagen`
* `yt-dlp`

## Installing FFmpeg

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

Using `winget`:

```powershell
winget install --id Gyan.FFmpeg
```

Restart the terminal after installation.

### macOS

Using Homebrew:

```bash
brew install ffmpeg
```

Verify the installation:

```bash
ffmpeg -version
```

## Clone the repository

```bash
git clone https://github.com/p1k777/mus-down.git
cd mus-down
git switch dev
```

## Python environments

MusDown uses two virtual environments because regular `yt-dlp` and the VK-compatible fork cannot be installed together in the same environment.

### Environment 1: YouTube Music and SoundCloud

Create the environment:

```bash
python -m venv .venv
```

Activate it.

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install --upgrade mutagen yt-dlp
```

Check the installed version:

```bash
python -m yt_dlp --version
```

Use this environment for:

* YouTube Music
* SoundCloud

### Environment 2: VK Music

Create a separate environment:

```bash
python -m venv .venv-vk
```

Activate it.

#### Linux/macOS

```bash
source .venv-vk/bin/activate
```

#### Windows PowerShell

```powershell
.venv-vk\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv-vk\Scripts\activate.bat
```

Install `mutagen` and the VK-compatible `yt-dlp` fork:

```bash
python -m pip install --upgrade pip
python -m pip install mutagen "yt-dlp @ git+https://github.com/DarkCat09/yt-dlp.git@vkmusic"
```

Use this environment only for VK Music URLs.

> [!WARNING]
> The VK fork contains an older version of the YouTube extractor. YouTube Music may fail in this environment with errors such as:
>
> ```text
> Signature extraction failed
> Only images are available for download
> ```
>
> For YouTube Music and SoundCloud, switch back to `.venv`.

## Switching between environments

Deactivate the currently active environment:

```bash
deactivate
```

Activate the regular environment for YouTube Music and SoundCloud:

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Activate the VK environment for VK Music:

### Linux/macOS

```bash
source .venv-vk/bin/activate
```

### Windows PowerShell

```powershell
.venv-vk\Scripts\Activate.ps1
```

## Usage

```bash
python src/main.py [-h] [-u URL] [--input INPUT] [-o OUTPUT]
```

### Options

* `-h`, `--help` — show help
* `-u`, `--url` — download one track by URL
* `--input` — read URLs from a file, one URL per line
* `-o`, `--output` — set the download directory

The default output directory is:

```text
downloads
```

When neither `--url` nor `--input` is specified, MusDown starts in interactive mode.

Enter `Q` or `QUIT` to exit interactive mode.

## Examples

### YouTube Music

Activate the regular environment:

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Run MusDown:

```bash
python src/main.py \
    -o downloads \
    -u 'https://music.youtube.com/watch?v=oxv5WWJ0oAo'
```

### SoundCloud

Use the same regular environment:

```bash
python src/main.py \
    -o downloads \
    -u 'https://soundcloud.com/artist/track'
```

### VK Music

Deactivate the regular environment:

```bash
deactivate
```

Activate the VK environment:

#### Linux/macOS

```bash
source .venv-vk/bin/activate
```

#### Windows PowerShell

```powershell
.venv-vk\Scripts\Activate.ps1
```

Run MusDown:

```bash
python src/main.py \
    -o downloads \
    -u 'VK_TRACK_URL'
```

## Downloading URLs from a file

Create a file such as `urls.txt`:

```text
https://music.youtube.com/watch?v=oxv5WWJ0oAo
https://music.youtube.com/watch?v=oqFRIjWo2I4
https://music.youtube.com/watch?v=DmOaxyilm4g
```

Activate the environment appropriate for those URLs and run:

```bash
python src/main.py --input urls.txt -o downloads
```

> [!IMPORTANT]
> Do not mix VK URLs with YouTube Music or SoundCloud URLs in the same input file.
>
> A single MusDown process uses the `yt-dlp` installation from only one active virtual environment. Use separate input files and separate runs:
>
> * regular URLs with `.venv`
> * VK URLs with `.venv-vk`

## Interactive mode

Activate the required environment and run:

```bash
python src/main.py
```

Then enter one URL at a time:

```text
URL: https://music.youtube.com/watch?v=oxv5WWJ0oAo
```

To exit:

```text
URL: Q
```

## Updating dependencies

### Update regular yt-dlp

Activate `.venv` and run:

```bash
python -m pip install --upgrade yt-dlp mutagen
```

### Update the VK fork

Activate `.venv-vk` and reinstall the fork:

```bash
python -m pip install --upgrade --force-reinstall \
    "yt-dlp @ git+https://github.com/DarkCat09/yt-dlp.git@vkmusic"
```

Updating the VK fork does not necessarily update it to the latest upstream `yt-dlp` version. It only installs the latest state of the fork's `vkmusic` branch.

## Troubleshooting

### Only images are available for download

Example:

```text
WARNING: Only images are available for download
```

First, check which environment is active:

```bash
python -c "import sys; print(sys.executable)"
```

Then check the installed `yt-dlp` version:

```bash
python -m yt_dlp --version
```

For YouTube Music, make sure `.venv` is active and update `yt-dlp`:

```bash
python -m pip install --upgrade yt-dlp
```

### The wrong yt-dlp installation is used

Check the package location:

```bash
python -c "import yt_dlp; print(yt_dlp.__file__)"
```

The path should contain either:

```text
mus-down/.venv/
```

or:

```text
mus-down/.venv-vk/
```

depending on the selected source.

### FFmpeg is not found

Check that FFmpeg is available:

```bash
ffmpeg -version
```

If the command is not found, install FFmpeg and restart the terminal.

## Environment summary

| Source        | Environment | yt-dlp package                       |
| ------------- | ----------- | ------------------------------------ |
| YouTube Music | `.venv`     | Current official `yt-dlp`            |
| SoundCloud    | `.venv`     | Current official `yt-dlp`            |
| VK Music      | `.venv-vk`  | `DarkCat09/yt-dlp`, branch `vkmusic` |

## Disclaimer

MusDown uses third-party services and unofficial download tools. Service behavior may change at any time.

Users are responsible for complying with applicable laws and the terms of service of the platforms they use.
