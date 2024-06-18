from gtts import gTTS
import playsound

text = "Hello, how are you?"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
playsound.playsound("output.mp3")
