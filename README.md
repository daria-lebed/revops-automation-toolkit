# ⚙️ RevOps Automation Toolkit  
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

## 🧩 Tech Stack
| Category | Tools |
|-----------|-------|
| Programming | Python, Pandas, Regex |
| Data | CSV Pipelines |
| Automation | HubSpot API (coming soon) |
| Version Control | Git & GitHub |

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

## 🔧 Installation
```bash
git clone https://github.com/daria-lebed/revops-automation-toolkit.git
cd revops-automation-toolkit
python3 -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

---

## ▶️ Usage
```bash
python src/email_cleaner.py
python src/lifecycle_tagging.py
python src/hygiene_report.py
```

---

## 📊 Outputs
- 🧹 Cleaned leads → `data/outputs/cleaned_leads.csv`  
- 🏷️ Tagged leads → `data/outputs/tagged_leads.csv`  
- 📈 Hygiene report → `docs/hygiene_before_after.md`

**Example Result:**  
Before cleaning → 78 % valid emails  
After cleaning → 96 % valid emails  
📈 Improvement: +18 %

---

## 🔮 Next Steps
- 🔗 HubSpot API integration  
- 🧠 AI-driven lead enrichment  
- 🤖 Automated follow-up and lead scoring  

---

## 👩‍💻 Author
**Daria Lebed**  
RevOps & CRM Automation | HubSpot | AI-Powered Sales Systems  
📫 [LinkedIn](https://www.linkedin.com/in/dioraswan/) | [GitHub](https://github.com/daria-lebed)

---

⭐ If you find this useful, please star the repo — it helps more RevOps builders discover automation tools!  
python src/hygiene_report.py
```
