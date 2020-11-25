import pyttsx3

engine = pyttsx3.init()
# engine.say("轻轻地，我走了，正如我轻轻地来......")
# with open('text.txt', 'r', encoding='utf8') as f:
#     engine.say(f.read())
# engine.save_to_file('轻轻地，我走了，正如我轻轻地来......', 'Poetry.mp3')
# voices = engine.getProperty('voices')
# for voice in voices:
    # engine.setProperty('voice', voice.id)
    # engine.say('The quick brown fox jumped over the lazy dog.')

# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate + 50)
# engine.say('The quick brown fox jumped over the lazy dog.')

# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume-0.25)
# engine.say('The quick brown fox jumped over the lazy dog.')

# 标准的粤语发音
voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
# 普通话发音
# voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.ting-ting.premium")
# 台湾甜美女生普通话发音
# voices = engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")

# engine.runAndWait()
