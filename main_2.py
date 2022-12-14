# Извлечение аудио дорожки из видео-файла
import moviepy.editor
from pathlib import Path

# video = moviepy.editor.VideoFileClip('my_video.mkv')
video = moviepy.editor.VideoFileClip(f'{my_video}')
audio = video.audio
# audio.write_audiofile('my_audio.mp3')
audio.write_audiofile(f'{my_audio.stem}.mp3')     # .stem отбросили расширение







