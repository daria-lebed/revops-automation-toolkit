import pandas as pd

def generate_hygiene_report(input_file, output_file):
    """
    Generates a CRM hygiene report with:
    - Total leads
    - Leads per lifecycle stage
    - Duplicate and empty email counts
    """
    df = pd.read_csv(input_file)

    total_leads = len(df)
    duplicates = df['email'].duplicated().sum()
    empty_emails = df['email'].isna().sum()

    stage_counts = df['lifecycle_stage'].value_counts().to_dict()

    report = {
        "total_leads": total_leads,
        "duplicate_emails": duplicates,
        "empty_emails": empty_emails,
        **{f"{stage}_count": count for stage, count in stage_counts.items()}
    }

    report_df = pd.DataFrame([report])
    report_df.to_csv(output_file, index=False)
    print(f"✅ Hygiene report generated: {output_file}")
    print(report_df.T)

# Пример использования
if __name__ == "__main__":
    generate_hygiene_report("../data/outputs/tagged_leads.csv", "../data/outputs/hygiene_report.csv")