import sys
import os

YOUTUBE_DL = "youtube-dl"
MUSIC_DIR = "~/storage/downloads/DRIVE/"
VIDEO_DIR = "~/storage/downloads/"
FILENAME = "%(title)s.%(ext)s"
DOWNLOADED_FILE = "downloaded.txt"

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def print_eggog():
    print("ёггог")
    sys.exit(-1337)

def is_youtube(url):
    if url.find("youtu") > -1 or url.find("youtube") > -1:
        return True
    return False

def is_playlist(url):
    if (url.find("/playlist?list=") > -1) or (url.find("/watch") > -1 and url.find("list=") > -1):
        return True
    return False

if len(sys.argv) == 2:

    URL = sys.argv[1]

    if not is_youtube(URL):
        os.system(YOUTUBE_DL + " -o " + "\"" + VIDEO_DIR + "\" " + URL)

    print("Download video?(Y/n)")
    getch = _Getch()
    answer = getch()

    print(answer)

    if answer == 'y' or answer == 'Y' or answer == '\r':
        print("Downloading video...")
        KEYS = " --no-mtime -o "
    elif answer == b'n' or answer == b'N':
        print("Downloading mp3 file...")
        KEYS = " --no-mtime --extract-audio --audio-format mp3 --audio-quality 0 -f 'bestaudio' -o "
    else:
        print_eggog()

    if is_playlist(URL):
        os.system(YOUTUBE_DL + " --yes-playlist" + " --download-archive \"" + MUSIC_DIR + "%(playlist_title)s/" + DOWNLOADED_FILE + "\"" + KEYS + "\"" + MUSIC_DIR + "%(playlist_title)s/" + FILENAME + "\"" +  " -f \"best\" " + "\"" + URL + "\"")
    else:
        os.system(YOUTUBE_DL + "--download-archive \"" + MUSIC_DIR + DOWNLOADED_FILE + "\"" + KEYS + "\"" +  MUSIC_DIR + FILENAME + "\"" + " -f \"best\" " + URL)
else:
    print_eggog()
