import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {

  const [resume, setResume] = useState("");
  const [result, setResult] = useState(null);

  const analyzeResume = async () => {

    try {

      const response = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ resume })
      });

      const data = await response.json();

      setResult(data);

    }

    catch(error){

      console.log(error);
      alert("Backend Connection Failed");

    }

  };

  return (

    <div className="main-container">

      <div className="glass-card">

        <h1 className="title">
          SkillSync AI
        </h1>

        <p className="subtitle">
          AI Career Intelligence Platform
        </p>

        <textarea
          className="form-control mb-3"
          rows="8"
          placeholder="Paste Resume Content"
          onChange={(e) => setResume(e.target.value)}
        />

        <button
          className="btn btn-primary analyze-btn"
          onClick={analyzeResume}
        >
          Analyze Resume
        </button>

        {

          result && (

            <div className="result-box mt-4">

              <h2>
                Resume Score: {result.score}/100
              </h2>

              <h3>
                {result.stars}
              </h3>

              <h4>
                {result.grade}
              </h4>

              <p>
                ATS Compatibility: {result.ats_score}%
              </p>

              <p>
                Reward Points: {result.reward_points} XP
              </p>

              <h4>
                Detected Skills
              </h4>

              <ul>

                {

                  result.skills.map((skill, index) => (

                    <li key={index}>
                      {skill}
                    </li>

                  ))

                }

              </ul>

              <h4>
                Recommended Skills
              </h4>

              <ul>

                {

                  result.recommended_skills.map((skill, index) => (

                    <li key={index}>
                      {skill}
                    </li>

                  ))

                }

              </ul>

              <h4>
                Career Roles
              </h4>

              <ul>

                {

                  result.career_roles.map((role, index) => (

                    <li key={index}>
                      {role}
                    </li>

                  ))

                }

              </ul>

              <h4>
                Achievement Badges
              </h4>

              <div>

                {

                  result.badges.map((badge, index) => (

                    <span
                      key={index}
                      className="badge-box"
                    >
                      {badge}
                    </span>

                  ))

                }

              </div>

            </div>

          )

        }

      </div>

    </div>

  );
}

export default App;