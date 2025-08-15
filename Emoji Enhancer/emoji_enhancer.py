"""
 Challenge: Emoji Enhancer for Messages

Create a Python script that takes a message and adds emojis after specific keywords to make it more expressive.

Your program should:
1. Ask the user to input a message.
2. Add emojis after certain keywords (like "happy", "love", "code", "tea", etc.).
3. Print the updated message with emojis.

Example:
Input:
  I love to code and drink tea when I'm happy.

Output:
  I love ❤️ to code 💻 and drink tea 🍵 when I'm happy 😊.

Bonus:
- Make it case-insensitive (match "Happy" or "happy")
- Handle punctuation (like commas or periods right after keywords)

"""


all_emoji = {
    "love":"❣️",
    "code":"💻",
    "happy":"😊",
    "sad":"😔",
    "tea":"🍵",
    "music":"🎵"
}

update = []
pera = input("Enter your message -> ")

for word in pera.split():
    cleaned = word.lower().strip(",.?|")
    emoji = all_emoji.get(cleaned)
    if emoji:
        update.append(f"{word} {emoji}")
    else:
        update.append(word)

final_result = " ".join(update)
print(final_result)