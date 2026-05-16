from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_resume():

    data = request.json
    resume = data.get("resume", "")
    resume_text = resume.lower()

    skills = []
    recommended_skills = []

    all_skills = {
        "python": "Python",
        "java": "Java",
        "react": "React",
        "mern": "MERN Stack",
        "full stack": "Full Stack Development",
        "frontend": "Frontend Development",
        "backend": "Backend Development",
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript",
        "machine learning": "Machine Learning",
        "bootstrap": "Bootstrap",
        "flask": "Flask"
    }

    for key, value in all_skills.items():

        if key in resume_text:
            skills.append(value)

    if "react" not in resume_text:
        recommended_skills.append("React")

    if "sql" not in resume_text:
        recommended_skills.append("SQL")

    if "backend" not in resume_text:
        recommended_skills.append("Backend Development")

    if "github" not in resume_text:
        recommended_skills.append("GitHub")

    score = min(len(skills) * 10, 100)

    ats_score = score - 5

    reward_points = score * 10

    if score >= 90:
        stars = "⭐⭐⭐⭐⭐"
        grade = "Excellent"

    elif score >= 70:
        stars = "⭐⭐⭐⭐"
        grade = "Good"

    elif score >= 50:
        stars = "⭐⭐⭐"
        grade = "Average"

    else:
        stars = "⭐⭐"
        grade = "Needs Improvement"

    career_roles = []

    if "react" in resume_text:
        career_roles.append("Frontend Developer")

    if "backend" in resume_text:
        career_roles.append("Backend Developer")

    if "python" in resume_text:
        career_roles.append("Python Developer")

    if "full stack" in resume_text:
        career_roles.append("Full Stack Developer")

    badges = []

    if "react" in resume_text:
        badges.append("🏅 React Explorer")

    if "python" in resume_text:
        badges.append("🏅 Python Developer")

    if "full stack" in resume_text:
        badges.append("🏅 Full Stack Learner")

    return jsonify({
        "skills": skills,
        "recommended_skills": recommended_skills,
        "score": score,
        "ats_score": ats_score,
        "reward_points": reward_points,
        "stars": stars,
        "grade": grade,
        "career_roles": career_roles,
        "badges": badges
    })

if __name__ == '__main__':
    app.run(debug=True)