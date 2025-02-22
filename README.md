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

### 2️ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️ Run the Backend (FastAPI)
```sh
uvicorn backend.main:app --reload
```

### 4️ Run the Frontend (Streamlit)
```sh
streamlit run frontend/app.py
```

## 🤔 Example Questions you can ask the model 
- "What percentage of passengers were male on the Titanic?"
- "Show me a histogram of passenger ages."
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"

## Output 
![Chatbot Output](https://github.com/UB2002/Chat_Agent/blob/main/output.png)
