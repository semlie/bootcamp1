
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
    brands = get_brand()
    colors = get_color()

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

            # # Create annotation dictionary
            # annotation = {
            #     "entities": [
            #         [start_index_brand, end_index_brand, "BRAND"] if brand_found else 
            #         [start_index_color, end_index_color, "COLOR"] if color_found else 
            #     ]
            # }
            # annotations.append([line, annotation])
                
            # Create annotation dictionary
            annotation_entities = []
            if brand_found:
                 annotation_entities.append([start_index_brand, end_index_brand, "BRAND"])
            if color_found:
                 annotation_entities.append([start_index_color, end_index_color, "COLOR"])

        # Add the annotation only if at least one entity is found
            if annotation_entities:
                annotation = {"entities": annotation_entities}
                annotations.append([line, annotation])

    # Write annotations to JSON file
    with open('annotations.json', 'w') as f:
        json.dump(annotations, f, indent=4)

    print("Annotations saved to annotations.json")


def get_brand():
    return  [
        "Apple",
        "Samsung",
        "Huawei",
        "Xiaomi",
        "OnePlus",
        "Oppo",
        "Vivo",
        "Google Pixel",
        "Sony Xperia",
        "Motorola",
        "LG",
        "HTC",
        "Nokia",
        "Asus",
        "BlackBerry",
        "Lenovo",
        "ZTE",
        "Meizu",
        "Realme",
        "Honor",
        "Sharp",
        "Panasonic",
        "TCL",
        "Alcatel",
        "LeEco",
        "Ulefone",
        "Elephone",
        "Coolpad",
        "Gionee",
        "Micromax",
        "Infinix",
        "Tecno",
        "iQOO",
        "Redmi",
        "Poco",
        "Itel",
        "Doogee",
        "Cubot",
        "Vernee",
        "Vivo",
        "Umidigi",
        "Wileyfox",
        "Energizer",
        "Razer",
        "Nextbit",
        "Essential",
        "Fairphone",
        "Black Shark",
        "Sharp Aquos",
        "Bluboo",
        "Wiko",
        "Meitu",
        "Vodafone",
        "YotaPhone",
        "Sirin Labs",
        "Vertu",
        "CAT (Caterpillar)",
        "Google Nexus",
        "HP",
        "Dell",
        "Acer",
        "Fujitsu",
        "Toshiba",
        "Kyocera",
        "Casio",
        "NEC",
        "Gigabyte",
        "Panasonic Toughbook",
        "Sonim",
        "RugGear",
        "Doogee",
        "Homtom",
        "F(x)tec",
        "Planet Computers",
        "Jolla",
        "Fairphone",
        "Unihertz",
        "Energizer",
        "NuAns",
        "Punkt",
        "Zebra",
        "Bullitt",
        "Crosscall",
        "Land Rover Explore",
        "Marshall",
        "Palm",
        "Shift Phones",
        "Sugar",
        "Turing",
        "Silent Circle",
        "Saygus",
        "Obi Worldphone",
        "Wileyfox",
        "Archos",
        "bq",
        "Emporia",
        "Gigaset",
        "Hisense",
        "Kodak",
        "Yotaphone"
        ]

def get_color():
    return [
    "Black",
    "White",
    "Silver",
    "Gold",
    "Space Gray",
    "Rose Gold",
    "Midnight Black",
    "Blue",
    "Red",
    "Green",
    "Pink",
    "Purple",
    "Yellow",
    "Coral",
    "Azure",
    "Mystic Bronze",
    "Graphite",
    "Emerald Green",
    "Sunset Orange",
    "Cloud White",
    "Ocean Blue",
    "Cosmic Gray",
    "Aura Glow",
    "Phantom Black",
    "Frost White",
    "Electric Blue",
    "Lavender Purple",
    "Pearl White",
    "Titanium Gray",
    "Platinum",
    "Forest Green",
    "Aurora",
    "Ceramic Black",
    "Royal Blue",
    "Glacier White",
    "Mint Green",
    "Sunrise Red",
    "Sapphire Blue",
    "Burgundy Red",
    "Amber Brown",
    "Carbon Black",
    "Deepsea Blue",
    "Polar White",
    "Sonic Blue",
    "Blush Gold",
    "Alpine Green",
    "Copper",
    "Lunar Gray",
    "Shadow Black",
    "Flamingo Pink",
    "Brilliant Blue",
    "Topaz Blue",
    "Crimson Red",
    "Opal Blue",
    "Lagoon Blue",
    "Ruby Red",
    "Peacock Blue",
    "Ice Blue",
    "Champagne Gold",
    "Moonlight Silver",
    "Marble White",
    "Pearl Black",
    "Crystal Black",
    "Arctic Silver",
    "Rose Pink",
    "Anthracite Gray",
    "Ceramic White",
    "Ruby Pink",
    "Azure Blue",
    "Sunburst Gold",
    "Royal Gold",
    "Phantom Blue",
    "Amethyst Purple",
    "Solar Red",
    "Forest Mist Green",
    "Cloud Blue",
    "Flame Red",
    "Topaz Gold",
    "Rosewood Red",
    "Quartz Pink",
    "Sapphire Black",
    "Metallic Blue",
    "Midnight Blue",
    "Brilliant Black",
    "Peach Gold",
    "Platinum Silver",
    "Pebble Blue",
    "Sunset Gold",
    "Nebula Purple",
    "Arctic Blue",
    "Bordeaux Red",
    "Mocha Brown",
    "Deep Indigo",
    "Carbon Fiber",
    "Fog Gray",
    "Bronze",
    "Cherry Red",
    "Metallic Red"
    ]


generate_text_annotator()
