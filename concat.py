import subprocess

video = '20180510094301-3595_360'
#scales the video for concating. Different scale ratio videos can not be concatenated
subprocess.call('ffmpeg -i /var/www/html/GetVideo/video/%s.mp4 -c:v libx264 -c:a copy -vf scale=1920:1080,setdar=16/9 /var/www/html/GetVideo/video/output2.mp4' % video, shell=True)
subprocess.call('ffmpeg -i /var/www/html/GetVideo/video/{0}.mp4 -i /var/www/html/GetVideo/video/{1}.mp4 -filter_complex "[0:v:0] [0:a:0] [1:v:0] [1:a:0] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" /var/www/html/GetVideo/video/{2}.mp4'.format('outputreklam','output2','reklamli2'), shell=True)
