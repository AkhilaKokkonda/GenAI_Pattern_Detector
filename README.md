# 🚀 GenAI Pattern Detector
### Generative AI for Automated Design Pattern Evaluation

An AI-powered Code Intelligence Platform that helps students analyze source code, identify software design patterns, evaluate code quality, and receive intelligent recommendations using Generative AI.

---

## 📌 Overview

**GenAI Pattern Detector** is a Python-based application designed to automate the evaluation of design patterns in student-written code.

The platform combines rule-based analysis, dataset-based pattern detection, and Google's Gemini Generative AI to provide meaningful code insights, quality assessments, similarity analysis, and improvement suggestions.

It aims to make software design pattern learning and code evaluation easier, smarter, and more accessible.

## ✨ Key Features

- **Design Pattern Detection:** Identifies commonly used software design patterns in source code.
- **Code Quality Evaluation:** Evaluates code quality using structural and complexity-related characteristics.
- **Pattern Recommendations:** Suggests suitable design patterns to improve code organization and maintainability.
- **Code Similarity Analysis:** Analyzes similarities between code submissions and provides similarity percentages.
- **AI-Powered Code Analysis:** Uses Google Gemini to generate explanations, insights, and improvement suggestions.
- **Intelligent Coding Assistant:** Provides AI-based guidance to help students understand and improve their code.
- **Interactive Dashboard:** Displays analysis results and feedback through a user-friendly Streamlit interface.

## 🧩 Design Patterns Supported

The platform focuses on detecting and evaluating the following five design patterns:

| Design Pattern | Category |
|---|---|
| Singleton | Creational |
| Factory | Creational |
| Observer | Behavioral |
| Strategy | Behavioral |
| Visitor | Behavioral |

## ⚙️ How It Works

The application follows a structured code analysis workflow:

1. **Code Input:** Users provide their source code for analysis.
2. **Preprocessing:** The submitted code is cleaned and prepared for analysis.
3. **Code Analysis:** The system processes code structures, classes, methods, inheritance, and object creation.
4. **Pattern Detection:** Rule-based and dataset-based techniques identify potential design patterns.
5. **Quality Evaluation:** The system evaluates code characteristics and generates quality feedback.
6. **Pattern Recommendation:** Relevant design pattern recommendations are generated.
7. **Similarity Analysis:** Code similarity is analyzed and presented as a percentage.
8. **Generative AI Analysis:** Google Gemini provides explanations, insights, and improvement suggestions.
9. **Results Dashboard:** Analysis results are presented through the Streamlit interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Google Gemini API | Generative AI-powered code analysis |
| Rule-Based Analysis | Design pattern identification |
| Dataset-Based Analysis | Supporting pattern detection |
| Code Processing | Source code preprocessing and analysis |

## 📂 Project Structure

```text
GenAI-Pattern-Detector/
│
├── dataset/
│   ├── Factory/
│   │   ├── App.java
│   │   ├── Coin.java
│   │   ├── CoinFactory.java
│   │   ├── CoinType.java
│   │   ├── CopperCoin.java
│   │   └── GoldCoin.java
│   │
│   ├── Observer/
│   ├── Singleton/
│   ├── Strategy/
│   └── Visitor/
│
├── templates/
│
├── ai_engine.py
├── app.py
├── comparison.py
├── detector.py
├── evaluator.py
├── plagiarism.py
├── recommender.py
├── test_gemini.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/GenAI-Pattern-Detector.git
```

### 2. Navigate to the Project Directory

```bash
cd GenAI-Pattern-Detector
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API

Obtain a Google Gemini API key and configure it using the environment variable expected by `ai_engine.py`.

Keep your API key private. Never upload API credentials to GitHub.

### 7. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🤖 Role of Generative AI

Google Gemini is integrated to enhance the code analysis experience by providing:

- Natural-language explanations of detected design patterns.
- Intelligent code improvement suggestions.
- Contextual feedback for student-written code.
- AI-assisted coding guidance.

The project uses a hybrid approach, combining traditional rule-based and dataset-based analysis with Generative AI assistance.

## 🎯 Project Objectives

- Automate software design pattern evaluation.
- Help students understand software design principles.
- Improve code quality and maintainability.
- Provide intelligent and actionable feedback.
- Explore practical applications of Generative AI in software engineering education.

## 🔮 Future Enhancements

- Support for additional design patterns.
- Expanded programming language support.
- More advanced code similarity detection.
- Improved evaluation accuracy.
- Detailed code analysis reports.
- Enhanced AI-powered learning assistance.

## 👩‍💻 Author

**Kokkonda Akhila**

B.Tech Computer Science and Engineering

Interested in Software Development, Artificial Intelligence, and Generative AI.

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Streamlit, and Google Gemini AI.**
