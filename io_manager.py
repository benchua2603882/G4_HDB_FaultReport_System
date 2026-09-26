from datetime import datetime
from pathlib import Path


def show_menu():
    """Display the menu and return a valid user choice."""

    while True:
        print("\nHDB Fault Reporting System")
        print("1. Submit a complaint")
        print("2. View reports")
        print("Type 'quit' to exit.")

        choice = input("Choose an option: ").strip().lower()

        if choice in ("1", "2", "quit"):
            return choice

        print("Invalid input. Enter 1, 2, or quit.")


def collect_name():
    """Accept a nonempty name containing only letters and spaces."""

    while True:
        name = input("What is your name? ").strip()

        if name and all(
            char.isalpha() or char == " " for char in name
        ):
            return name

        print("Invalid name. Enter letters and spaces only.")


def collect_phone_number():
    """Accept digits with an optional single '+' at the beginning."""

    while True:
        phone_number = input(
            "What is your phone number? "
        ).strip()

        # Remove a leading '+' only for checking.
        # Keep the original input for storage.
        digits = (
            phone_number[1:]
            if phone_number.startswith("+")
            else phone_number
        )

        if digits and all(
            char in "0123456789" for char in digits
        ):
            return phone_number

        print(
            "Invalid phone number. Enter digits only, "
            "with an optional '+' at the beginning."
        )


def get_required_input(prompt):
    """Repeat a question until the user enters a nonempty answer."""

    while True:
        answer = input(prompt).strip()

        if answer:
            return answer

        print("This field cannot be empty. Please try again.")


def collect_image_path():
    """Return a valid image path, or 'no_image' if no image is attached."""

    project_folder = Path(__file__).resolve().parent
    allowed_extensions = {".jpg", ".jpeg", ".png", ".webp"}

    # Ask whether the user wants to attach an image.
    while True:
        answer = input(
            "Do you have an image to attach? (Y/N): "
        ).strip().lower()

        if answer == "n":
            return "no_image"

        if answer == "y":
            break

        print("Invalid input. Please enter Y or N.")

    # If the user selected Y, ask for the image path.
    while True:
        image_path = input(
            "Enter the image path "
            "(e.g. test_images/leak.jpg): "
        ).strip().strip("\"'")
                #Test images example below =========
                # water_pipe_leak.png
                # broken_floor_tile.png
                # exposed_wires.png
                # broken_flowerpot.png
                # function_room_fire.png

        if not image_path:
            print("The image path cannot be empty.")
            continue

        path = Path(image_path).expanduser()

        # Resolve relative paths from the folder containing this file.
        if not path.is_absolute():
            path = project_folder / path

        if not path.is_file():
            print("File not found. Please check the path.")
            continue

        if path.suffix.lower() not in allowed_extensions:
            print("Please select a JPG, JPEG, PNG, or WEBP image.")
            continue

        return str(path.resolve())


def collect_complaint():
    """Collect validated details and package them into a complaint list."""

    print("\n--- Submit a Complaint ---")

    # Ask and validate each question before continuing.
    name = collect_name()
    phone_number = collect_phone_number()
    description = get_required_input("What is your complaint? ")
    image_path = collect_image_path()

    # Use a placeholder until complaint ID generation is implemented.
    complaint_id = "complain_id_here"

    # Record the submission time using the computer's local timezone.
    date_time = datetime.now().astimezone().isoformat(
        timespec="seconds"
    )

    # Complaint ID is first; submission date and time are last.
    complaint = [
        complaint_id,
        name,
        phone_number,
        description,
        image_path,
        date_time
    ]

    return complaint


def show_message(message):
    """Display a message or complaint list."""

    print(message)


def show_goodbye():
    """Display a goodbye message when the user exits."""

    print("Goodbye!")