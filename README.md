# 🤖 Multi-Agent System using OpenAI Agents SDK & Gemini

This project demonstrates a basic multi-agent architecture using the OpenAI Agents SDK with Google's Gemini model. A triage agent decides which expert agent (Web Developer, Math Tutor, Science Tutor, or English Tutor) should handle the user's query.

## 📦 Features

- ✅ Integrated with OpenAI Agents SDK
- 🔁 Handoff between agents based on query type
- 🤖 Uses Gemini (via OpenAI-compatible client) as LLM
- 👨‍🏫 Specialized agents for math, science, web development, and English
- 🧠 Central triage agent for task delegation

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone <repo-url>
cd <project-folder>



### 2. Install Dependencies
pip install -r requirements.txt

###  3. Add Environment Variables

GEMINI_API_KEY=your_gemini_api_key

4. Run the App
uv run chainlit run chatbot.py


🧠 How It Works
Triage Agent takes the user query and decides which expert agent should handle it.

Supported agents:

Web Developer

Math Tutor

Science Tutor

English Tutor

Each agent responds based on its domain expertise.


🧪 Example Query

Input: What is the output of 12 + 10?
→ Triage Agent → Math Tutor → Response