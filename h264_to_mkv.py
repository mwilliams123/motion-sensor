import os
import subprocess
video_dir = 'videos/'
out_dir = 'processed/'
videos = os.listdir(video_dir)
for i in range(len(videos)):
    f = video_dir + videos[i]
    out_file = out_dir + 'video' + str(i) + '.mkv'
    subprocess.run(['ffmpeg', '-y', '-r', '30', '-i', f, out_file])