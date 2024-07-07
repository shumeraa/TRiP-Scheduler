import os
import pandas as pd
import re

from readTripLeaderStatusSheet import *
from readTripsInfoSheet import *


def readPrefFolder(excelFilePath):
    """ """
    messages = []
    # Check if the file exists
    if os.path.isfile(excelFilePath):
        messages.append("Reading: " + excelFilePath)
        try:
            df = pd.ExcelFile(excelFilePath, engine="openpyxl")

            sheetNames = df.sheet_names
            lowercase_sheetnames = [name.lower() for name in sheetNames]

            if re.search(r"prefs", lowercase_sheetnames[0]):
                prefTemplateIndex = 0
                statusIndex = 1
            elif re.search(r"prefs", lowercase_sheetnames[1]):
                prefTemplateIndex = 1
                statusIndex = 0
            else:
                messages.append(
                    "Error: Could not find a sheet with 'prefs' in the name in TripsAndLeaderStatusInfo."
                )
                return messages

            tripInfoSheet = pd.read_excel(
                excelFilePath, sheet_name=sheetNames[prefTemplateIndex]
            )
            statusSheet = pd.read_excel(
                excelFilePath, sheet_name=sheetNames[statusIndex]
            )

            statusData = readStatusInfo(statusSheet, excelFilePath, messages)
            if statusData is None:
                return messages

            # tripInfoData = readInPrefs(prefsSheet, excelFilePath, messages)
            # if tripInfoData is None:
            #     return False

            messages.append("The file was read successfully.")
            return messages

            # NEED TO HANDLE ERROR IN leaderInfoSheet

        except Exception as e:
            messages.append(
                f"Error: {excelFilePath} could not be read"
                + f" and {os.path.exists(excelFilePath)}. Exception: {str(e)}"
            )

    else:
        messages.append("The directory does not exist.")

    return messages


# Test
output = readPrefFolder(r"Example_Data\TripsAndLeaderStatusInfo.xlsx")
for message in output:
    print(message)
