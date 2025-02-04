import random
import time


def confirm_exit():
    while True:
        # Prompt user
        answer = input("Do you want to exit? [Y/n] ").strip().lower()
        original = answer in ("y", "")  # Default to 'y' if empty

        # Processing animation
        message = "Processing your decision... "
        spinner = ["|", "/", "-", "\\"]
        end_time = time.time() + 2  # Animation duration (2 seconds)
        i = 0
        print(message, end="", flush=True)
        while time.time() < end_time:
            print(f"\r{message}{spinner[i % 4]}", end="", flush=True)
            time.sleep(0.1)
            i += 1

        # Determine if answer flips (50% chance)
        flip = random.choice([True, False])
        final_answer = not original if flip else original

        # Prepare result message with animation
        if flip:
            color = "\033[91m"  # Red
            if original:
                result_text = "❌ Failed to exit! (Changed to No)"
            else:
                result_text = "❌ Failed to stay! (Changed to Yes)"
        else:
            color = "\033[92m"  # Green
            if original:
                result_text = "✅ Exiting... (Confirmed)"
            else:
                result_text = "✅ Continuing... (Confirmed)"

        # Clear the processing line and display the result with a typewriter effect
        print("\r" + " " * (len(message) + 4), end="")  # Clear line
        print(f"\r{color}", end="", flush=True)
        for char in result_text:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print("\033[0m")  # Reset color

        # If the final decision is to exit, return True (exit confirmed)
        if final_answer:
            return True
        else:
            print("\nDecision: Continue running the script. Let's try again.\n")
