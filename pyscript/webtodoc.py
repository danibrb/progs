import requests
from bs4 import BeautifulSoup
from docx import Document

def save_webpage_as_doc(url, output_path):
    # Send a GET request to the web page
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create a new Word document
    doc = Document()
    
    # Extract the text from the HTML and add it to the document
    for paragraph in soup.find_all('p'):
        doc.add_paragraph(paragraph.get_text())
    
    # Save the document to the specified output path
    doc.save(output_path)

# URL of the web page to save
url = 'https://canti.app/luce/'

# Output path for the DOC file
output_path = './output.docx'

# Save the web page as a DOC file
save_webpage_as_doc(url, output_path)