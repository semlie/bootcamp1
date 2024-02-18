import pickle

# Open the pickle file in binary mode
with open('filterd.pkl', 'rb') as file:
    # Load the pickled object
    obj = pickle.load(file)

# Now 'obj' holds the object that was stored in the pickle file
print(obj)
