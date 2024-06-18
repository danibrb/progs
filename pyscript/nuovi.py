import pandas as pd
from tkinter import Tk, Label, Entry, filedialog, Button, StringVar
import unicodedata

def open_file():
  """Opens an xls file using a file dialog and creates a DataFrame."""
  root = Tk()
  root.withdraw()  # Hide the main window

  file_path = filedialog.askopenfilename(title="Select File", filetypes=[("Excel Files", "*.xlsx")])

  if file_path:
    try:
      df = pd.read_excel(file_path)
      print("File opened successfully!")
      # You can now work with the DataFrame (df) here
      create_domain_window(df)  # Call function to create domain and password input window
    except Exception as e:
      print(f"Error opening file: {e}")
  else:
    print("No file selected.")

  root.destroy()  # Destroy the hidden window

def get_domain_and_password(df):
  """Gets the domain name and password entered in the text boxes and processes data."""
  domain_name = domain_entry.get()
  password = password_entry.get()
  if domain_name and password:
    # Convert 'CL' column to string
    df['CL'] = df['CL'].apply(str)

    # Create additional email addresses
    df['Additional Email'] = "studenti_" + df['CL'] + df['SEZ'] + "@" + domain_name

    # Combine all three columns with dots (original email)
    df['AN'] = df['AN'].apply(str)  # Ensure 'AN' is string
    combined_name = df['NOME'] + '.' + df['COGNOME'] + '.' + df['AN']
    df['Email Address'] = create_email_address(combined_name, domain_name)

    # Assign the password to all emails
    df['Password'] = password
    print(df)  # Print the DataFrame with added columns
  else:
    print("Please enter a domain name and password.")

def create_email_address(name_data, domain_name):
  """Creates valid email addresses from the given data and domain."""
  emails = []
  for name in name_data:
    # Normalize name, replacing accented letters, removing quotes, replacing spaces with dots
    normalized_name = normalize_name(name)
    # Create email address and append to list
    email = normalized_name.lower() + '@' + domain_name
    emails.append(email)
  return emails

def normalize_name(name):
  """Normalizes a name string for email address creation."""
  normalized_name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8')
  normalized_name = normalized_name.replace("'", "").replace(" ", ".")
  return normalized_name

def create_domain_window(df):
  """Creates a new window for entering the domain name and password."""
  domain_window = Tk()
  domain_window.title("Enter Domain Name and Password")

  # Create a label for domain name
  domain_label = Label(domain_window, text="Enter Domain Name:")
  domain_label.pack()

  # Create a text box for domain name with default text
  global domain_entry
  domain_entry = Entry(domain_window, insertwidth=0, textvariable=StringVar(value="calvino.edu.it"))  # Set default text
  domain_entry.insert(0,"calvino.edu.it")
  domain_entry.pack()

  # Create a label for password
  password_label = Label(domain_window, text="Enter Password:")
  password_label.pack()

  # Create a text box for password (show characters and default text)
  global password_entry
  password_entry = Entry(domain_window, textvariable=StringVar(value="Calvino2025!"))  # Set default text
  password_entry.insert(0,"Calvino2025!")
  password_entry.config(show="")  # Show characters as typed
  password_entry.pack()

  # Create a button to submit
  submit_button = Button(domain_window, text="Submit", command=lambda: get_domain_and_password(df.copy()))
  submit_button.pack()

  domain_window.mainloop()

if __name__ == "__main__":
  open_file()
