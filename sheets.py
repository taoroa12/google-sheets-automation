import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

sheet = client.open("Portfolio Test").sheet1

sheet.update("A1", [["Имя", "Возраст", "Город"]])

data = [
    ["Алексей", 25, "Москва"],
    ["Мария", 30, "Санкт-Петербург"],
    ["Иван", 22, "Казань"],
]
sheet.append_rows(data)

print("Данные записаны!")

records = sheet.get_all_values()
for row in records: 
    print(row)