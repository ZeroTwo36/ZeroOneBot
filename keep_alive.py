from flask import Flask
from threading import Thread
import random
import json

app = Flask('')

api_data = {
  "conversation_starter":{
    "topic":[
      "What is something you are obsessed with?",
      "If you had intro music, what song would it be? Why?",
      "What is something that is popular now that annoys you?",
      "Who is your favorite entertainer (comedian, musician, actor, etc.)?",
      "What’s your favorite way to waste time?",
      "Do you have any pets? What are their names?",
      "How much wood could a woodchuck chuck if a woodchuck could chuck wood? :)",
      "What do you do to get rid of stress?",
      "Where did you go last weekend? What did you do?",
      "What’s the best / worst thing about your work / school?"
    ]
  }
}

@app.route("/")
def index():
  return "Bot is online"

@app.route("/api/conversation")
def convo():
  data = {"topic":random.choice(api_data["conversation_starter"]["topic"])}

  return json.dumps(data)

def run():
  app.run("0.0.0.0",port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()
