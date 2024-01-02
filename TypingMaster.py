import json
import random
import time
import os

def update_leaderboard(username, wpm):
    leaderboard_file = 'leaderboard.json'

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
    else:
        leaderboard = []

    leaderboard.append({'username': username, 'wpm': wpm})
    leaderboard = sorted(leaderboard, key=lambda x: x['wpm'], reverse=True)[:5]

    with open(leaderboard_file, 'w') as file:
        json.dump(leaderboard, file, indent=2)

def show_leaderboard():
    leaderboard_file = 'leaderboard.json'

    if os.path.exists(leaderboard_file):
        with open(leaderboard_file, 'r') as file:
            leaderboard = json.load(file)
            print("\nLeaderboard:")
            for entry in leaderboard:
                print(f"{entry['username']}: {entry['wpm']} WPM")
    else:
        print("\nLeaderboard is empty.")

def load_words_from_json(category):
    words_file = 'words.json'

    if os.path.exists(words_file):
        with open(words_file, 'r') as file:
            languages_data = json.load(file)

        if category in languages_data:
            return languages_data[category]
        else:
            print(f"Error: Words for category '{category}' not found.")
            return []
    else:
        print(f"Error: Programming languages file not found.")
        return []

def get_user_input():
    try:
        return input().strip()
    except KeyboardInterrupt:
        exit_game()

def main():
    print("Welcome to the Terminal Typing Master!")

    username = input("Enter your username: ")

    while True:
        print("\nOptions:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            print("\nChoose a category:")
            print("1. C")
            print("2. Python")
            print("3. Java")
            print("4. JavaScript")

            category_choice = input("Enter the number for your chosen category: ")

            categories = {
                '1': 'C',
                '2': 'Python',
                '3': 'Java',
                '4': 'JavaScript',

            }

            selected_category = categories.get(category_choice)
            if not selected_category:
                print("Invalid category choice.")
                continue

            num_words = int(input("Enter the number of words to practice (1-20): "))

            words = load_words_from_json(selected_category)

            if not words:
                continue

            words_to_type = random.sample(words, min(num_words, len(words)))

            print("\nWords to type:")
            print(" ".join(words_to_type))

            input("\nPress Enter to start the typing test...")
            start_time = time.time()

            for word in words_to_type:
                print(f"Type: {word}")
                user_input = get_user_input()
                if user_input.lower() == word.lower():
                    print("Correct! ")
                else:
                    print("Incorrect. ")

            print("\nTyping test completed!")


            end_time = time.time()
            time_taken = end_time - start_time

            typed_words = get_user_input().split()
            words_typed = len(typed_words)
            wpm = int((words_typed / time_taken) * 60)

            print("\nTyping Metrics:")
            print(f"Words Typed: {words_typed}")
            print(f"Time Taken: {time_taken:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm}")

            update_leaderboard("username", wpm)

        elif choice == '2':
            show_leaderboard()

        elif choice == '3':
            exit_game()

        else:
            print("Invalid choice. Please enter a valid option.")

def exit_game():
    print("\nExiting Terminal Typing Master. Goodbye!")
    exit()

if __name__ == "__main__":
    main()
