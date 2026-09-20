import io_manager
import ai_manager


def process_new_report():
    """Collect a complaint, package it, and send it to the AI Manager."""

    # Ask the user to describe the problem.
    complaint = io_manager.collect_complaint()

    # Package the input into a dictionary.
    # Additional fields such as location can be added later.
    report = {
        "description": complaint
    }

    io_manager.show_message("\nAnalysing your complaint...")

    # The AI Manager handles the Gemini API call and response validation.
    ai_result = ai_manager.analyse_report(report)

    # Agreed convention: return None if analysis fails.
    if ai_result is None:
        io_manager.show_message(
            "Unable to analyse your complaint. Please try again later."
        )
        return

    # Display the validated AI response for now.
    io_manager.show_message(f"\nAnalysis result: {ai_result}")

    # Return both the original input and the AI analysis.
    return {
        **report,
        "ai_analysis": ai_result
    }

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