import re
import pandas as pd


def readStatusInfo(statusInfoSheet, statusFilePath, messages):
    """ """
    try:
        # Find the row and column with the value "uf" (as in UF ID) in the first 5 rows of every column until found
        foundStatus = False
        ufID_Col = None
        ufID_Row = None
        for column in statusInfoSheet.columns:
            if foundStatus:
                break
            for row in range(5):
                cell_value = str(statusInfoSheet.at[row, column])
                if re.search(
                    r"uf", cell_value, re.IGNORECASE
                ):  # Use regex for case-insensitive search
                    ufID_Col = statusInfoSheet.columns.get_loc(
                        column
                    )  # Get the column index
                    ufID_Row = row
                    foundStatus = True  # Exit the row loop
                    break

        if ufID_Col is None or ufID_Row is None:
            messages.append(
                f"Error: The Trip Leader Status sheet in {statusFilePath} does "
                + "not contain a column with 'uf' in the first 5 rows."
            )
            return None

        colHeaders = ufID_Col + 1  # to skip ufID
        colToHeaderDict = {}

        while not pd.isnull(statusInfoSheet.iloc[ufID_Row, colHeaders]):
            colToHeaderDict[colHeaders] = statusInfoSheet.iloc[ufID_Row, colHeaders]
            colHeaders += 1

        statusDict = {}
        currentRow = ufID_Row + 1  # Skip the row with the headers
        # Go through every row, and stop when the ufID is empty
        while not pd.isnull(statusInfoSheet.iloc[currentRow, ufID_Col]):
            tripLeaderStatusDict = {}

            # Go through every column and assign the values from the row to the dictionary
            for colNum, colName in colToHeaderDict.items():
                tripLeaderStatusDict[colName] = statusInfoSheet.iloc[currentRow, colNum]

            # Add the dictionary to the status dictionary
            # The key is the UF ID, the value is the dictionary of the trip leader's status
            statusDict[statusInfoSheet.iloc[currentRow, ufID_Col]] = (
                tripLeaderStatusDict
            )

            currentRow += 1

        return statusDict

    except Exception as e:
        messages.append(
            "Error: The trip leader prefs could not be read for "
            + f"{statusFilePath}. Exception: {str(e)}"
        )


# UF ID needs to be the column in Trip Leader info sheet
