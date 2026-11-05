


import streamlit as st
import difflib
import random
from detector import detect_pattern
from evaluator import evaluate_code
from recommender import recommend_pattern
from plagiarism import check_plagiarism
from ai_engine import analyze_code
# from comparison import compare_models
# from detector import detect_pattern

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="GenAI Code Intelligence Platform",
    page_icon="🧠",
    layout="wide"
)

# -------------------------
# GLOBAL UI STYLE
# -------------------------
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #0f172a, #4f46e5, #06b6d4);
    padding: 60px;
    border-radius: 28px;
    color: white;
    text-align: center;
    box-shadow: 0px 18px 45px rgba(0,0,0,0.25);
}

/* CARD */
.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
}

/* TILE */
.tile {
    padding: 22px;
    border-radius: 18px;
    color: white;
    font-weight: 700;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.18);
}

.blue { background: linear-gradient(135deg,#6366f1,#3b82f6); }
.green { background: linear-gradient(135deg,#10b981,#06b6d4); }
.orange { background: linear-gradient(135deg,#f59e0b,#ef4444); }
.purple { background: linear-gradient(135deg,#8b5cf6,#ec4899); }
.dark { background: linear-gradient(135deg,#111827,#374151); }

/* SIDEBAR TEXT BIGGER */
section[data-testid="stSidebar"] * {
    font-size: 17px !important;
    font-weight: 500;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg,#4f46e5,#06b6d4);
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------
st.markdown("""
<div class="hero">
<h1>🧠 GenAI Code Intelligence Platform</h1>
<p>AI-powered system for Code Understanding • Evaluation • Recommendation • Assistance</p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR (KEEP SAME CONTENT STYLE)
# -------------------------
menu = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "📄 Pattern Detection",
        "📊 Code Evaluation",
        "🎯 Pattern Recommendation",
        "🔍 Plagiarism Check",
        "⚡ Coding Assistant",
        # "📈 Model Comparison"
    ]
)
st.sidebar.markdown("---")
st.sidebar.caption("🚀 Smart AI Research Prototype v2.0")

# =========================================================
# 🏠 CREATIVE DASHBOARD (FULLY REDESIGNED)
# =========================================================
if menu == "🏠 Home":

    st.markdown("## ✨ Intelligent Code Understanding Platform")

    st.markdown("""
    <div class="card">
    This AI system analyzes student-written code, detects design patterns, evaluates quality,
    checks similarity, and provides intelligent feedback using hybrid AI reasoning.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # FEATURE GRID
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown('<div class="tile blue">🧠 Code Understanding Engine</div>', unsafe_allow_html=True)
        st.caption("Analyzes structure, logic, OOP behavior")

    with c2:
        st.markdown('<div class="tile green">📊 Code Evaluation System</div>', unsafe_allow_html=True)
        st.caption("Scores correctness + quality")

    with c3:
        st.markdown('<div class="tile orange">🔍 Plagiarism Detection</div>', unsafe_allow_html=True)
        st.caption("Detects similarity & duplication")

    st.write("")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown('<div class="tile purple">🎯 Pattern Recommendation</div>', unsafe_allow_html=True)
        st.caption("Suggests best design patterns")

    with c5:
        st.markdown('<div class="tile dark">⚡ Coding Assistant</div>', unsafe_allow_html=True)
        st.caption("Real-time coding support")

    with c6:
        st.markdown('<div class="tile blue">📈 Confidence AI Engine</div>', unsafe_allow_html=True)
        st.caption("Explains AI decisions clearly")

    st.write("")

    # WORKFLOW
    st.markdown("## 🔄 How System Works")

    st.markdown("""
    <div class="card">

    1️⃣ Input Student Code  
    ↓  
    2️⃣ AI analyzes structure & logic  
    ↓  
    3️⃣ Pattern detection + evaluation  
    ↓  
    4️⃣ Confidence score generation  
    ↓  
    5️⃣ Recommendation + feedback  

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # IMPACT METRICS
    st.markdown("## 🎯 System Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Automation Level", "High")

    with col2:
        st.metric("AI Mode", "Hybrid (Rules + AI Logic)")

    with col3:
        st.metric("Learning Support", "Real-Time")

# =========================================================
# 📄 PATTERN DETECTION
# =========================================================
# elif menu == "📄 Pattern Detection":

#     st.markdown("## 🧠 Pattern Detection Engine")

#     code = st.text_area("Paste Code", height=200)

#     if st.button("Analyze Pattern"):

#         code_l = code.lower()

#         pattern = "Unknown"

#         if "singleton" in code_l:
#             pattern = "Singleton Pattern"
#         elif "factory" in code_l:
#             pattern = "Factory Pattern"
#         elif "observer" in code_l:
#             pattern = "Observer Pattern"
#         elif "strategy" in code_l:
#             pattern = "Strategy Pattern"

#         confidence = random.randint(75, 96)

#         st.success(f"Detected Pattern: {pattern}")
#         st.metric("Confidence Score", f"{confidence}%")
# =========================================================
# 📄 PATTERN DETECTION
# =========================================================
# elif menu == "📄 Pattern Detection":

#     st.markdown("## 🧠 Pattern Detection Engine")

#     code = st.text_area(
#         "Paste Java Code",
#         height=300
#     )

#     if st.button("Analyze Pattern"):

#         pattern, confidence, reason = detect_pattern(code)

#         st.success(
#             f"Detected Pattern: {pattern}"
#         )

#         st.metric(
#             "Confidence Score",
#             f"{confidence}%"
#         )

#         st.info(reason)
elif menu == "📄 Pattern Detection":

    st.markdown("## 🧠 AI Pattern Detection Engine")

    code = st.text_area(
        "Paste Java Code",
        height=300
    )

    if st.button("Analyze Pattern"):

        result = detect_pattern(code)

        st.markdown("### 🎯 Detection Result")

        st.success("Pattern Detected Successfully")

        st.code(result)

# elif menu == "📄 Pattern Detection":

#     st.markdown("## 🧠 Pattern Detection Engine")

#     code = st.text_area(
#         "Paste Java Code",
#         height=300
#     )

#     if st.button("Analyze Pattern"):

#         pattern, confidence, reason = detect_pattern(code)

#         st.success(
#             f"Detected Pattern: {pattern}"
#         )

#         st.metric(
#             "Confidence Score",
#             f"{confidence}%"
#         )

#         st.info(reason)
# # =========================================================
# 📊 CODE EVALUATION
# =========================================================
# elif menu == "📊 Code Evaluation":

#     st.markdown("## 📊 Code Quality Engine")

#     code = st.text_area("Paste Code", height=200)

#     if st.button("Evaluate"):

#         score = 0

#         if "class" in code:
#             score += 25
#         if "for" in code or "while" in code:
#             score += 20
#         if "if" in code:
#             score += 20
#         if "return" in code:
#             score += 20
#         if len(code.split()) > 30:
#             score += 15

#         confidence = random.randint(80, 97)

#         st.metric("Score", f"{score}/100")
#         st.metric("Confidence", f"{confidence}%")

# =========================================================
# 📊 CODE EVALUATION
# =========================================================
# elif menu == "📊 Code Evaluation":

#     st.markdown("## 📊 Code Quality Engine")

#     code = st.text_area(
#         "Paste Java Code",
#         height=300
#     )

#     if st.button("Evaluate Code"):

#         score, feedback = evaluate_code(code)

#         st.metric(
#             "Quality Score",
#             f"{score}/100"
#         )

#         st.subheader("Feedback")

#         for item in feedback:
#             st.info(item)


elif menu == "📊 Code Evaluation":

    st.markdown("## 📊 AI Code Evaluation Engine")

    code = st.text_area(
        "Paste Java Code",
        height=300
    )

    if st.button("Evaluate Code"):

        result = evaluate_code(code)

        st.markdown("### 📈 Evaluation Result")

        st.success("Evaluation Complete")

        st.code(result)

# =========================================================
# 🎯 PATTERN RECOMMENDATION
# =========================================================
# elif menu == "🎯 Pattern Recommendation":

#     st.markdown("## 🎯 Recommendation Engine")

#     code = st.text_area("Paste Code", height=200)

#     if st.button("Generate"):

#         rec = []

#         if "object" in code.lower():
#             rec.append("Factory Pattern")
#         if "single" in code.lower():
#             rec.append("Singleton Pattern")
#         if "behavior" in code.lower():
#             rec.append("Strategy Pattern")

#         if not rec:
#             rec.append("Use Modular OOP Design")

#         for r in rec:
#             st.info(r)

# elif menu == "🎯 Pattern Recommendation":

#     st.markdown("## 🎯 Pattern Recommendation Engine")

#     code = st.text_area(
#         "Paste Java Code",
#         height=300
#     )

#     if st.button("Generate Recommendation"):

#         recommendations = recommend_pattern(code)

#         st.subheader("Suggested Patterns")

#         for rec in recommendations:
#             st.success(rec)

# elif menu == "🔍 Plagiarism Check":

#     st.markdown("## 🔍 Similarity & Plagiarism Detection")

#     f1 = st.file_uploader(
#         "Upload Student Code",
#         type=["java", "py"]
#     )

#     f2 = st.file_uploader(
#         "Upload Reference Code",
#         type=["java", "py"]
#     )

#     if st.button("Check Similarity"):

#         if f1 and f2:

#             code1 = f1.read().decode(errors="ignore")
#             code2 = f2.read().decode(errors="ignore")

#             similarity = check_plagiarism(
#                 code1,
#                 code2
#             )

#             st.metric(
#                 "Similarity Score",
#                 f"{similarity:.2f}%"
#             )

#             if similarity >= 80:

#                 st.error(
#                     "🔴 High Risk Plagiarism Detected"
#                 )

#             elif similarity >= 50:

#                 st.warning(
#                     "🟠 Moderate Similarity Found"
#                 )

#             else:

#                 st.success(
#                     "🟢 Original Code"
#                 )

#         else:

#             st.warning(
#                 "Please upload both files."
#             )
elif menu == "🎯 Pattern Recommendation":

    st.markdown("## 🎯 AI Pattern Recommendation Engine")

    code = st.text_area(
        "Paste Java Code",
        height=300
    )

    if st.button("Generate Recommendation"):

        result = recommend_pattern(code)

        st.markdown("### 🎯 Recommendation Result")

        st.success("Recommendation Generated")

        st.code(result)
# # =========================================================
# # 🔍 PLAGIARISM CHECK
# # =========================================================
# elif menu == "🔍 Plagiarism Check":

#     f1 = st.file_uploader("Upload Student Code", type=["java", "py"])
#     f2 = st.file_uploader("Upload Reference Code", type=["java", "py"])

#     if st.button("Check Similarity"):

#         if f1 and f2:

#             c1 = f1.read().decode(errors="ignore")
#             c2 = f2.read().decode(errors="ignore")

#             similarity = difflib.SequenceMatcher(None, c1, c2).ratio() * 100

#             st.metric("Similarity", f"{similarity:.2f}%")

#             if similarity > 70:
#                 st.error("High Similarity ⚠")
#             else:
#                 st.success("Original Code ✔")

# =========================================================
# 🔍 PLAGIARISM CHECK
# =========================================================
elif menu == "🔍 Plagiarism Check":

    st.markdown("## 🔍 Similarity & Plagiarism Detection")

    f1 = st.file_uploader(
        "Upload Student Code",
        type=["java", "py"]
    )

    f2 = st.file_uploader(
        "Upload Reference Code",
        type=["java", "py"]
    )

    if st.button("Check Similarity"):

        if f1 and f2:

            code1 = f1.read().decode(
                errors="ignore"
            )

            code2 = f2.read().decode(
                errors="ignore"
            )

            similarity = (
                difflib.SequenceMatcher(
                    None,
                    code1.lower(),
                    code2.lower()
                ).ratio()
                * 100
            )

            st.metric(
                "Similarity Score",
                f"{similarity:.2f}%"
            )

            # Risk Analysis

            if similarity >= 80:

                st.error(
                    "🔴 High Risk Plagiarism Detected"
                )

                st.info(
                    "Large portions of code appear identical."
                )

            elif similarity >= 50:

                st.warning(
                    "🟠 Moderate Similarity Found"
                )

                st.info(
                    "Some code fragments are similar."
                )

            else:

                st.success(
                    "🟢 Original Code"
                )

                st.info(
                    "Low similarity detected."
                )

        else:

            st.warning(
                "Please upload both files."
            )
# =========================================================
# ⚡ CODING ASSISTANT
# =========================================================
# elif menu == "⚡ Coding Assistant":

#     q = st.text_area("Ask Coding Question")

#     if st.button("Get Answer"):

#         q = q.lower()

#         if "array" in q:
#             st.info("Use loops and indexing for arrays")

#         elif "sort" in q:
#             st.info("Use QuickSort or MergeSort")

#         elif "pattern" in q:
#             st.info("Use design patterns for scalable systems")

#         elif "oop" in q:
#             st.info("Encapsulation, Inheritance, Polymorphism, Abstraction")

#         else:
#             st.info("Break problem into modules and solve step-by-step")

elif menu == "⚡ Coding Assistant":

    st.markdown(
        "## ⚡ AI Coding Assistant"
    )

    code = st.text_area(
        "Paste Your Code",
        height=300
    )

    if st.button(
        "Analyze Code"
    ):

        result = analyze_code(
            code
        )

        st.write(result)




# # -------------------------
# # Model Comparision
# # -------------------------
# elif menu == "📈 Model Comparison":

#     st.title("📈 GenAI Model Comparison")

#     code = st.text_area(
#         "Paste Java Code",
#         height=300,
#         key="compare_code"
#     )

#     if st.button("Compare Models"):

#         pattern, confidence, reason = detect_pattern(code)

#         import pandas as pd

#         df = pd.DataFrame({
#             "Model": ["GPT-4", "Claude", "Gemini"],
#             "Pattern": [pattern, pattern, pattern],
#             "Confidence": [
#                 max(confidence - 5, 80),
#                 max(confidence - 7, 78),
#                 confidence
#             ]
#         })

#         st.dataframe(df)

#         st.bar_chart(
#             df.set_index("Model")["Confidence"]
#         )

#         st.success(
#             f"Gemini achieved highest confidence ({confidence}%)"
#         )

#         st.info(reason)
# -------------------------
# FOOTER
# -------------------------
st.markdown("""
<div style="text-align:center; margin-top:20px; color:gray;">
🧠 GenAI Code Intelligence Platform • Professional AI Research System
</div>
""", unsafe_allow_html=True)


