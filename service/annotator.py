
import pickle
import json

# Load pickle file
def generate_text_annotator():
    with open('../data/filterd.pkl', 'rb') as file:
        text_data = pickle.load(file)

        # Decode pickled text_data into bytes using 'latin1' encoding
        pickled_bytes = pickle.dumps(text_data)
        
        # Decode bytes into string using 'latin1' encoding
        latin1_text = pickled_bytes.decode('latin1')
        
        # Encode text into UTF-8 encoding
        utf8_text = latin1_text.encode('utf-8')

        # Decode utf-8 bytes to string
        text_data = utf8_text.decode('utf-8')

    # Sample array of brands and colors
    brands = ['Samsung', 'Apple', 'Huawei']
    colors = ['graph', 'violet', 'blue']

    # Function to check if a word exists in the array
    def check_word(word, word_list):
        print(word)
        for item in word_list:
            if item in word:
                print(item,"__________________________")
                return True, item
        return False, None

    # List to store annotations
    annotations = []

    # Split the text into lines
    lines = text_data.splitlines()

    # Iterate over each line
    for idx, line in enumerate(lines):
        # Check for brands
        brand_found, brand = check_word(line, brands)
        # Check for colors
        color_found, color = check_word(line, colors)

        # If brand or color found, create annotation
        if brand_found or color_found:
            # Find the start and end indices of the word in the line
            start_index = text_data.find(line)
            
            if brand_found:
                
                wrod_in_line = line.find(brand)
                start_index_brand = start_index + wrod_in_line
                end_index_brand = start_index_brand + len(brand)

            if color_found:

                wrod_in_line = line.find(color)
                start_index_color = start_index + wrod_in_line
                end_index_color = start_index_color + len(color)

            # Create annotation dictionary
            annotation = {
                "entities": [
                    [start_index_brand, end_index_brand, "BRAND"] if brand_found else None,
                    [start_index_color, end_index_color, "COLOR"] if color_found else None
                ]
            }
            annotations.append([line, annotation])

    # Write annotations to JSON file
    with open('annotations.json', 'w') as f:
        json.dump(annotations, f, indent=4)

    print("Annotations saved to annotations.json")

generate_text_annotator()
