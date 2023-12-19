#we will be making a tip calculat
print("welcome to the tip calculator")
total = float(input("what was the total amount of bill? $"))
tip = int(input("how much tip are you willing to give?"))
people = int(input("how many people are splitting this bill?"))
#lets calculate bill with tip
bill_tip = total *(1+tip/100)
bill_per_person = bill_tip/people
final = round(bill_per_person, 2)
print(f"each person needa pay ${final}")
