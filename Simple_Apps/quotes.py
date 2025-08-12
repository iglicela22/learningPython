import random

quotes = [
    "My life is my message.",
    "Our life is what our thoughts make it.",
    "The best way to find yourself is to lose yourself in the service of others.",
    "In a gentle way, you can shake the world.",
    "Live as if you were to die tomorrow. Learn as if you were to live forever.",
]

print("Random Quote Generator <3")
print("Hopefull you will find some inspiration here!")
while True:
    user_input = input(">>> ")
    if user_input.lower() == "q":
        print("You will get inspired someday!")
        break

    quote = random.choice(quotes)
    print("\n" + quote)
    print("----------------------")
      
      