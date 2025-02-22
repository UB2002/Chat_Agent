import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.base import LLM
from typing import Optional, List, Any
import re
import os
from dotenv import load_dotenv
import io

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

df = sns.load_dataset('titanic')

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")
genai.configure(api_key=api_key)

class GeminiLLM(LLM):
    model_name: str = "gemini-pro"
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt)
        return response.text
    @property
    def _llm_type(self) -> str:
        return "gemini"

llm = GeminiLLM()

prompt = PromptTemplate(
    input_variables=["question", "data_summary"],
    template="""
    You are a data analyst chatbot for the Titanic dataset. The dataset summary is:
    {data_summary}

    Answer the user's question: {question}
    - Provide a concise text answer in natural language (e.g., "The histogram shows the distribution of passenger ages.").
    - If a visualization is requested, end your response with exactly this format: "Visualization: [type] of [column]" (e.g., "Visualization: histogram of age").
    - Do NOT include Python code, tool calls, or programming instructions under any circumstances. I will handle visualizations locally.
    """
)

data_summary = f"Columns: {', '.join(df.columns)}. Total passengers: {len(df)}."
chain = LLMChain(llm=llm, prompt=prompt)

def process_query(question):
    response = chain.run(question=question, data_summary=data_summary)
    response = re.sub(r'```.*?```|`[^`]*`|\bTOOL_CALL\b', '', response, flags=re.DOTALL).strip()
    return parse_response(response)

def parse_response(response):
    lines = response.strip().split('\n')
    text_answer = ""
    viz_type = None
    viz_column = None
    for line in lines:
        if line.startswith("Visualization:"):
            parts = line.split(" of ")
            viz_type = parts[0].replace("Visualization: ", "").strip()
            viz_column = parts[1].strip() if len(parts) > 1 else None
        else:
            text_answer += line + " "
    return text_answer.strip(), viz_type, viz_column

def generate_visualization(viz_type, viz_column):
    plt.figure(figsize=(8, 6))
    if viz_type == "histogram" and viz_column in df.columns:
        sns.histplot(df[viz_column].dropna(), bins=20)
        plt.title(f"Histogram of {viz_column}")
    elif viz_type == "bar" and viz_column in df.columns:
        sns.countplot(x=viz_column, data=df)
        plt.title(f"Bar Plot of {viz_column}")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf.getvalue()

def analyze_data(question):
    text_answer, viz_type, viz_column = process_query(question)
    viz_bytes = None
    if viz_type and viz_column:
        viz_bytes = generate_visualization(viz_type, viz_column)
    if not text_answer and viz_type:
        text_answer = f"The {viz_type} shows the distribution of {viz_column}."
    return text_answer, viz_bytes