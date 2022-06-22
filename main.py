import pickle

def load_model():
    filename = "models/decision_tree.pkl"
    model = pickle.load(open(filename, 'rb'))
    return model

if __name__ == "__main__":
    model = load_model()
    print(model)