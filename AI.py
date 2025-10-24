import json
import os
import random
import string

imquestions = os.path.dirname(__file__)
folder_to_check = imquestions  
files_to_check = os.listdir(folder_to_check)
rightquestions = 0
xquestions = imquestions


for file in files_to_check:
    file = os.path.join(imquestions, file)
    if "AI.py" in file:
        continue
    rng = random.randint(0,1)
    with open (file, "r", encoding='utf-8') as JsonFile:
        ques = json.load(JsonFile)
        questouse = ques["questions"][rng]
        print (questouse["question"])
        answer = questouse["answer"]
        
    
    useranswer = input (questouse["question"])
    useranswer.lower()
    if useranswer == answer:
        xofquestions =+1


