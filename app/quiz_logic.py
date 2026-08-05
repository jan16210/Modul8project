

website_url = "https://www.un.org/en/climatechange/paris-agreement"
difficult_questions_url = "https://www.epa.gov/ghgemissions/overview-greenhouse-gases"

levels = {
    "Beginner": {
        "lives": 3,
        "questions": [
            {
                "question": "What country is the Paris Climate Agreement held in?",
                "answers": ["france", "francja"]
            },
            {
                "question": "What is the cap for the temperature increase set by the Paris Climate Agreement?",
                "answers": [
                    "2c",
                    "2°c",
                    "2 degrees",
                    "two degrees",
                    "two degrees warmer"
                ]
            },
            {
                "question": "What is the target year for countries to achieve net-zero emissions?",
                "answers": ["2050"]
            }
        ]
    },

    "Intermediate": {
        "lives": 2,
        "questions": [
            {
                "question": "Which greenhouse gas is the largest contributor to human-caused climate change?",
                "answers": [
                    "carbon dioxide",
                    "co2"
                ]
            },
            {
                "question": "What type of energy creates greenhouse gases? (Hint: it cannot be remade)",
                "answers": [
                    "fossil fuels",
                    "fossil fuel"
                ]
            }
        ]
    },


    "Difficult": {
        "lives": 2,
        "questions": [
            {
                "question": "What greenhouse gas is released in large amounts by livestock such as cattle?",
                "answers": [
                    "methane",
                    "ch4"
                ]
            },
            {
                "question": "What atmospheric layer contains the ozone that protects Earth from harmful ultraviolet radiation?",
                "answers": [
                    "stratosphere"
                ]
            }
        ]
    },


    "Final": {
        "lives": 2,
        "questions": [
            {
                "question": "What year did the Paris Agreement enter into force?",
                "answers": [
                    "2016"
                ]
            },
            {
                "question": "What is the name of the national climate plans that countries submit under the Paris Agreement?",
                "answers": [
                    "nationally determined contributions",
                    "ndcs",
                    "ndc"
                ]
            }
        ]
    }
}


def check_answer(question, answer):
    answer = answer.lower().strip()
    return answer in question["answers"]

def calculate_score(submitted_answers, level):
    score = 0
    questions = levels[level]["questions"]
    for i in range(len(questions)):

        if check_answer(
            questions[i],
            submitted_answers[i]):
            score += 1
    return score