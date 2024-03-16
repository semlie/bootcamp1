import pickle
import json
import re

# Function to get brands from file
def get_brand():
    with open('../data/brands.txt', 'r') as file:
        brands = [line.strip() for line in file]
    return brands

# Function to get colors from file
def get_color():
    with open('../data/colors.txt', 'r') as file:
        colors = [line.strip() for line in file]
    return colors

# Function to get countries from file
def get_country():
    with open('../data/countries.txt', 'r') as file:
        countries = [line.strip() for line in file]
    return countries

# Function to get smartphone models from file
def get_smartphone_models():
    with open('../data/models.txt', 'r') as file:
        models = [line.strip() for line in file]
    return models

# Function to check if a word exists in the array
def check_word(word, word_list):
    for item in word_list:
        if item in word:
            return True, item
    return False, None

# Function to check if a word is a smartphone model
def check_smartphone_model(word, model_list):
    for model in model_list:
        if model.lower() in word.lower():
            return True, model
    return False, None

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

    # Sample array of brands, colors, countries, and smartphone models
    brands = get_brand()
    colors = get_color()
    countries = get_country()
    smartphone_models = get_smartphone_models()

    # List to store annotations
    annotations = []

    # Split the text into lines
    lines = text_data.splitlines()

    # Keywords for buy and sale status
    buy_keywords = ["buy", "purchase", "acquire", "BUY", "PURCHASE", "ACQUIRE"]
    sale_keywords = ["sell", "sale", "offer", "SELL", "SALE", "OFFER"]

    # Iterate over each line
    for idx, line in enumerate(lines):
        # Check for brands, colors, prices, countries, status, and smartphone models
        brand_found, brand = check_word(line, brands)
        color_found, color = check_word(line, colors)
        price_found = re.search(r'\d+\s*(?:USD|EUR|GBP|CAD|AUD|JPY)', line)
        country_found, country = check_word(line, countries)
        model_found, model = check_smartphone_model(line, smartphone_models)
        status = None
        for word in line.split():
            if word.lower() in buy_keywords:
                status = "BUY"
            elif word.lower() in sale_keywords:
                status = "SALE"

        # If brand, color, price, country, status, or model found, create annotation
        if brand_found or color_found or price_found or country_found or status or model_found:
            # Find the start and end indices of the word in the line
            start_index = text_data.find(line)
            
            annotation_entities = []
            if brand_found:
                word_in_line = line.find(brand)
                start_index_entity = word_in_line
                end_index_entity = start_index_entity + len(brand)
                annotation_entities.append([start_index_entity, end_index_entity, "BRAND"])
                
            if color_found:
                word_in_line = line.find(color)
                start_index_entity = word_in_line
                end_index_entity = start_index_entity + len(color)
                annotation_entities.append([start_index_entity, end_index_entity, "COLOR"])

            if price_found:
                start_index_entity = line.find(price_found.group())
                end_index_entity = start_index_entity + len(price_found.group())
                annotation_entities.append([start_index_entity, end_index_entity, "PRICE"])

            if country_found:
                word_in_line = line.find(country)
                start_index_entity = word_in_line
                end_index_entity = start_index_entity + len(country)
                annotation_entities.append([start_index_entity, end_index_entity, "COUNTRY"])

            if model_found:
                word_in_line = line.lower().find(model.lower())
                start_index_entity = word_in_line
                end_index_entity = start_index_entity + len(model)
                annotation_entities.append([start_index_entity, end_index_entity, "MODEL"])

            if status:
                start_index_entity = line.lower().find(status.lower())
                end_index_entity = start_index_entity + len(status)
                annotation_entities.append([start_index_entity, end_index_entity, "STATUS"])

            # Add the annotation only if at least one entity is found
            if annotation_entities:
                annotation = {"entities": annotation_entities}
                annotations.append([line, annotation])

    # Write annotations to JSON file
    with open('annotations.json', 'w') as f:
        json.dump(annotations, f, indent=4)

    print("Annotations saved to annotations.json")

# Generate text annotations
generate_text_annotator()
