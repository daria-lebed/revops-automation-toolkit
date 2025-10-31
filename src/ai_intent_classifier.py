import pandas as pd

# Правильный путь к файлу
input_file = "data/outputs/tagged_leads.csv"
output_file = "data/outputs/intent_classified_leads.csv"

# Загружаем CSV
df = pd.read_csv(input_file)

# Добавляем простую классификацию интента (пример)
def classify_intent(stage):
    stage = stage.lower()
    if "sql" in stage or "qualified" in stage:
        return "Ready to Engage"
    elif "engaged" in stage:
        return "Nurture"
    elif "cold" in stage:
        return "Reactivation Needed"
    else:
        return "New Lead"

df["intent"] = df["lifecycle_stage"].apply(classify_intent)

# Сохраняем результат
df.to_csv(output_file, index=False)

print(f"✅ Intent classification complete! Saved to {output_file}")