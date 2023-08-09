import speech_recognition as sr
import keyboard
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

def record_audio():
    print("Recording...")
    
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
    
    return audio

def main():
    print("Hold down Space to start recording, release to stop.")
    recording = False
    
    while True:
        if keyboard.is_pressed("space"):
            if not recording:
                recording = True
                print("Recording started.")
            
            audio = record_audio()
            
            try:
                # Recognize the speech using Google Web Speech API
                text = recognizer.recognize_google(audio)
                print("You said:", text)
            except sr.UnknownValueError:
                print("Speech recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API; {0}".format(e))
        
        else:
            if recording:
                recording = False
                print("Recording stopped.")
                time.sleep(0.02)  # To avoid recognizing multiple presses
        
        if keyboard.is_pressed("esc"):  # Press Esc key to exit the program
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
