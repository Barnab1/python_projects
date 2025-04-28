
import json
import os

class DataStorage:
    """
    Base class for data storage.  Defines the interface.
    """
    def __init__(self, filepath, data_type):
        self.filepath = filepath
        self.data_type = data_type  # e.g., "task", "note", etc.

    def save(self, data):
        raise NotImplementedError("Subclasses must implement the save() method.")

    def load(self):
        raise NotImplementedError("Subclasses must implement the load() method.")

class JsonStorage(DataStorage):
    """
    Handles data storage in JSON format.
    """
    def save(self, data):
        try:
            with open(self.filepath, 'w') as file:
                json.dump(data, file)
            print(f'{self.data_type}s saved to {self.filepath}')
        except Exception as e:
            print(f'Error saving {self.data_type}s to {self.filepath}: {e}')

    def load(self):
        data = []
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    data = json.load(file)
                print(f'{self.data_type}s loaded from {self.filepath}')
            except json.JSONDecodeError:
                print(f'Error decoding JSON from {self.filepath}. Starting with an empty list of {self.data_type}s.')
            except Exception as e:
                print(f'Error loading {self.data_type}s from {self.filepath}: {e}. Starting with an empty list.')
        else:
            print(f'No {self.data_type} file found at {self.filepath}. Starting with an empty list.')
        return data

# We could add other storage classes here, e.g., CsvStorage, DatabaseStorage
