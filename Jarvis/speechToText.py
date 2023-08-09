import speech_recognition as sr

recognizer = sr.Recognizer()

def record_audio():
    print("Recording...")
    
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
    return audio

def get_speech_input():
    while True:
        if input("Press Enter to start recording, or 'q' to quit: ") == "":
            audio = record_audio()
            
            try:
                # Recognize the speech using Google Web Speech API
                text = recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    speech_text = get_speech_input()
    print("Recognized text:", speech_text)
