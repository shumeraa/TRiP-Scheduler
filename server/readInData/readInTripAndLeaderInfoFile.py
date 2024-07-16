import os
import pandas as pd
import re

from readLeadersStatusSheet import *
from readTripInfoSheet import *


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

            firstSheetName = r"trip info"  # keep lowercase

            if re.search(firstSheetName, lowercase_sheetnames[0]):
                tripInfoIndex = 0
                tripLeaderInfoIndex = 1
            elif re.search(firstSheetName, lowercase_sheetnames[1]):
                tripInfoIndex = 1
                tripLeaderInfoIndex = 0
            else:
                messages.append(
                    "Error: Could not find a sheet with 'Trip Info' in the name in TripsAndLeaderStatusInfo."
                )
                return messages

            tripInfoSheet = pd.read_excel(
                excelFilePath, sheet_name=sheetNames[tripInfoIndex]
            )
            tripLeaderInfo = pd.read_excel(
                excelFilePath, sheet_name=sheetNames[tripLeaderInfoIndex]
            )

            statusData = readStatusInfo(tripLeaderInfo, excelFilePath, messages)
            if statusData is None:
                return messages

            tripInfoData = readTripInfo(tripInfoSheet, excelFilePath, messages)
            if tripInfoData is None:
                return messages

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
