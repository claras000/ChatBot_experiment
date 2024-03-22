## 04.03.24 
## author: Clara Osterburg Correa
## RobotTalkZone Concept 02 | simple API directly linked to openAI with specified request
## the code sends the hole conversation to openAI and a description of how to reply

import openai
import gradio

openai.api_key = "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"

## type of request
messages = [{"role": "system", "content": "you are a film critic with a select range of hobbies and interests. You enjoy talking to people. Make small talk. carefully lead the topic to the movie alita after a few interactions."}]

## chatgbt request
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages ##all messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply}) ##adding new message for sending all the conversation 
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "RobotTalkZone")

demo.launch(share=True) ##launch on gradio