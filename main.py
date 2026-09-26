import io_manager


def process_new_report():
    """Collect user input and return the complaint list."""

    complaint = io_manager.collect_complaint()

    io_manager.show_message("\nComplaint details collected:")
    io_manager.show_message(complaint)

    return complaint


def main():
    """Keep showing the menu until the user types 'quit'."""

    # Store all complaints collected during this run.
    complaints = []

    while True:
        choice = io_manager.show_menu()

        if choice == "quit":
            io_manager.show_goodbye()
            break

        elif choice == "1":
            # Collect a complaint and add it to the list.
            complaint = process_new_report()
            complaints.append(complaint)

        elif choice == "2":
            # Display complaints collected during this run.
            if not complaints:
                io_manager.show_message("\nNo complaints collected yet.")
            else:
                for complaint in complaints:
                    io_manager.show_message(complaint)


# Start the application when this file is run directly.
if __name__ == "__main__":
    main()