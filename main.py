import io_manager


def main():
    """Run the menu and selected actions until the user types 'quit'."""

    # Show the menu again after each action finishes.
    while True:
        choice = io_manager.show_menu()

        if choice == "quit":
            io_manager.show_goodbye()

            # Leave the loop and finish the main function.
            break

        elif choice == "1":
            # Run the complaint submission workflow.
            io_manager.process_new_report()

        elif choice == "2":
            # Retrieve and display saved reports.
            io_manager.view_reports()


# Start the application only when this file is run directly.
# Importing main.py from another file will not start the menu.
if __name__ == "__main__":
    main()