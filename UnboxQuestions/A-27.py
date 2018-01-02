from datetime import datetime, date

print("Your date of birth (dd mm yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age)