chcp 1251
set /p url=url_:
echo %url%
youtube-dl -o %%(title)s.%%(ext)s %url%"
pause
