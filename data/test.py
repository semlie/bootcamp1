import pickle

try:
    with open("/filterd.pkl", "rb") as f:
        data_structure = pickle.load(f)

    print(type(data_structure))  # Check the type of the loaded object
    print(data_structure)  # Print the object's representation

except (FileNotFoundError, PermissionError) as e:
    print("Error opening or loading the file:", e)

