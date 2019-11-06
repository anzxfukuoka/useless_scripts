set FILENAME=%1

ffmpeg -i %FILENAME% -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" video.mp4
ffmpeg -i video.mp4 -vf "boxblur=5:1" video_blur.mp4
ffmpeg -i video_blur.mp4 -vf scale=1920:1080 video_blur_scaled.mp4
ffmpeg -i video.mp4 -vf "movie=video_blur_scaled.mp4:loop=200,scale=iw/2:-1[bg];[bg][0]overlay=120:200:shortest=1" out.mp4