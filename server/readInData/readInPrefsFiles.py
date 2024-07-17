import os
import pandas as pd
import re

from readPrefsTripLeaderInfoSheet import *
from readPrefsSheet import *


def readPrefFolder(prefsDirectoryPath):
    """
    Reads preference files from a specified directory and logs the process.

    This function iterates over all files in a given directory path, filtering for Excel files (excluding temporary files),
    and attempts to read them using the readPrefFile function. It logs each attempt and outcome to a list of messages,
    including whether the directory exists, is empty, or if all files have been successfully read. If the readPrefFile
    function returns False for any file, the process is halted, and the current state of messages is returned.
    
    Parameters:
    - prefsDirectoryPath (str): The path to the directory containing preference files.

    Returns:
    - list: A list of messages indicating the status of each file read attempt, as well as overall process outcomes.
    """
    messages = []
    # Check if the directory exists
    if os.path.isdir(prefsDirectoryPath):
        # Check if the directory contains at least one file
        if any(os.listdir(prefsDirectoryPath)):
            for file in os.listdir(prefsDirectoryPath):
                if not file.startswith("~") and file.endswith(".xlsx"):
                    messages.append("Reading file: " + file)
                    readPrefFile(os.path.join(prefsDirectoryPath, file), messages)
                    if readPrefFile is False:
                        return messages

            messages.append("All files have been read.")
        else:
            messages.append("The directory is empty.")
    else:
        messages.append("The directory does not exist.")

    return messages


def readPrefFile(prefFilePath, messages):
    """
    Reads preference and leader information from a specified Excel file.

    This function attempts to read an Excel file specified by prefFilePath, identifying and processing two key sheets:
    one containing preferences and the other containing leader information. The function determines the correct sheets
    based on their names, expecting one to contain "prefs" and the other to be implicitly treated as the leader info sheet.
    It then reads these sheets into DataFrames, processes them using readInTripLeaderInfo and readInPrefs functions,
    and updates a list of messages with the status of the operation. If any step fails, the function returns False,
    indicating an unsuccessful read operation.

    Parameters:
    - prefFilePath (str): The path to the Excel file to be read.
    - messages (list): A list to which status messages and errors will be appended.

    Returns:
    - bool: True if the file was read and processed successfully, False otherwise.

    Raises:
    - Exception: Captures and logs any exception that occurs during the file reading process, appending the error message
                 to the messages list along with a check if the file exists.
    """
    try:
        df = pd.ExcelFile(prefFilePath, engine="openpyxl")

        sheetNames = df.sheet_names
        lowercase_sheetnames = [name.lower() for name in sheetNames]

        if re.search(r"prefs", lowercase_sheetnames[0]):
            prefsIndex = 0
            leaderInfoIndex = 1
        elif re.search(r"prefs", lowercase_sheetnames[1]):
            prefsIndex = 1
            leaderInfoIndex = 0
        else:
            messages.append(f"Error: Could not find a sheet with 'prefs' in the name in {prefFilePath}.")
            return False

        prefsSheet = pd.read_excel(prefFilePath, sheet_name=sheetNames[prefsIndex])
        leaderInfoSheet = pd.read_excel(
            prefFilePath, sheet_name=sheetNames[leaderInfoIndex]
        )

        leaderInfoData = readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages)
        if leaderInfoData is None:
            return False

        prefsInfoData = readInPrefs(prefsSheet, prefFilePath, messages)
        if prefsInfoData is None:
            return False

        # TODO: read in info sheet

        messages.append("The file was read successfully.")
        return True

        # NEED TO HANDLE ERROR IN leaderInfoSheet

    except Exception as e:
        messages.append(
            f"Error: {prefFilePath} could not be read"
            + f" and {os.path.exists(prefFilePath)}. Exception: {str(e)}"
        )


# Test
output = readPrefFolder(r"Example_Data\prefs")
for message in output:
    print(message)

""" 
RULES:

TODO: Clear database before adding new data

"""