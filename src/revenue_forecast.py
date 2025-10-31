import pandas as pd

# Правильный путь к файлам
input_file = "data/outputs/intent_classified_leads.csv"
output_file = "data/outputs/revenue_forecast.csv"

# Загружаем классифицированные лиды
df = pd.read_csv(input_file)

# Добавляем примерную оценку выручки (моковые данные)
def forecast(intent):
    if intent == "Ready to Engage":
        return 5000
    elif intent == "Nurture":
        return 2000
    elif intent == "Reactivation Needed":
        return 1000
    else:
        return 500

df["forecast_revenue_$"] = df["intent"].apply(forecast)

# Сохраняем отчёт
df.to_csv(output_file, index=False)

print(f"✅ Revenue forecast generated! Saved to {output_file}")