import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
faq_path = BASE_DIR / "faq.json"


with open(faq_path, "r") as f:
    faq = json.load(f)


question_count = 0


while True:
    question = input("\nAsk a question (or type quit): ").lower().strip()


    if question == "quit":
        print("Question asked:", question_count)
        print("Goodbye!")
        break
   
    question_count += 1
   
    found_answer = False


    for item in faq.values():
        if question in item["keywords"]:
            print(item["answer"])
            found_answer = True
            break


    if not found_answer:
        print("Sorry, I dont know the answer")