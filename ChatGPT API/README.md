RobotTalkZone Concept 01 ReadMe
Date: 04.03.24
Author: Clara Osterburg Correa

Overview
Chatbot with to separate NLP modells:
first the ChatGBT Api Modell, where we are sending requests and getting answers. By doing this we encircle the topic until we talk about the movie “Alita”

### Key Components
## API Key Setup:

The OpenAI API key is required to run this code. Please replace the placeholder "###" with your actual OpenAI API key.
Type of Request:

The code initiates a conversation with a predefined system message, setting the user as a film critic with specific hobbies and interests. The goal is to guide the conversation toward the movie "Alita" after a few interactions.
ChatGPT Request Function:

The CustomChatGPT function handles user inputs, sends the entire conversation to the OpenAI GPT-3.5 Turbo model, and returns the model's reply. The conversation history is maintained in the messages variable.

## Gradio Interface:

The Gradio interface (RobotTalkZone) is set up to take user input as text and display the model's response in real-time. It provides an interactive platform for users to engage with the ChatGPT model.
How to Run
Ensure you have the required dependencies installed. You can install them using:

Copy code
pip install openai gradio
Replace the OpenAI API key placeholder in the code with your actual API key.

Run the code. The Gradio interface will launch, allowing you to interact with the ChatGPT model.

## run programm
Run the code. The Gradio interface will launch, allowing you to interact with the ChatGPT model.

python run ApiSolo.py

## Additional Information
The code utilizes the GPT-3.5 Turbo model from OpenAI for natural language understanding and generation.
The gradio library is used to create a user-friendly interface for interacting with the ChatGPT model.


##the feed forward implementation follows the instrucions of following video: https://github.com/patrickloeber/pytorch-chatbot -> the credits are going there

furthermore all the connection and additions are made by Clara Osterburg Correa