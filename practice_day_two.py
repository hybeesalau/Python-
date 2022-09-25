age = int(input("What is your age? \n"))
year_left = (90 - age)
age_in_days = (age*365)
days_in_90years = (90*365)
age_left = days_in_90years - age_in_days
print(f"If your age threshold is 90 years, You will die at the age of {year_left} years which means you have {age_left} days left")
