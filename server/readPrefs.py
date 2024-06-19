
import os
import pandas as pd

def readPrefFolder(prefsDirectoryPath):
    messages = []
    # Check if the directory exists
    if os.path.isdir(prefsDirectoryPath):
        # Check if the directory contains at least one file
        if any(os.listdir(prefsDirectoryPath)):
            for file in os.listdir(prefsDirectoryPath):
                if file.endswith(".xlsx"):
                    messages.append("Reading file: " + file)
                    readPrefFile(os.path.join(prefsDirectoryPath, file), messages)
                else:
                    messages.append("The file is not an Excel file.")
                    
            messages.append("All files have been read.")
        else:
            messages.append("The directory is empty.")
    else:
        messages.append("The directory does not exist.")
    
    return messages
        
        
        
def readPrefFile(prefFilePath, messages):
    try:
        df = pd.read_excel(prefFilePath)
        messages.append("The file was read successfully.")
        #STUCK HERE
    except:
        messages.append(f"Error: {prefFilePath} could not be read and {os.path.exists(prefFilePath)}.")
        
# Test
print(readPrefFolder("Example_Data\prefs"))