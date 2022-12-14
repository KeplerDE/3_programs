# Извлечение аудио дорожки из видео-файла
import moviepy.editor


video = moviepy.editor.VideoFileClip('my_video.mkv')
audio = video.audio
audio.write_audiofile('my_audio.mp3')







