# Guess Number 🔢
# Codédex

# Initialize guess to 0 (arbitrary number not equal to 6)
guess = 0

# Initialize tries to count how many attempts the user makes
tries = 0

# Loop continues while the guess is wrong AND the user has tries left
while guess != 6 and tries < 5:
    # Ask the user to guess the number
    guess = int(input("Guess the number: "))

    # Increase the try count by 1
    tries = tries + 1

# After the loop ends, check if the guess was correct
if guess != 6:
    # User didn't guess correctly within the allowed tries
    print("You ran out of tries.")
else:
    # User guessed correctly
    print("You got it!")
