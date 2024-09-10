import speech_recognition as sr 
import pyttsx3
import webbrowser
from hugchat import hugchat

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured.."

def chatBot(query):
    user_input=query.lower()
    chatbot=hugchat.ChatBot(cookie_path="cookies.json")
    id=chatbot.new_conversation()
    chatbot.change_conversation(id)
    response=chatbot.chat(user_input)
    print(response)
    say(response)
    return response

if __name__ == "__main__":
    say('I am A.I, nice to meet you')
    while True:
        print("Listning...")
        query = takeCommand()
        sites=[["youtube","https://youtube.com"], ["chat gpt","https://chatgpt.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Openning {site[0]}...")
                webbrowser.open(site[1])
            
        chatBot(query)
            
        #say(query)
