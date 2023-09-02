from moviepy.editor import VideoFileClip
import sys

videoId = sys.argv[1]
videoPath = sys.argv[2]
exportVideoPath = sys.argv[3]
videoFileClip = VideoFileClip(f"{videoPath}/{videoId}.mp4")

for i, arg in enumerate(sys.argv[4:]):
    interval = list(map(float, arg.split('-')))
    targetPath = f"{exportVideoPath}/{videoId}_({interval[0]}-{interval[1]})_{i+1}.mp4"
    videoFileClip.subclip(interval[0], interval[1]).write_videofile(targetPath, fps=24)

videoFileClip.reader.close()