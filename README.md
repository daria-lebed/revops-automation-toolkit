# ⚙️ RevOps Automation Toolkit  
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai&logoColor=white)
![HubSpot](https://img.shields.io/badge/HubSpot-CRM-orange?logo=hubspot&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
**CRM Hygiene • Lifecycle Tagging • AI-Ready Data Pipelines**

Modern RevOps system that automates CRM cleaning, lifecycle tagging, and reporting for B2B SaaS sales teams.

---

## 🧠 About the Project
This toolkit automates data hygiene and segmentation across CRM systems to help revenue teams operate faster and smarter.

**Goal:** streamline CRM operations without losing personalization.  
**Built by:** Daria Lebed — RevOps & CRM Automation Engineer  

---

## 🚀 Features
✅ Email validation & format correction  
✅ Lifecycle stage tagging (Engaged / Nurture / Cold / Unqualified)  
✅ Before/after data hygiene report  
✅ Modular Python architecture ready for HubSpot API integration  

---

## ⚙️ Tech Stack  
- **Python 3.13**  
- **OpenAI GPT-4o-mini** (AI report generation)  
- **Pandas / OpenPyXL** (data analytics & processing)  
- **HubSpot API** (CRM automation)

---

## 🧠 AI Summary Module  
The `src/ai_summary.py` module automatically:  
1. Generates CRM and revenue summaries via OpenAI  
2. Saves results in `data/outputs/` and formatted `.md` reports  
3. Integrates outputs into Notion dashboards  

🧾 Example Output:  
[📄 `docs/ai_summary.md`](./docs/ai_summary.md)  

---

## 📁 Project Structure
```
revops-automation-toolkit/
│
├── data/
│   ├── inputs/             # raw lead lists (CSV)
│   └── outputs/            # cleaned lists & tagged leads
├── docs/                   # reports & docs
├── src/                    # source code
│   ├── email_cleaner.py
│   ├── lifecycle_tagging.py
│   └── hygiene_report.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation  
```bash
git clone https://github.com/daria-lebed/revops-automation-toolkit.git
cd revops-automation-toolkit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## 🧩 Usage  
```bash
export OPENAI_API_KEY="your_api_key_here"
python3 src/ai_summary.py
```

Results will appear in:  
- `data/outputs/ai_summary.txt`  
- `docs/ai_summary.md`  

---

## 🌐 Vision  
Creating scalable, AI-driven RevOps systems that enhance revenue operations, automate analytics, and make data human-readable.  

---

## 👩‍💻 Author
**Daria Lebed**  
RevOps & CRM Automation | HubSpot | AI-Powered Sales Systems  
📫 [LinkedIn](https://www.linkedin.com/in/dioraswan/) | [GitHub](https://github.com/daria-lebed)

---

⭐ If you find this useful, please star the repo — it helps more RevOps builders discover automation tools!  
python src/hygiene_report.py
```
