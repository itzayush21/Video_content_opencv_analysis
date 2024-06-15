import speech_recognition as sr
def analyze_speech_clarity(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as audio_file:
        audio_data = recognizer.record(audio_file)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Speech recognized:", text)
        except sr.UnknownValueError:
            print("Speech could not be recognized.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
analyze_speech_clarity("/Users/abc/Desktop/code/output_audio.wav")