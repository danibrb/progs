import pandas as pd
from tkinter import Tk, Label, Entry, filedialog, Button, StringVar
import unicodedata

def open_file():
    """Opens an XLSX file using a file dialog and creates a DataFrame."""
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select File", filetypes=[("Excel Files", "*.xlsx")]
    )

    if file_path:
        try:
            df = pd.read_excel(file_path)
            print("File opened successfully!")
            create_domain_window(df.copy())  # Call function to create input window
        except Exception as e:
            print(f"Error opening file: {e}")
    else:
        print("No file selected.")

    root.destroy()  # Destroy the hidden window


def get_domain_and_password(df):
    """Gets the domain name and password from the text boxes and processes data."""
    domain_name = domain_entry.get()
    password = password_entry.get()
    if domain_name and password:
        # Process data (ensure 'CL' is string, create additional emails,...)
        df["CL"] = df["CL"].apply(str)
        df["Group Email"] = "studenti_" + df["CL"] + df["SEZ"] + "@" + domain_name

        df["AN"] = df["AN"].apply(str)  # Ensure 'AN' is string
        combined_name = df["NOME"] + "." + df["COGNOME"] + "." + df["AN"]
        df["Email Address"] = create_email_address(combined_name, domain_name)

        df["Password"] = password
        print(df)  # Print the DataFrame with added columns


def create_email_address(name_data, domain_name):
    """Creates valid email addresses from the given data and domain."""
    emails = []
    for name in name_data:
        # Normalize name (handle characters, remove quotes, replace spaces)
        normalized_name = normalize_name(name)
        email = normalized_name.lower() + "@" + domain_name
        emails.append(email)
    return emails


def normalize_name(name):
    """Normalizes a name string for email address creation."""
    normalized_name = (
        unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("utf-8")
    )
    normalized_name = normalized_name.replace("'", "").replace(" ", ".")
    return normalized_name


def create_domain_window(df):
    """Creates a window for entering domain name, password, and export button."""
    domain_window = Tk()
    domain_window.title("Enter Domain Name and Password")

    # Labels and text boxes for domain name (default text) and password (show characters)
    domain_label = Label(domain_window, text="Enter Domain Name:")
    domain_label.pack()
    global domain_entry
    domain_entry = Entry(
        domain_window, insertwidth=0, textvariable=StringVar(value="calvino.edu.it")
    )
    domain_entry.insert(0, "calvino.edu.it")
    domain_entry.pack()

    password_label = Label(domain_window, text="Enter Password:")
    password_label.pack()
    global password_entry
    password_entry = Entry(domain_window, textvariable=StringVar(value="Calvino2025!"))
    password_entry.insert(0, "Calvino2025!")
    password_entry.config(show="")  # Show characters as typed
    password_entry.pack()

    # Submit button to process data
    submit_button = Button(
        domain_window, text="Submit", command=lambda: get_domain_and_password(df)
    )
    submit_button.pack()

    # Export button to save DataFrame as CSV
    export_button = Button(
        domain_window, text="Export Data (CSV)", command=lambda: export_data(df)
    )
    export_button.pack()

    domain_window.mainloop()  # Start the event loop for the window


def export_data(df):
    """Exports the DataFrame with processed data (emails, password) to a CSV file."""
    try:
        # Prompt user for filename and location to save the CSV
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")],
            title="Save Data as CSV",
        )
        if file_path:
            # Save the DataFrame to the chosen CSV file
            df.to_csv(file_path, index=False)
            print("Data exported successfully!")
        else:
            print("Export cancelled.")
    except Exception as e:
        print(f"Error exporting data: {e}")


if __name__ == "__main__":
    open_file()
