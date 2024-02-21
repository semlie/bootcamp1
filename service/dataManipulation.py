import pickle
import re


def extract_data():
    with open('data/filterd.pkl', 'rb') as file:
        data = pickle.load(file)

    # Decode pickled data into bytes using 'latin1' encoding
    pickled_bytes = pickle.dumps(data)
    
    # Decode bytes into string using 'latin1' encoding
    latin1_text = pickled_bytes.decode('latin1')
    
    # Encode text into UTF-8 encoding
    utf8_text = latin1_text.encode('utf-8')

    # Decode utf-8 bytes to string
    text = utf8_text.decode('utf-8')

    # Write the text to a file
    with open('filterd', 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

def create_smart_phone_list():

    text = extract_data()

    # Define a regular expression pattern to match smartphone names
    pattern = r'\b[A-Z][a-zA-Z0-9\s-]+\b'

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # Filter out common words that are not smartphone names
    filtered_matches = [match for match in matches if len(match) > 3]

    # Create a list of dictionaries to hold the extracted smartphone names with IDs
    smartphone_list = []
    
    # Assign IDs to filtered matches and store them in the list of dictionaries
    for idx, name in enumerate(filtered_matches, start=1):
        smartphone_list.append({"id": idx, "brand": name})

    return smartphone_list



def clean_smartphone_list():

    smartphone_list = create_smart_phone_list()

    cleaned_smartphone_list = []
    for smartphone in smartphone_list:
        cleaned_brand = smartphone['brand']
        # Remove \n
        cleaned_brand = re.sub(r'\n', '', cleaned_brand)
        # Remove \r
        cleaned_brand = re.sub(r'\r', '', cleaned_brand)
        # Remove \t
        cleaned_brand = re.sub(r'\t', '', cleaned_brand)
        # Remove numbers with more than 3 digits
        cleaned_brand = re.sub(r'\b\d{4,}\b', '', cleaned_brand)
        
        cleaned_smartphone_list.append({"id": smartphone["id"], "brand": cleaned_brand})
    return cleaned_smartphone_list

