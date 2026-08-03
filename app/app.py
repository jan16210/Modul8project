from flask import Flask, render_template, request, redirect, url_for, session
from quiz_logic import levels, calculate_score

app = Flask(__name__)

# Needed to store scores/progress
app.secret_key = "climatequiz"

level_names = [
    "Beginner",
    "Intermediate",
    "Difficult",
    "Final"
]
@app.route("/language/<lang>")
def change_language(lang):
    session["language"] = lang
    return redirect(request.referrer or "/")

@app.route("/")
def home():
    return render_template("html.html")

@app.route("/quiz")
def quiz():

    session["level"] = 0
    session["total_score"] = 0

    return redirect(url_for("question_page"))


@app.route("/question")
def question_page():

    current_level = level_names[session["level"]]

    questions = levels[current_level]["questions"]

    return render_template(
        "quiz.html",
        level=current_level,
        questions=questions
    )


@app.route("/submit", methods=["POST"])
def submit():

    current_level = level_names[session["level"]]

    questions = levels[current_level]["questions"]

    answers = []

    for i in range(len(questions)):
        answers.append(
            request.form.get(f"question{i}", ""))


    score = calculate_score(
        answers,
        current_level)
    session["total_score"] += score
    
    session["level"] += 1

   
    if session["level"] >= len(level_names):

        return render_template(
            "result.html",
            score=session["total_score"],
            total=9
        )

    return redirect(url_for("question_page"))

if __name__ == "__main__":
    app.run(debug=True)