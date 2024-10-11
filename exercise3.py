eating_out = int(input("How many times do you eat out per week? "))
price_of_lunch = float(input("What is the average cost of a student lunch? "))
price_of_groceries = float(input("What is the average cost of doing your groceries? "))

weekly_expenditure = round(eating_out * price_of_lunch + price_of_groceries)
daily_expenditure = round(weekly_expenditure / 7)

print(f"Average food expenditure: Daily: {daily_expenditure}. Weekly: {weekly_expenditure}")