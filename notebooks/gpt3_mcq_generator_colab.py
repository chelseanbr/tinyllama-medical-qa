
# Medical MCQ Generation using GPT-3.5 Turbo

import openai
import json
import time
from pathlib import Path
from tqdm import tqdm

# 🔑 Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# 📄 Load your input Q&A pairs
with open("qa_data.jsonl", "r") as f:
    qa_data = [json.loads(line) for line in f]

# 🧠 Prompt builder
def build_prompt(question, answer):
    return f"""Convert the following medical Q&A into a multiple-choice question.

Question: {question}
Answer: {answer}

Provide output in this XML format:

<question>...</question>
<choices>
A. ...
B. ...
C. ...
D. ...
</choices>
<reason>...</reason>
<answer>C</answer>
"""

# 🚀 Generate MCQ with retries
def generate_mcq(prompt, model="gpt-3.5-turbo", retries=3):
    for attempt in range(retries):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=512,
            )
            return response.choices[0].message.content.strip()
        except openai.error.OpenAIError as e:
            print(f"Error: {e}. Retrying...")
            time.sleep(1)
    return None

# 📤 Output file
output_path = Path("generated_mcqs.jsonl")

with open(output_path, "a") as f:
    for idx, row in tqdm(enumerate(qa_data), total=len(qa_data)):
        prompt = build_prompt(row["question"], row["answer"])
        completion = generate_mcq(prompt)
        if completion:
            entry = {
                "question": row["question"],
                "answer": row["answer"],
                "completion": completion
            }
            f.write(json.dumps(entry) + "\n")
        if idx % 100 == 0:
            print(f"{idx} / {len(qa_data)} completed")

print(f"✅ Saved to {output_path}")
