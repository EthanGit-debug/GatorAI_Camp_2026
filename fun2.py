from datetime import datetime

birth_date_input = input("Enter your birthday (YYYY-MM-DD): ")

try:
    birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d").date()
    today = datetime.today().date()
    age_in_days = (today - birth_date).days
    print(f"You are {age_in_days} days old.")
except ValueError:
    print("Please enter the date in YYYY-MM-DD format.")
