import pandas as pd

def clean_email_list(input_file, output_file):
    """
    Cleans a raw CSV list of leads by:
    - Removing duplicates
    - Dropping empty rows
    - Filtering invalid emails
    """
    df = pd.read_csv(input_file)

    # Удаляем пустые строки и дубликаты
    df.dropna(subset=['email'], inplace=True)
    df.drop_duplicates(subset=['email'], inplace=True)

    # Фильтруем некорректные email'ы
    df = df[df['email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', na=False)]

    # Сохраняем чистую версию
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned list saved to: {output_file}")

# Пример использования
if __name__ == "__main__":
    clean_email_list("../data/inputs/raw_leads.csv", "../data/outputs/cleaned_leads.csv")