import json
import os
import random
import getpass



user = getpass.getuser()

imquestions = os.path.dirname(__file__)
#ścieżka do zapisu odpowiedzi
user = os.path.join(imquestions, user)
folder_to_check = imquestions  
#folder z pytaniami
files_to_check = os.listdir(folder_to_check)
rightquestions = 0
donequestions = 0

#Pobranie ustawień dla testów
config = os.path.join(os.path.dirname(__file__), "config.JSON")

with open (config, "r", encoding="utf-8") as config:
    data = json.load(config)
amofquest = data["config"]["amountofquestions"]
needtopass = data["config"]["needtopass"]

ignored_files = ["AI.py","config.JSON"]


while  donequestions != amofquest: 
    for file in files_to_check:
            
        file = os.path.join(imquestions, file)
        if os.path.basename(file) in ignored_files:
            continue

        with open (file, "r", encoding='utf-8') as JsonFile:
            ques = json.load(JsonFile)
            rng = random.randint(0, len(ques["questions"])-1)
            questouse = ques["questions"][rng]
            question = questouse["question"]
            useranswer = input (f"{question}\nOdpowiedz: ")
            answer = questouse["answer"]
            useranswer = useranswer.strip().lower()
            answer = answer.strip().lower()

            if useranswer == answer:
                rightquestions += 1
                donequestions += 1
                print("Dobrze")
            else:
                donequestions += 1
                print("Zle")


wynik = (rightquestions / amofquest) * 100

percent = (rightquestions / amofquest) * 100
passed = "Tak" if percent >= needtopass else "Nie"
with open(f"{user}.txt", "w", encoding="utf-8-sig") as f:
    f.write(f"{user} otrzymal {wynik}%. Zdal? {passed}")
