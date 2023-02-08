import pickle

def load_pickle(filepath):
    with open(filepath, 'rb') as f:
        file = pickle.load(f)

    return file