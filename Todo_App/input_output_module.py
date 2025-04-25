#input_output_module.py
import json, os 

class InputOutputModule:
    """
        This module is responsible for file loading ans saving
    """
    def __init__(self,filePath,informationType):
        
        self.filePath = filePath
        self.informationType = informationType


    def save(self,informationsObject):
        """
        Write iformation object to a file
        """
        try:
            with open(self.filePath, 'w+') as file:
                json.dump(informationsObject, file)
                print(f'{self.informationType} saved to {self.filePath}')
        except Exception as e:
            print(f'Error saving your {self.informationType} object {e}')


    def load(self):
        """
        return the loaded informations list (or an empty list if the file doesn't exist or there's an error).
        """
        informations = []
        if os.path.exists(self.filePath):
            try:
                with open(self.filePath, "r") as file:
                    informations = json.load(file)
                print(f'Informations loaded from {self.filePath}')
            except json.JSONDecodeError:
                print(f'Error decoding JSON from {self.filePath}. Starting with an empty list')
            except Exception as e:
                print(f'Error while loading file : {e}. Starting with an empty list')
        else:
            print('File not found. Starting with an empty list')

        return informations

