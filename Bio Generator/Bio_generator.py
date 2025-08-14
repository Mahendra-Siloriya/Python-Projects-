"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
# """

import textwrap

name = input("Enter you name ").strip()
profession = input("Enter your profession ").strip()
passion = input("Enter your passion in one line or goal ").strip()
emoji = input("Enter your Favorite Emoji ").strip()
website = input("Enter your website or handle ").strip()

print("""\nChoose your style 
    1.Simple line 
    2.Vertical line 
    3.Emoji Sandwich """)


style = input("Enter 1 , 2, or 3 ").strip()

def generate_bio(style):
    
    if style == '1':
        return f"{emoji} {name}|{profession} \n💡 {passion}\n🔗 {website}"
    if style == '2':
        return f"{emoji} {name}|{profession}🔥 \n💡 {passion} 💡\n🔗 {website} 🔥"
    if style == '3':    
        return f"{emoji*3} \n{name}|{profession} \n{passion} 💡\n🔗 {website}\n{emoji*3}"


bio = generate_bio(style)
print(bio)

print("\nYour Stylish Bio\n")
print("*" * 50 )
print(textwrap.dedent(bio))
print("*" * 50 )

save = input("Do you want to save Y or N \n").strip().upper()

if save == 'Y':
    filename = f"{name.lower().replace(' ','_')}_bio.txt"
    print(filename)
    with open(filename,'w' ) as f:
        f.write(bio)
    print("saved file")
        