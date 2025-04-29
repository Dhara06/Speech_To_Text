import speech_recognition as sr
filename = "C:/Users/dhara/Desktop/GitHubDemo/STT/sttdemo.wav"
r = sr.Recognizer()
def transcribe_from_audiofile(path):
    try:
        with sr.AudioFile(path) as source:
            audio = r.record(source)
            text = r.recognize_google(audio)
            print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except FileNotFoundError:
        print("Audio file not found. Check the path.")
            
transcribe_from_audiofile(filename)