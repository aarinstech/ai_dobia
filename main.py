bot_name="Dobia"
dev_name="aarinstech"

from en_to_hi.en_to_hi import *
from ldr.ldr import *
from sp_li.li import *
from sp_li.sp import *
from yr_info.yr_info import *
from yr_info.yr_info_write import *
import os
import g4f
import random

'''clear'''
def clr():
    os.system('cls')


messages = [{"role": "system", "content": f"You are {bot_name} and developed by {dev_name}"}]
def GPT(*args):

    global messages
    assert args != ()

    message = ''
    for i in args:
        message += i

    messages.append({'role': 'user', "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)

    messages.append({'role': 'assistant', "content": ms})
    return ms


'''First_Time Info'''
# yr_info_write()
my_name, my_age, my_sex = yr_info()
loading_spinner('Initializing',2)
clr()
clr()

while True:
    query=li()
    # query=input(f"{my_name}: ")
    print(f"{my_name}: "+query)
    query=translate_to_english(query)
    query=query.lower()
    
    if '-' == query:
        break
    else:
        if 'your name' in query or 'coded you' in query or 'build you' in query or 'your developer' in query or 'made you' in query or 'developed you' in query:

            me_res_dev=(f"Hi, I am {bot_name}, developed by {dev_name}. How can I assist you today",f"Hey, I am {bot_name} developed by {dev_name}")
            me_res_dev=me_res_dev[random.randint(0,1)]
            me_res_dev=translate_to_hindi(me_res_dev)
            speak(me_res_dev)

        elif 'hello' in query or 'hi' in query or 'Hey' in query or 'sole' in query:

            me_res_hi=("Hello, How are you?", f"Hello, I am {bot_name}", f"Hi, How {bot_name} can help you?")
            me_res_hi1=me_res_hi[random.randint(0,2)]
            me_res_hi1=translate_to_hindi(me_res_hi1)
            speak(me_res_hi1)

        elif 'colour of sky' in query:
            response=("The colour of sky is Blue", "Sky colour is Blue but I think you know it.","It is Blue", "It is neither red nor yellow it is Blue","I think it is Blue")
            response=response[random.randint(0,4)]
            response=translate_to_hindi(response)
            speak(response)

        else:

            response=GPT(query)
            response=translate_to_hindi(response)
            speak(response)




# def find_code(text):
#     pattern = r'```python(.*?)```'
#     matches = re.findall(pattern, text, re.DOTALL)
#     if matches:
#         code = matches[0].strip()
#         return code
#     else:
#         print('no code found')

