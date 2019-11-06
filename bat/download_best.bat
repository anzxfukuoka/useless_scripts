@ECHO OFF


chcp 1251

set ffmpeg="D:\ffmpeg.exe"

set /p url=:_

youtube-dl -f 137+bestaudio/136+bestaudio/278+bestaudio/244+bestaudio/ --merge-output-format mkv --ffmpeg-location %ffmpeg% -o %%(title)s.%%(ext)s %url%

REM %ffmpeg% -i %title%.mkv %title%.mp4

pause
