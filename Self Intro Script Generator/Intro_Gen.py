import datetime

name = input("Enter your name ").strip()
age = input("How old are you  ").strip()
city = input("In which city you live ").strip()
profession = input("What is your profession ").strip()
hobby = input("What is you favorite hobby ").strip()
  
intro ="""Hi, My name is {name} , I am {age} years old. And live in {city}. 
I work as a {profession} and enjoy {hobby} in my free time.
Nice to meet you!
""".format(name= name , age = age , city = city , profession = profession , hobby = hobby)

style = "*" * 80
currdate = datetime.date.today()

print(f"\n{style}\n{intro}\n{currdate}\n{style}")