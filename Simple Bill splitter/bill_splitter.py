"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""


def get_amount(number):
    while True :
        try :
            return float(input(number))
        except ValueError:
            print("❌ Enter valid number ")
            
            
print("Simple Bill Splitter \n")
peoples = int(input("how many people in your group \n"))
Total_amt = get_amount("Enter your Total amount \n")
bill = round(Total_amt / peoples,2 )
person = []


for people in range(peoples):
    test = input(f"Enter Person name: {people+1}")
    person.append(test)
    
print("*" * 50)
print(f'Total bill: ₹{Total_amt}\n')
# print(person)
print("Each person own: ₹{bill}\n")
for i in person:
    print(f"{i} owes ₹{bill}")
print("*" * 50)



