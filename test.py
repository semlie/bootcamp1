import spacy
import random
import pickle
import re

from spacy.training.example import Example

# Function to load data
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


# Function to train NER model
def train_ner_model(train_data, labels, iterations=100):
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")
    for label in labels:
        ner.add_label(label)

    optimizer = nlp.begin_training()
    for itn in range(iterations):
        random.shuffle(train_data)
        losses = {}
        for text, annotations in train_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], drop=0.5, losses=losses)
        print("Iteration:", itn + 1, "Loss:", losses)
    return nlp

# Example usage
if __name__ == "__main__":
    # Load training data (replace with your labeled data)
    train_data = [
        ("I like the iPhone.", {"entities": [(10, 16, "SMARTPHONE")]}),
        ("Samsung Galaxy is popular.", {"entities": [(0, 14, "SMARTPHONE")]}),
        ("The Google Pixel has a great camera.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("I'm excited about the new OnePlus release.", {"entities": [(21, 28, "SMARTPHONE")]}),
        ("The Huawei P40 is launching soon.", {"entities": [(4, 12, "SMARTPHONE")]}),
        ("I need to upgrade my LG phone.", {"entities": [(22, 24, "SMARTPHONE")]}),
        ("The Motorola Edge+ has impressive specs.", {"entities": [(4, 20, "SMARTPHONE")]}),
        ("The iPhone 12 Pro Max is too expensive for me.", {"entities": [(4, 18, "SMARTPHONE")]}),
        ("I prefer using my Google Pixel over other phones.", {"entities": [(15, 27, "SMARTPHONE")]}),
        ("OnePlus Nord offers great value for its price.", {"entities": [(0, 10, "SMARTPHONE")]}),
        ("The Samsung Galaxy Note series is known for its large displays.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Google Pixel 5 has an amazing camera.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The Huawei Mate 40 Pro features a curved display.", {"entities": [(4, 18, "SMARTPHONE")]}),
        ("I'm waiting for the new iPhone SE to be released.", {"entities": [(16, 23, "SMARTPHONE")]}),
        ("The OnePlus 9 Pro has a smooth 120Hz display.", {"entities": [(4, 14, "SMARTPHONE")]}),
        ("The Samsung Galaxy S21 Ultra offers top-of-the-line specs.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Google Pixel 6 is rumored to have a new processor.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The Xiaomi Mi 11 has received positive reviews from critics.", {"entities": [(4, 14, "SMARTPHONE")]}),
        ("I'm considering buying the Sony Xperia 1 III.", {"entities": [(22, 35, "SMARTPHONE")]}),
        ("The Realme GT 5G offers flagship-level performance at an affordable price.", {"entities": [(4, 14, "SMARTPHONE")]}),
        ("The Oppo Find X3 Pro has a unique design.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The Vivo X60 Pro+ is equipped with a powerful camera setup.", {"entities": [(4, 17, "SMARTPHONE")]}),
        ("The ASUS ROG Phone 5 is tailored for gaming enthusiasts.", {"entities": [(4, 17, "SMARTPHONE")]}),
        ("The Motorola Moto G Power has a long-lasting battery.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The LG Velvet offers a stylish design and good performance.", {"entities": [(4, 12, "SMARTPHONE")]}),
        ("The iPhone SE (2020) is a budget-friendly option from Apple.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The Samsung Galaxy A52 5G is a mid-range smartphone with 5G connectivity.", {"entities": [(4, 23, "SMARTPHONE")]}),
        ("The Google Pixel 4a is praised for its excellent camera performance.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The OnePlus 8T features a fast-charging technology.", {"entities": [(4, 12, "SMARTPHONE")]}),
        ("The Xiaomi Redmi Note 10 Pro offers great value for money.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Sony Xperia 5 II is known for its compact size and high-quality display.", {"entities": [(4, 20, "SMARTPHONE")]}),
        ("The Realme X50 Pro 5G is equipped with a Snapdragon 865 chipset.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The Oppo Reno 5 Pro 5G features a sleek design and impressive camera capabilities.", {"entities": [(4, 18, "SMARTPHONE")]}),
        ("The Vivo V20 Pro offers a versatile camera setup for photography enthusiasts.", {"entities": [(4, 13, "SMARTPHONE")]}),
        ("The ASUS Zenfone 8 Flip comes with a flip camera module for versatile photography.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Motorola Moto E7 Plus is an entry-level smartphone with a large battery.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The LG Wing has a unique swivel display design.", {"entities": [(4, 12, "SMARTPHONE")]}),
        ("The iPhone XR is still a popular choice among Apple fans.", {"entities": [(4, 12, "SMARTPHONE")]}),
        ("The Samsung Galaxy M51 offers a massive 7000mAh battery.", {"entities": [(4, 20, "SMARTPHONE")]}),
        ("The Google Pixel 3a is known for its exceptional camera quality at a lower price point.", {"entities": [(4, 16, "SMARTPHONE")]}),
        ("The OnePlus Nord N10 5G brings 5G connectivity to a budget-friendly smartphone.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Xiaomi Poco X3 NFC offers impressive performance at an affordable price.", {"entities": [(4, 15, "SMARTPHONE")]}),
        ("The Sony Xperia 10 III features a sleek design and a 6-inch OLED display.", {"entities": [(4, 17, "SMARTPHONE")]}),
        ("The Realme Narzo 30 Pro 5G is a mid-range smartphone with 5G support.", {"entities": [(4, 21, "SMARTPHONE")]}),
        ("The Oppo A74 5G offers 5G connectivity at an affordable price point.", {"entities": [(4, 13, "SMARTPHONE")]}),
    ]
    

    
    # # Define the labels
    # labels = ["SMARTPHONE"]

    # # Train the NER model
    # ner_model = train_ner_model(train_data, labels)

    # # Save the trained model
    # ner_model.to_disk("smartphone_ner_model")

    # # Test the model
    # test_text = "The new iPhone was announced."
    # doc = ner_model(test_text)
 
        # Load the trained NER model
    ner_model = spacy.load("smartphone_ner_model")

    # Sample text to check
    data = extract_data()
    text = ' '.join(data)
  

    # Process the text with the NER model
    doc = ner_model(text)

    
    # Extract and print the predicted entities
 
    NER_RESULT = doc.text
    print(NER_RESULT)






