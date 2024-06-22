import os

from readPrefsTripLeaderInfo import *
from readPrefs import *


def readPrefFolder(prefsDirectoryPath):
    messages = []
    # Check if the directory exists
    if os.path.isdir(prefsDirectoryPath):
        # Check if the directory contains at least one file
        if any(os.listdir(prefsDirectoryPath)):
            for file in os.listdir(prefsDirectoryPath):
                if not file.startswith("~") and file.endswith(".xlsx"):
                    messages.append("Reading file: " + file)
                    readPrefFile(os.path.join(prefsDirectoryPath, file), messages)
                # else:
                # messages.append("The file is not an Excel file.")
                # commented out because of temp files

            messages.append("All files have been read.")
        else:
            messages.append("The directory is empty.")
    else:
        messages.append("The directory does not exist.")

    return messages


def readPrefFile(prefFilePath, messages):
    try:
        df = pd.ExcelFile(prefFilePath, engine="openpyxl")

        sheetNames = df.sheet_names
        lowercase_sheetnames = [name.lower() for name in sheetNames]

        if re.search(r"prefs", lowercase_sheetnames[0]):
            prefsIndex = 0
            leaderInfoIndex = 1
        else:
            prefsIndex = 1
            leaderInfoIndex = 0

        prefsSheet = pd.read_excel(prefFilePath, sheet_name=sheetNames[prefsIndex])
        leaderInfoSheet = pd.read_excel(
            prefFilePath, sheet_name=sheetNames[leaderInfoIndex]
        )

        leaderInfoData = readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages)
        prefsInfoData = readInPrefs(prefsSheet, prefFilePath, messages)

        messages.append("The file was read successfully.")

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

# RULES:
# it can only read xlsx files
# there can only be two sheets in the prefs file
# the prefs sheet has "prefs" in the name, the trip leader info does not have "prefs" in the name
# the first non-empty column in the trip leader info sheet must
