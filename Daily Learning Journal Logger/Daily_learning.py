"""
 Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add an optional rating (1-5) for how productive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
📅 2025-06-14 — 10:45 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

import datetime 

today_learning = input("Enter what you learn today -> ").strip()
curr_date = datetime.datetime.now()
date_str = curr_date.strftime("%Y-%m-%d - %I:%M %p")
rating = input("Give today learning rating out of 5 (optional) -> ").strip()

style = "-" * 50 

# with open("learning_journal.txt","a") as f:
#     f.write(f"{date_str}\n")
#     f.write(f"today_learning \n")
#     f.write(f"Productivity Rating: {rating}/5")
#     f.write(style)

# print("file sucessfully saved")


learning_journal = f"\n{date_str}\n{today_learning}"
if rating:
    learning_journal += f"\nProductivity Rating : {rating}/5\n{style}"
else:
    learning_journal += f"\n{style}"

with open("learning_journal.txt","a") as f:
    f.write(learning_journal)


print("file sucessfully saved")