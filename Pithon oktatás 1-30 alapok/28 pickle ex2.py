import pickle

with open('data.pickle', 'rb') as file:
    data = pickle.load(file)
    print(data)