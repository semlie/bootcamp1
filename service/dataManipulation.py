
# import pickle



# def extract_data():
#     with open('data/filterd.pkl', 'rb') as file:
#         data = pickle.load(file)

#     #  Serialize Object to String
#     return pickle.dumps(data).decode('latin1')  # Convert bytes to string





# def get_brands_names():

#     return  [
#     "Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Huawei", "Sony", "LG", "Motorola", "Nokia",
#     "Asus", "HTC", "BlackBerry", "Lenovo", "ZTE", "OPPO", "Vivo", "Realme", "TCL", "Alcatel",
#     "Honor", "Meizu", "Infinix", "Oukitel", "Doogee", "Ulefone", "Cat", "Fairphone", "Sharp", "Wiko",
#     "LeEco", "Razer", "Essential", "Micromax", "Yota", "Xolo", "Gionee", "Symphony", "Lava", "Tecno",
#     "Blackview", "Umidigi", "Cubot", "Elephone", "Nubia", "ZUK", "Coolpad", "Hisense", "Karbonn",
#     "Intex", "Swipe", "Spice", "iBall", "Celkon", "Kult", "Lemon", "Videocon", "Maxx", "Kenxinda",
#     "Haier", "Gfive", "ThL", "Jiayu", "Zopo", "Obi", "Kazam", "Plum", "BLU", "Walton", "MyPhone"
# ]



# def extract_products():
#     text = extract_data()
#     brands = get_brands_names()  # Assuming extract_data() retrieves the text containing product information
#     products = []
#     current_product = {}
#     words = text.split()
#     for i, word in enumerate(words):
#         if word.isdigit():  # Check if the word is a number (assumed to be the price)
#             try:
#                 price = float(word)
#                 if 100 <= price <= 10000:  # Check if the price falls within the desired range
#                     if 'brand' in current_product:  # If there's a brand associated with the current product
#                         current_product['price'] = price  # Set the price
#                         # Check if the brand is in the list of smartphone brands
#                         if current_product['brand'] in brands:
#                             products.append(current_product.copy())  # Append a copy of current_product
#                         current_product = {}  # Reset the current product dictionary
#             except ValueError:
#                 # Handle the case where the word contains characters that can't be interpreted as a number
#                 pass
#         elif any(char.isdigit() for char in word):  # Check if the word contains any digits
#             if 'brand' in current_product:  # If there's a brand associated with the current product
#                 current_product['brand'] += ' ' + word  # Append the word to the brand name
#             else:  # If there's no brand associated with the current product
#                 # Check if the word is a known smartphone brand
#                 if word in brands:
#                     current_product['brand'] = word  # Assume the word is the brand name
#         else:
#             if i + 1 < len(words) and words[i + 1].isdigit():  # Check if the next word is a price
#                 current_product['brand'] = word
#             else:  # If the next word is not a price, assume it's part of the brand name
#                 current_product['brand'] = current_product.get('brand', '') + ' ' + word
#     return text

import pickle
import spacy
import re

# Define a list of common smartphone keywords

# Load the spaCy English language model

        # Load the trained NER model
ner_model = spacy.load("smartphone_ner_model")

# def extract_smartphone_names(text):
#     # Create an empty set to store smartphone names
#     smartphone_names = set()
#     print("before LNP1")
#     # Process the text using the spaCy language model
#     t= "The iPhone 12 Pro Max is a flagship smartphone produced by Apple Inc. It features a stunning 6.7-inch Super Retina XDR display and is powered by the A14 Bionic chip. The Samsung Galaxy S21 Ultra, on the other hand, boasts a massive 108MP camera and supports 8K video recording. Both of these smartphones offer cutting-edge technology and premium features."

#     doc = nlp(t)
    
#     # Iterate over the entities recognized in the processed text
#     for ent in doc.ents:
#         # Check if the entity label is "PRODUCT"
#         if ent.label_ == "PRODUCT":
#             # If it is, add the text of the entity to the set of smartphone names
#             smartphone_names.add(ent.text)
    
#     # Return the set of smartphone names
#     print(smartphone_names,"smartphone_names")
#     return smartphone_names


# def extract_smartphone_names(text):
#     smartphone_names = set()

#     doc = nlp(text)
#     print(doc.ents,"doc.ents")

#     # Extract smartphone names recognized by spaCy NER
#     for ent in doc.ents:
#         if ent.label_ == "PRODUCT":
#             smartphone_names.add(ent.text)

