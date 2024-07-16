import re
import pandas as pd
from datetime import datetime


def readTripInfo(tripsInfoSheet, infoFilePath, messages):
    templateInfoCols = [
        "trip",
        "start date",
        "end date",
        "trip category",
        "# of total guides needed",
        "# of lead guides needed",
    ]

    optionalCols = ["end date"]

    try:
        tripRow = 0
        tripCol = 1

        cell_value = tripsInfoSheet.iloc[tripRow, tripCol].lower()

        if cell_value != templateInfoCols[0]:
            messages.append(
                f"Error: The cell in Prefs Template Status sheet in {infoFilePath} does "
                + f"not contain '{templateInfoCols[0]}' at row 2 column B, it contains {cell_value}."
            )
            return None

        colHeaders = tripCol  # start where the Trip column is
        colToHeaderDict = {}

        for i in range(len(templateInfoCols)):
            header = tripsInfoSheet.iloc[tripRow, colHeaders].lower()
            if header in templateInfoCols:
                colToHeaderDict[colHeaders] = header
                colHeaders += 1
            elif header is None:
                messages.append(
                    f"Error: Ran into an empty value when verifying the column headers in the Trip Info sheet in the TripsAndLeaderStatusInfo document. "
                    + f"Make sure all column headers have the following names with no empty columns in between: {templateInfoCols}"
                )
                return None
            else:
                messages.append(
                    f"Error: In the Trip Info sheet in the TripsAndLeaderStatusInfo document "
                    + f" the column header '{header}' is not recognized as a valid column header. "
                    + f"Valid column headers are: {templateInfoCols}"
                )
                return None

        allTripsInfoDict = {}
        currentRow = tripRow + 1  # Skip the row with the headers
        tripID = 1

        # Go through every row, and stop when the trip name column is empty
        while (
            currentRow < len(tripsInfoSheet.index)
            and tripCol < len(tripsInfoSheet.columns)
        ) and not pd.isnull(tripsInfoSheet.iloc[currentRow, tripCol]):
            currentTripStatusDict = {}

            # Go through every column and assign the values from the row to the dictionary
            for colNum, colName in colToHeaderDict.items():
                # The column is not a trip type column
                cellValue = tripsInfoSheet.iloc[currentRow, colNum]

                if colName not in optionalCols and pd.isnull(cellValue):
                    messages.append(
                        f"Error: The value in the '{colName}' column for Trip Name: "
                        + f"{tripsInfoSheet.iloc[currentRow, tripCol]} "
                        + "was empty. Please enter a value for this cell."
                    )
                    return None
                else:
                    if isinstance(cellValue, datetime):
                        cellValue = cellValue.strftime("%Y-%m-%d")
                    currentTripStatusDict[colName] = cellValue

            # Add the dictionary to the status dictionary
            # The key is the tripID (row of the trip - 1), the value is the dictionary of the trip's info
            allTripsInfoDict[tripID] = currentTripStatusDict
            tripID += 1
            currentRow += 1

        return allTripsInfoDict

    except Exception as e:
        messages.append(
            "Error: The Trip Info sheet in the TripsAndLeaderStatusInfo document could not be read. "
            + f"Exception: {str(e)}"
        )
