from moviepy.editor import VideoFileClip

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)
    audio.close()
    video.close()

# Example usage
extract_audio("/Users/abc/Desktop/sbh codes/videoreume.mov", "output_audio1.wav")
import speech_recognition as sr

def recognize_speech(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

# Example usage
recognized_text = recognize_speech("output_audio1.wav")
print("Recognized Speech:", recognized_text)
print("aaaa")