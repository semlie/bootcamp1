import fitz

def create_pdf_with_text(text, output_path):
    # Create a new PDF document
    doc = fitz.open()

    # Add a page to the document
    page = doc.new_page()

    # Split the text into lines
    lines = text.strip().split('\n')

    # Add the text to the page
    for line in lines:
        page.insert_text((10, page.rect.height - 20), line, fontsize=12)

    # Save the PDF document
    doc.save(output_path)

    print(f"PDF file created successfully at: {output_path}")

# Provided text
text = """
* Samsung Galaxy A546 A54 5G 8/128gb graph OEM EAN 8806094891973
* Samsung Galaxy A546 A54 5G 8/128gb violet OEM EAN 8806094891980
* Samsung Galaxy A546 A54 5G 8/128gb lime OEM EAN 8806094891997
* Samsung Galaxy A546 A54 5G 8/128gb white OEM EAN 8806094891966
"""

# Call the function to create the PDF
create_pdf_with_text(text, "output.pdf")
