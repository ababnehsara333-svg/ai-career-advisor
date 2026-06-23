import streamlit as st

st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.hero {
    padding: 45px;
    border-radius: 24px;
    background: linear-gradient(135deg, #111827, #312E81, #4F46E5);
    color: white;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}
.hero p {
    font-size: 18px;
    color: #E5E7EB;
}
.badge {
    display: inline-block;
    padding: 8px 14px;
    background-color: rgba(255,255,255,0.15);
    border-radius: 999px;
    font-size: 14px;
    margin-bottom: 18px;
}
.result-card {
    padding: 28px;
    border-radius: 22px;
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    color: white;
    text-align: center;
    margin-top: 20px;
}
.small-card {
    padding: 20px;
    border-radius: 18px;
    background-color: #F8FAFC;
    border: 1px solid #E5E7EB;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="badge">Personalized Career Intelligence</div>
    <h1>Find Your Best Tech Career Path</h1>
    <p>
        Select your current skills and get a personalized career match,
        missing skills analysis, and a focused learning roadmap.
    </p>
</div>
""", unsafe_allow_html=True)

career_paths = {
    "Data Analyst": {
        "skills": ["Excel", "SQL", "Power BI", "Statistics", "Data Visualization", "Communication"],
        "roadmap": ["Advanced Excel", "SQL Projects", "Power BI Dashboards", "Business Analysis"]
    },
    "Machine Learning Engineer": {
        "skills": ["Python", "Machine Learning", "Statistics", "Deep Learning", "SQL"],
        "roadmap": ["Scikit-learn", "Model Deployment", "Deep Learning", "MLOps Basics"]
    },
    "Data Scientist": {
        "skills": ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization"],
        "roadmap": ["EDA Projects", "Feature Engineering", "ML Models", "Storytelling with Data"]
    },
    "BI Developer": {
        "skills": ["SQL", "Power BI", "Excel", "Data Visualization", "Communication"],
        "roadmap": ["Power BI Advanced", "DAX", "SQL Reporting", "Dashboard Design"]
    },
    "AI Product Designer": {
        "skills": ["UI/UX", "Figma", "Communication", "AI Concepts", "Data Visualization"],
        "roadmap": ["Figma Projects", "AI UX Patterns", "Product Thinking", "Case Studies"]
    }
}

all_skills = [
    "Python", "SQL", "Excel", "Power BI", "Machine Learning",
    "Deep Learning", "Statistics", "Tableau", "Communication",
    "Data Visualization", "UI/UX", "Figma", "AI Concepts"
]

st.subheader("Choose the skills you already have")

selected_skills = st.multiselect(
    "Your current skills",
    all_skills
)

if st.button("✨ Generate My Career Path", use_container_width=True):
    if len(selected_skills) == 0:
        st.warning("Please select at least one skill.")
    else:
        results = []

        for career, data in career_paths.items():
            required_skills = data["skills"]
            matched_skills = list(set(selected_skills) & set(required_skills))
            missing_skills = list(set(required_skills) - set(selected_skills))
            match_score = len(matched_skills) / len(required_skills) * 100

            results.append({
                "career": career,
                "score": match_score,
                "matched": matched_skills,
                "missing": missing_skills,
                "roadmap": data["roadmap"]
            })

        results = sorted(results, key=lambda x: x["score"], reverse=True)
        best_match = results[0]

        st.markdown(f"""
        <div class="result-card">
            <h2>Your Best Career Match</h2>
            <h1>{best_match["career"]}</h1>
            <h3>{best_match["score"]:.0f}% Match</h3>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ✅ Matched Skills")
            if best_match["matched"]:
                for skill in best_match["matched"]:
                    st.success(skill)
            else:
                st.info("No matched skills yet.")

        with col2:
            st.markdown("### ⚠️ Missing Skills")
            if best_match["missing"]:
                for skill in best_match["missing"]:
                    st.warning(skill)
            else:
                st.success("You have all the required skills!")

        st.markdown("### 📚 Focused Learning Roadmap")

        for i, step in enumerate(best_match["roadmap"], start=1):
            st.markdown(f"""
            <div class="small-card">
                <strong>Step {i}:</strong> {step}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📊 Other Career Matches")

        for result in results[1:]:
            st.write(f"**{result['career']}** — {result['score']:.0f}% match")