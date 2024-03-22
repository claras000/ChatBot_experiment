## 04.03.24 
## author: Clara Osterburg Correa
## RobotTalkZone Concept 02 | feed forward learning, topic finde & openAI connection in addition
## the code sends the hole conversation to openAI and a description of how to reply with the following topic

import random
import json
import requests
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import openai
import gradio

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load training Data
with open('pytorch-chatbot-master\\pytorch-chatbot-master\\topics.json', 'r') as json_data:
    topics = json.load(json_data)

# Load trained model
FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# ChatGPT connection
topic = "random topic"
bot_name = "Chatbot talking about Alita"
openai.api_key = "###"  # OpenAI API key please add here

messages = []

def chatbot(input_text):
    global topic, messages

    if input_text.lower() == "quit":
        messages = []  
        return "Conversation ended."

    system_msg = f"you are a film critic with a select range of hobbies and interests. You enjoy talking to people. Make small talk."
    messages.append({"role": "system", "content": system_msg})

   

   
    sentence = tokenize(input_text)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.5:
        for topic_data in topics['topics']:
            if tag == topic_data["tag"]:
                topic = random.choice(topic_data['followingTags'])

                user_input = input_text
                messages.append({"role": "user", "content": str(user_input)})  # Ensure user_input is a string
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": f"{system_msg} Lead the topic from the current topic to {topic}!"}, {"role": "user", "content": str(user_input)}]
                )
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})

                # Return ChatGPT's response
                return reply

    else:
       # Send order to ChatGPT API if no topic is chosen by feed forward modell
        topic = "chose topic random"

        user_input = input_text
        messages.append({"role": "user", "content": str(user_input)}) 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": f"{system_msg} Lead the topic from the current topic to {topic}!"}, {"role": "user", "content": str(user_input)}]
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        
        return reply

iface = gradio.Interface(fn=chatbot, inputs="text", outputs="text", title = "RobotTalkZone")
iface.launch()
