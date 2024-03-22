###Introduction

Understanding Language with Computers

name: “RobotTalkZone”
Domain: conversation logs / a conversation chatbot

Task: Conversation Agent

###We implemented two Version 
-one simple only with chatgbt: Folder ChatGBT API
-one with chatGBT API and a feedforward model before to analyse the topic: Folder pytorch-chatbot-master


###summary
Our goal is to approach the topic of creating a chatbot that leads a conversation on a set
topic. In the first step, we want to analyze what constitutes a conversation. In the second
part, we want to implement one of these features, such as asking questions back or referring
to related issues.

###Intro
Normally chatbots do task-oriented chats or do so called chit-chat conversations.
We want to combine these two skills and build a chatbot that can lead a small talk chat and move on from topic to topic until he always ends with the same topic. This transformation should be gentle and inconspicuous. In addition we want some influence on the model with parameters that we implement. The currently famous NLP from openAI also has the skill to fulfill the task, but as a coder you have not much influence. We have opted for a model that consists of two parts. One in which we can exert influence, a feed-forward model and the openAI API. This combination allows us to influence our results differently. 

Our idea is to approach the topic of creating a chatbot that leads a conversation on a set topic. In the first step, we want to analyze what constitutes a conversation. In the second part, we want to implement one of these features, such as asking questions back or referring to related issues. 
As a resume we make a transition from shitchat to task oriented Dialogue.

Dialogue systems are typically classified into two main types: open-domain and task-oriented. Open-domain systems aim to engage users in casual conversations, where selecting appropriate topics is crucial for a successful interaction. On the other hand, task-oriented systems focus on specific tasks such as finding a movie or playing a song. These two directions have traditionally been studied separately due to their distinct purposes. However, transitioning smoothly from social chatting to task-oriented dialogues is crucial for capitalizing on business opportunities, yet there is a lack of publicly available data focusing on such transitions. 
Therefore, this paper delves into exploring conversations starting from open-domain social chatting and gradually transitioning to task-oriented purposes. To facilitate this research direction, we introduce a large-scale dataset with detailed annotations. Our framework proposes automatic dialogue generation without human involvement, leveraging powerful open-domain dialogue generation models. Human evaluation indicates that our generated dialogues exhibit a natural flow and reasonable quality, showcasing potential for guiding future research and commercial activities. 2022.acl-long.425.pdf (acl anthology.org)
