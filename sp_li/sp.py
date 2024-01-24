'''here is the voices from pygame module'''
import os
import pygame

def speak(text):
    voice = "hi-IN-SwaraNeural" # "en-US-AnaNeural" #AI voice from icriss studio
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "audio_file/output.mp3"' #text to speech convertion
    os.system(command) #audio file creation
    # setting pygame for audio play back
    pygame.init() 
    pygame.mixer.init()
    pygame.mixer.music.load("audio_file/output.mp3") #loading the audio file
    try:
        # audio play
        pygame.mixer.music.play()
        # playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        # Stop the audio
        pygame.mixer.music.stop()
        pygame.mixer.quit()






'''here are the voices from a module pyttsx3'''
# import pyttsx3

# # Initialize the TTS engine
# engine = pyttsx3.init()
# # Get the list of available voices
# voices = engine.getProperty('voices')
# # Print available voices
# for voice in voices:
#     print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)
# # Set a specific voice by ID (change the ID to the desired voice)
# engine.setProperty('voice', voices[1].id)
# # Set the rate of speech (optional)
# engine.setProperty('rate', 150)
# # Convert text to speech
# def sp(text):
#     engine.say(text)
# # Wait for the speech to finish
#     engine.runAndWait()





'''Here is the code for voice from a website tts'''
# from time import sleep 
# from selenium import webdriver 
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import warnings 
# from selenium.webdriver.chrome.service import Service

# warnings.simplefilter("ignore")
# url = f'https://text-to-speech.online/'
# chrome_driver_path = 'chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_argument("--headless=new")  # Enable headless mode (runs Chrome without GUI)
# chrome_options.add_argument('--log-level=3')  # Set Chrome log level
# service = Service(chrome_driver_path)
# user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
# chrome_options.add_argument(f'user-agent={user_agent}')
# driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
# driver.get(url)
# sleep(3)

# def select_voice():
#     locale = driver.find_element(By.ID, 'locale').click()
#     sleep(0.7)
#     japnese_voice = driver.find_element(By.XPATH, '//*[@id="locale"]/option[66]').click() #hindi voice
#     sleep(0.7)
#     voice = driver.find_element(By.ID, 'voice').click()
#     sleep(0.7)
#     female_voice = driver.find_element(By.XPATH, '//*[@id="voice"]/option[2]').click()


# def sp(text):
#     driver.execute_script("document.querySelector('.cookiealert').style.display='none';")
#     textarea = driver.find_element(By.ID, 'text')
#     textarea.clear()
#     textarea.send_keys(text)
#     sleep(2)
#     playBtn = driver.find_element(By.ID,'quick-play')
#     playBtn.click()
#     sleep(10)
    
    
# # select_voice()



# while 1:
#     text=input(">> ")
#     speak(text)