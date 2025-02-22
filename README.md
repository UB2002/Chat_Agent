# Titanic Dataset Chat Agent

## 🚀 Mission
Build a friendly chatbot that can analyze the famous Titanic dataset. Users should be able to ask questions in plain English and get both text answers and visual insights about the passengers.

## Tech Stack
- **Backend**: Python with FastAPI
- **Agent Framework**: LangChain
- **Frontend**: Streamlit

## Features
1. Accepts questions in natural language.
2. Provides clear text responses.
3. Generates helpful visualizations.
4. Displays everything in a clean Streamlit interface.


## 🛠 Setup Instructions
### 1️ Clone the Repository
```sh
git clone https://github.com/your-repo/titanic-chatbot.git
cd titanic-chatbot
```
### 2 Configure Environment
Create backend/.env:
```sh
GEMINI_API_KEY=your_gemini_api_key_here
```
Replace your_gemini_api_key_here with your actual Gemini API key.

### 3 Install Dependencies
```sh
pip install -r requirements.txt
```

### 4 Run the Backend (FastAPI)
```sh
fastapi dev api.py
```

### 5 Run the Frontend (Streamlit)
```sh
streamlit run frontend.py
```

## 🤔 Example Questions you can ask the model 
- "What percentage of passengers were male on the Titanic?"
- "Show me a histogram of passenger ages."
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"

## Output 
![Chatbot Output](https://github.com/UB2002/Chat_Agent/blob/main/output.png)
