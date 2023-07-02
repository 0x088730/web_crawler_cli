import pickle
import json

class Memento:
    def __init__(self, path):
        self.path = path


    def pickle_save(self, state):
        with open(f"{self.path}.pkl", "wb") as f:
            pickle.dump(state, f)
            print(f"\n\U0001F4BE Saved state to {self.path}.pkl")


    def pickle_load(self):
        try:
            with open(f"{self.path}.pkl", "rb") as f:
                print(f"\n\U0001F4BE Loaded state from {self.path}.pkl")
                return pickle.load(f)
        
        except Exception:
            print(f"\n\U0001F6AB\tThe following file does not exist:\n{self.path}.pkl")
            return False




    def json_save(self, state):
        with open(f"{self.path}.json", "w") as f:
            json.dump(state, f)
            print(f"\n\U0001F4BE Saved state to {self.path}.json")


    def json_load(self):
        try:
            with open(f"{self.path}.json", "r") as f:
                loaded_state = json.load(f)
            print(f"\n\U0001F4BE Loaded state from:\n{self.path}.json")
            return loaded_state

                
        except Exception as ex:
            print(f"\n\U0001F6AB\tThe following file does not exist:\n{self.path}.json\n{ex}")
            return False
                



    def display(self, state):
        for key, value in state.items():
            if isinstance(value, list):
                print(f"\n{key}:")
                for link in value:
                    print(f"{link}")
            else:
                print(key, value)
