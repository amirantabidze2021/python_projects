import time
name = input("ra gkvia?: ")
print(f"gamarjoba, {name}. tamashis droa!")
time.sleep(1)
print("davitskot gamocnoba...")
time.sleep(0.5)
word = "computer"
guesses = ''
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("shen moige")
        break
    guess = input("gamoicani simbolo:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("arasworia")
        print(f"shen dagrcha {turns} cdebis raodenoba")
        if turns == 0:
            print("shen tsaage")