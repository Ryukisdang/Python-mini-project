class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What does the 'def' keyword in Python stand for?\n(a) Define\n(b) Default\n(c) Deflate\n(d) Defrag\n\n",
    "In Java, which method must be present in every main class?\n(a) init\n(b) start\n(c) main\n(d) run\n\n",
    "What does HTML stand for?\n(a) Hyper Trainer Marking Language\n(b) Hyper Text Marketing Language\n(c) Hyper Text Markup Language\n(d) Hyper Transfer Protocol Language\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct!")

run_quiz(questions)
