@echo off

echo %~1

REM --video-zoom 0.4 ^

wp run mpv ^
--player-operation-mode=pseudo-gui ^
--force-window=yes ^
--terminal=no ^
--no-audio ^
--loop=inf ^
--loop-playlist=inf ^
--input-ipc-server=\\.\pipe\mpvsocket ^
%~1

wp mv --wait --class mpv -x 1920
wp add --wait --fullscreen --class mpv
