# Main application logic

from stopwatch import stopwatch
from timerwatch import countdown_timer

def main():
    print("Welcome to the Timer and Stopwatch App!")
    while True:
        print("Select an option:")
        print("1. Timer")
        print("2. Stopwatch")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            seconds = int(input("Enter the number of seconds for the timer: "))
            countdown_timer(seconds)
        elif choice == "2":
            stopwatch()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

