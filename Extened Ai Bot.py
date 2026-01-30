print("🤖 Hello! I’m ChatBuddy.")
name = input("What’s your name? ").strip()

if not name:
    name = "Friend"

print(f"\nNice to meet you, {name}!")

while True:
    print("\nHow are you feeling today?")
    print("Options: happy / sad / angry / bored")
    mood = input("Your mood: ").lower().strip()

    if mood == "happy":
        print("😊 That’s awesome! Keep smiling!")
    elif mood == "sad":
        print("😔 I’m sorry to hear that. Things will get better.")
    elif mood == "angry":
        print("😠 Take a deep breath. Want to talk about it?")
    elif mood == "bored":
        print("😐 Let’s fix that! I can chat with you.")
    else:
        print("🤔 Hmm… I don’t quite understand that mood.")


    print("\nWhat would you like to talk about?")
    print("1. Hobbies")
    print("2. Studies")
    print("3. Fun fact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        hobby = input("What’s your favorite hobby? ")
        print(f"🎨 Cool! {hobby.capitalize()} sounds fun.")
    elif choice == "2":
        subject = input("What subject do you like the most? ")
        print(f"📚 Nice! {subject.capitalize()} is interesting.")
    elif choice == "3":
        print("🤯 Fun Fact: Octopuses have three hearts!")
    elif choice == "4":
        print(f"👋 Goodbye, {name}! Take care.")
        break
    else:
        print("❌ Invalid choice. Please select 1–4.")


    repeat = input("\nDo you want to continue chatting? (yes/no): ").lower().strip()
    if repeat != "yes":
        print(f"👋 Thanks for chatting, {name}! See you next time.")
        break