### testing version for testing feed forward model

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
openai.api_key = ""  # OpenAI API key please add here

messages = []

print("Let's chat! (type 'quit' to exit)")
input_counter = 0


while True:
    sentence = input("You: ")
    
    if sentence.lower() == "quit":
        messages = []  
        break

    system_msg = f"you are a film critic with a select range of hobbies and interests. You enjoy talking to people. Make small talk."
    messages.append({"role": "system", "content": system_msg})
    
    input_counter += 1  

    if input_counter == 15:
        topic = "Alita"  # Change the topic to Alita after 15 inputs

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for topic_data in topics['topics']:
            if tag == topic_data["tag"]:
                topic = random.choice(topic_data['followingTags'])
                print(topic)

        

                user_input = sentence
                messages.append({"role": "user", "content": str(user_input)}) 
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": f"{system_msg} Lead the topic form current topic to {topic}!"}, {"role": "user", "content": str(user_input)}]
                )
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                print("\n" + reply + "\n")

                

    else:
        # Send order to ChatGPT API if no topic is chosen by feed forward modell
        topic = "chose topic random"
        print(topic)

        user_input = sentence
        messages.append({"role": "user", "content": str(user_input)})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": f"{system_msg} Lead the topic form current topic to {topic}!"}, {"role": "user", "content": str(user_input)}]
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")

       