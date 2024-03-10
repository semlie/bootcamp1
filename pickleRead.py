import pickle
def open_pickle_file(file_path):
  
  # Open the file in binary read mode
  with open(file_path, "rb") as f:
    try:
      # Load the data
      data = pickle.load(f)
      return data
    except EOFError:
      raise IOError("Pickle file is empty.")
    except pickle.UnpicklingError:
      raise IOError("Error unpickling data.")

# Example usage
file_path ="data/filterd.pkl"
data = open_pickle_file(file_path)
# print(f"Loaded data from pickle file: {data}")


def display_dictionaries(data):
    for key, value in data.items():
      print(f"  - {key}: {value}")
      
display_dictionaries(data)
    


    

