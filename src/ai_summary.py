import os
from openai import OpenAI

# --- API key setup ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Input prompt ---
prompt = """
Summarize CRM hygiene metrics and revenue forecast insights 
for a B2B SaaS team as if it’s an executive report.
"""

# --- Output paths ---
txt_path = "data/outputs/ai_summary.txt"
md_path = "docs/ai_summary.md"

def clean_text(text):
    return text.replace("\r", "").replace("\n", " ").strip()

try:
    # --- Generate AI summary ---
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional RevOps automation analyst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        temperature=0.7
    )

    summary = clean_text(response.choices[0].message.content)

    # --- Ensure folders exist ---
    os.makedirs("data/outputs", exist_ok=True)
    os.makedirs("docs", exist_ok=True)

    # --- Save to text file ---
    with open(txt_path, "w", encoding="utf-8", errors="replace") as txt:
        txt.write(summary)

    # --- Save to Markdown for GitHub ---
    md_template = f"""# 📊 AI Summary Report

**Model:** GPT-4o-mini  
**Context:** RevOps & CRM Automation Toolkit  

---

### 🧠 Executive Summary  
{summary}

---

*Generated automatically via AI-powered RevOps pipeline.*
"""
    with open(md_path, "w", encoding="utf-8", errors="replace") as md:
        md.write(md_template)

    print("\n✅ Summary successfully created!")
    print(f"📄 Text saved to: {txt_path}")
    print(f"🧾 Markdown saved to: {md_path}")

except Exception as e:
    with open("error_log.txt", "w", encoding="utf-8", errors="replace") as log:
        log.write(str(e))
    print("❌ Runtime Error:", e)