#     # Add additional smartphone names using regular expressions and keyword matching
#     for keyword in SMARTPHONE_KEYWORDS:
#         pattern = r'\b{}\b'.format(re.escape(keyword))
#         matches = re.findall(pattern, text, flags=re.IGNORECASE)
#         smartphone_names.update(matches)
#     return smartphone_names



# def extract_data():
#     with open('data/filterd.pkl', 'rb') as file:
#         data = pickle.load(file)
#     # Serialize Object to String
#     return pickle.dumps(data).decode('latin1')  # Convert bytes to string

# def extract_products():
#     text = extract_data()
    
#     # Store the original max_length
#     original_max_length = nlp.max_length
    
#     # Increase max_length temporarily
#     nlp.max_length = len(text) + 100000  # You can adjust this value as needed
    
#     smartphone_names = extract_smartphone_names(text)
    
#     # Reset max_length to the original value
#     nlp.max_length = original_max_length

#     print(smartphone_names,"smartphone_names")
    
#     products = []
#     current_product = {}
#     words = text.split()
#     for i, word in enumerate(words):
        
#         if word.isdigit():  
#             try:
#                 price = float(word)
#                 if 100 <= price <= 10000:
#                     if 'brand' in current_product:
#                         current_product['price'] = price
#                         if current_product['brand'] in smartphone_names:  
#                             products.append(current_product.copy())  
#                         current_product = {}  
#             except ValueError:
#                 pass
#         elif any(char.isdigit() for char in word):  
#             if 'brand' in current_product:
#                 current_product['brand'] += ' ' + word
#             else:
#                 if word in smartphone_names:
#                     current_product['brand'] = word
#         else:
#             if i + 1 < len(words) and words[i + 1].isdigit():
#                 current_product['brand'] = word
#             else:
#                 current_product['brand'] = current_product.get('brand', '') + ' ' + word
#     return products









def extract_smartphone_names(text):
    smartphone_names = set()

    # doc = nlp(text)
    

    # # Extract smartphone names recognized by spaCy NER
    # for ent in doc.ents:
    #     if ent.label_ == "PRODUCT":
    #         smartphone_names.add(ent.text)
    #         print(smartphone_names)
    doc = ner_model(text)

    
    # Extract and print the predicted entities
    for ent in doc.ents:
        smartphone_names.add(ent.text)
        
    print(smartphone_names)
    return smartphone_names

def extract_data():
    with open('data/filterd.pkl', 'rb') as file:
        data = pickle.load(file)
    # Serialize Object to String
    text = pickle.dumps(data).decode('latin1')
   
    filtered_words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    # Remove repeated words by converting to a set and back to a list
    filtered_words = list(set(filtered_words))

  

    return filtered_words
     # Convert bytes to string



def smart_phone_brands():
    data = extract_data()
    text = ' '.join(data)
    print(text)
    
   
    return ' '.join(extract_smartphone_names(text))
   
    # chunk_size = 1000000
    # for i in range (0, len(text), chunk_size):
    #     print(extract_smartphone_names(text[i:i+chunk_size]))
    #     print(i+chunk_size)



    # return text
    # chunk_size = 200  # Adjust chunk size as needed
    # products = []
    # print(len(text))
    # for i in range(0, int(100), chunk_size):
    #     chunk = text[i:i+chunk_size]
    #     print(i+chunk_size)
    #     smartphone_names =
    #     if smartphone_names:
    #          products.append(smartphone_names)
    #          print("check--> \n ",i)
     
    # print(products)
        
    

def extract_products():
   return smart_phone_brands()

# def extract_products():
#     text = extract_data()
#     chunk_size = 200  # Adjust chunk size as needed
#     products = []

#     for i in range(0, len(text), chunk_size):
#         chunk = text[i:i+chunk_size]
#         smartphone_names = extract_smartphone_names(chunk)
       
#         current_product = {}
#         words = chunk.split()
#         for i, word in enumerate(words):
#             if word.isdigit():
#                 try:
#                     price = float(word)
#                     if 100 <= price <= 10000:
#                         if 'brand' in current_product and current_product['brand'] in smartphone_names:
#                             current_product['price'] = price
#                             products.append(current_product.copy())
#                         current_product = {}
#                 except ValueError:
#                     pass
#             elif any(char.isdigit() for char in word):
#                 if 'brand' in current_product:
#                     current_product['brand'] += ' ' + word
#                 else:
#                     if word in smartphone_names:
#                         current_product['brand'] = word
#             else:
#                 if i + 1 < len(words) and words[i + 1].isdigit():
#                     current_product['brand'] = word
#                 else:
#                     current_product['brand'] = current_product.get('brand', '') + ' ' + word
    
#     return products
