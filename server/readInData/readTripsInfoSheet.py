import re
import pandas as pd


def readStatusInfo(statusInfoSheet, statusFilePath, messages):
    statusInfoCols = [
        "Start Date",
        "End Date",
        "Trip",
        "Trip Category",
        "# of Total Guides Needed",
        "# of Lead Guides Needed",
    ]

    # try:
    #     # Find the row and column with the value "uf" (as in UF ID) in the first 5 rows of every column until found
    #     foundStatus = False
    #     ufID_Col = None
    #     ufID_Row = None
    #     for column in statusInfoSheet.columns:
    #         if foundStatus:
    #             break
    #         for row in range(5):
    #             cell_value = str(statusInfoSheet.at[row, column])
    #             if re.search(
    #                 r"uf id", cell_value, re.IGNORECASE
    #             ):  # Use regex for case-insensitive search
    #                 ufID_Col = statusInfoSheet.columns.get_loc(
    #                     column
    #                 )  # Get the column index
    #                 ufID_Row = row
    #                 foundStatus = True  # Exit the row loop
    #                 break

    #     if ufID_Col is None or ufID_Row is None:
    #         messages.append(
    #             f"Error: The Trip Leader Status sheet in {statusFilePath} does "
    #             + "not contain a column with 'uf id' in the first 5 rows."
    #         )
    #         return None

    #     colHeaders = ufID_Col + 1  # to skip ufID
    #     colToHeaderDict = {}

    #     for i in range(len(statusCols) - 1):  # -1 because ufID is already accounted for
    #         header = statusInfoSheet.iloc[ufID_Row, colHeaders]
    #         if header in statusCols:
    #             colToHeaderDict[colHeaders] = header
    #             colHeaders += 1
    #         elif header is None:
    #             messages.append(
    #                 f"Error: Ran into an empty value when verifying the column headers in the Trip Leader Status sheet. "
    #                 + f"Make sure all column headers have the following names with no empty columns in between: {statusCols}"
    #             )
    #             return None
    #         else:
    #             messages.append(
    #                 f"Error: The column header '{header}' in the Trip Leader Status sheet "
    #                 + f"is not recognized as a valid column header. "
    #                 + f"Valid column headers are: {statusCols}"
    #             )
    #             return None

    #     statusDict = {}
    #     currentRow = ufID_Row + 1  # Skip the row with the headers
    #     # Go through every row, and stop when the ufID is empty
    #     while not pd.isnull(statusInfoSheet.iloc[currentRow, ufID_Col]):
    #         tripLeaderStatusDict = {}

    #         # Go through every column and assign the values from the row to the dictionary
    #         for colNum, colName in colToHeaderDict.items():
    #             if colName in tripTypes:
    #                 cellValue = statusInfoSheet.iloc[currentRow, colNum]
    #                 if cellValue in possibleStatuses or pd.isnull(cellValue):
    #                     tripLeaderStatusDict[colName] = cellValue
    #                 else:
    #                     messages.append(
    #                         f"Error: The value '{cellValue}' in the "
    #                         + f"'{colName}' column for UF ID '{statusInfoSheet.iloc[currentRow, ufID_Col]}' "
    #                         + "is not a valid trip status. Valid statuses are: 'LG', 'I', or an empty cell."
    #                     )
    #                     return None

    #         # Add the dictionary to the status dictionary
    #         # The key is the UF ID, the value is the dictionary of the trip leader's status
    #         statusDict[statusInfoSheet.iloc[currentRow, ufID_Col]] = (
    #             tripLeaderStatusDict
    #         )

    #         currentRow += 1

    #     return statusDict

    # except Exception as e:
    #     messages.append(
    #         "Error: The trip leader prefs could not be read for "
    #         + f"{statusFilePath}. Exception: {str(e)}"
    #     )
