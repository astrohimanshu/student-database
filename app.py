from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

CSV_FILE = "students.csv"

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    roll = request.form["roll"]
    name = request.form["name"]
    email = request.form["email"]
    gender = request.form["gender"]
    course = request.form["course"]
    experience = request.form["experience"]

    # Checkbox (multiple values)
    skills = request.form.getlist("skills")
    skills_str = ", ".join(skills)

    # Multiple select dropdown
    languages = request.form.getlist("languages")
    languages_str = ", ".join(languages)

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            roll, name, email, gender,
            skills_str, course,
            languages_str, experience
        ])

    return redirect("/students")

@app.route("/students")
def students():
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    return render_template("display.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)
