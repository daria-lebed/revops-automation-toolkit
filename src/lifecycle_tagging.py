import pandas as pd

def tag_lifecycle_stage(input_file, output_file):
    """
    Adds lifecycle stages based on simple logic:
    - New Lead: no company or short name
    - Engaged: company known but no domain email
    - SQL: domain email and known company
    - Customer: email includes partner domain
    """
    df = pd.read_csv(input_file)

    def assign_stage(row):
        email = str(row.get("email", "")).lower()
        company = str(row.get("company", "")).lower()

        if not company or len(company) < 3:
            return "New Lead"
        elif "gmail" in email or "yahoo" in email:
            return "Engaged"
        elif any(x in email for x in ["lbank", "bybit", "binance", "aaa-charm"]):
            return "Customer"
        else:
            return "SQL"

    df["lifecycle_stage"] = df.apply(assign_stage, axis=1)
    df.to_csv(output_file, index=False)
    print(f"✅ Lifecycle tags added and saved to: {output_file}")

# Пример использования
if __name__ == "__main__":
    tag_lifecycle_stage("../data/outputs/cleaned_leads.csv", "../data/outputs/tagged_leads.csv")