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

    # Flatten the text by removing numbers and words with uppercase letters
  

# Define a regular expression pattern to match smartphone names
    pattern = r'\b[A-Z][a-zA-Z0-9\s-]+\b'

    # Find all matches of the pattern in the text
    matches = re.findall(pattern, text)

    # Filter out common words that are not smartphone names
    filtered_matches = [match for match in matches if len(match) > 3]

    # Output the extracted smartphone names
    for name in filtered_matches:
        print(name)
    return name


