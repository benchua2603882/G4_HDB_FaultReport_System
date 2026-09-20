def show_menu():
    """Display the menu and return a valid user choice."""

    # Keep asking until the user enters a valid option.
    while True:
        print("\nHDB Fault Reporting System")
        print("1. Submit a complaint")
        print("2. View reports")
        print("Type 'quit' to exit.")

        # Remove surrounding spaces and convert input to lowercase.
        choice = input("Choose an option: ").strip().lower()

        # Return the valid choice to main.py.
        if choice in ("1", "2", "quit"):
            return choice

        # Invalid input: display an error, then repeat the menu.
        print("Invalid input. Enter 1, 2, or quit.")


def show_goodbye():
    """Display a goodbye message when the user exits."""

    print("Goodbye!")



def process_new_report():
    return




def view_reports():
    return