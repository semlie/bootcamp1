
import pickle



def extract_data():
    with open('data/filterd.pkl', 'rb') as file:
        data = pickle.load(file)

    #  Serialize Object to String
    return pickle.dumps(data).decode('latin1')  # Convert bytes to string





def get_brands_names():

    return  [
    "Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Huawei", "Sony", "LG", "Motorola", "Nokia",
    "Asus", "HTC", "BlackBerry", "Lenovo", "ZTE", "OPPO", "Vivo", "Realme", "TCL", "Alcatel",
    "Honor", "Meizu", "Infinix", "Oukitel", "Doogee", "Ulefone", "Cat", "Fairphone", "Sharp", "Wiko",
    "LeEco", "Razer", "Essential", "Micromax", "Yota", "Xolo", "Gionee", "Symphony", "Lava", "Tecno",
    "Blackview", "Umidigi", "Cubot", "Elephone", "Nubia", "ZUK", "Coolpad", "Hisense", "Karbonn",
    "Intex", "Swipe", "Spice", "iBall", "Celkon", "Kult", "Lemon", "Videocon", "Maxx", "Kenxinda",
    "Haier", "Gfive", "ThL", "Jiayu", "Zopo", "Obi", "Kazam", "Plum", "BLU", "Walton", "MyPhone"
]



def extract_products():
    text = extract_data()
    brands = get_brands_names()  # Assuming extract_data() retrieves the text containing product information
    products = []
    current_product = {}
    words = text.split()
    for i, word in enumerate(words):
        if word.isdigit():  # Check if the word is a number (assumed to be the price)
            try:
                price = float(word)
                if 100 <= price <= 10000:  # Check if the price falls within the desired range
                    if 'brand' in current_product:  # If there's a brand associated with the current product
                        current_product['price'] = price  # Set the price
                        # Check if the brand is in the list of smartphone brands
                        if current_product['brand'] in brands:
                            products.append(current_product.copy())  # Append a copy of current_product
                        current_product = {}  # Reset the current product dictionary
            except ValueError:
                # Handle the case where the word contains characters that can't be interpreted as a number
                pass
        elif any(char.isdigit() for char in word):  # Check if the word contains any digits
            if 'brand' in current_product:  # If there's a brand associated with the current product
                current_product['brand'] += ' ' + word  # Append the word to the brand name
            else:  # If there's no brand associated with the current product
                # Check if the word is a known smartphone brand
                if word in brands:
                    current_product['brand'] = word  # Assume the word is the brand name
        else:
            if i + 1 < len(words) and words[i + 1].isdigit():  # Check if the next word is a price
                current_product['brand'] = word
            else:  # If the next word is not a price, assume it's part of the brand name
                current_product['brand'] = current_product.get('brand', '') + ' ' + word
    return products

