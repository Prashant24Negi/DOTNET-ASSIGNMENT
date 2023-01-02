from datetime import datetime

def validDate(user_date):
    try:
        dateObj = datetime.strptime(user_date,'%m/%d/%Y');
        return True;

    except ValueError:
        return False;

print("Date Format (mm/dd/yyyy)");
user_date = input("Enter your Date To Check: ");

print(validDate(user_date));