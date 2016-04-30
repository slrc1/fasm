import os

os.system("wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz")

os.system("tar xf ffmpeg-release-64bit-static.tar.xz")

os.system("mv ffmpeg-3.0.2-64bit-static/ffmpeg ffmpeg")

os.system("del ffmpeg-3.0.2-64bit-static/ffmpeg")
