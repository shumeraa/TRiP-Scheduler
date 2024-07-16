import re
import pandas as pd


def readStatusInfo(statusInfoSheet, statusFilePath, messages):
    """
    Reads and processes the status information of trip leaders from the Trip Leader Status sheet.

    This function searches for a specific set of columns in the status information sheet,
    validates the presence of expected column headers, and then iterates through each row
    to compile a dictionary of trip leader statuses based on their UF ID. It handles various
    errors such as missing columns or invalid status values and reports them through a message list.

    Parameters:
    - statusInfoSheet (DataFrame): The pandas DataFrame containing the status information sheet.
    - statusFilePath (str): The file path of the Excel sheet being processed, used for error reporting.
    - messages (list): A list to which error or status messages will be appended.

    Returns:
    - dict or None: A dictionary mapping UF IDs to their respective trip leader status dictionaries
      if the sheet is processed successfully, or None if an error occurs.

    Raises:
    - Exception: Propagates any exceptions that occur during processing, with an error message appended to `messages`.
    """

    statusCols = [
        "uf id",
        "class",
        "full name",
        "overnight",
        "biking",
        "spelunking",
        "watersports",
        "surfing",
        "sea kayaking",
    ]

    tripTypes = [
        "overnight",
        "biking",
        "spelunking",
        "watersports",
        "surfing",
        "sea kayaking",
    ]

    possibleStatuses = ["LG", "I"]

    try:
        # Find the row and column with the value "uf id" in the first 5 rows of every column until found
        foundStatus = False
        ufID_Col = None
        ufID_Row = None
        for column in statusInfoSheet.columns:
            if foundStatus:
                break
            for row in range(5):
                cell_value = str(statusInfoSheet.at[row, column])
                if re.search(
                    r"uf id", cell_value, re.IGNORECASE
                ):  # Use regex for case-insensitive search
                    ufID_Col = statusInfoSheet.columns.get_loc(
                        column
                    )  # Get the column index
                    ufID_Row = row
                    foundStatus = True  # Exit the row loop
                    break

        if ufID_Col is None or ufID_Row is None:
            messages.append(
                f"Error: The Trip Leader Status sheet in the TripsAndLeaderStatusInfo document in {statusFilePath} does "
                + "not contain a column with 'uf id' in the first 5 rows."
            )
            return None

        colHeaders = ufID_Col + 1  # to skip ufID
        colToHeaderDict = {}

        for i in range(len(statusCols) - 1):  # -1 because ufID is already accounted for
            header = statusInfoSheet.iloc[ufID_Row, colHeaders].lower()
            if header in statusCols:
                colToHeaderDict[colHeaders] = header
                colHeaders += 1
            elif header is None:
                messages.append(
                    f"Error: Ran into an empty value when verifying the column headers in the Trip Leader Status sheet in the TripsAndLeaderStatusInfo document. "
                    + f"Make sure all column headers have the following names with no empty columns in between: {statusCols}"
                )
                return None
            else:
                messages.append(
                    f"Error: The column header '{header}' in the Trip Leader Status sheet in the TripsAndLeaderStatusInfo document"
                    + f"is not recognized as a valid column header. "
                    + f"Valid column headers are: {statusCols}"
                )
                return None

        statusDict = {}
        currentRow = ufID_Row + 1  # Skip the row with the headers
        # Go through every row, and stop when the ufID is empty
        while not pd.isnull(statusInfoSheet.iloc[currentRow, ufID_Col]):
            tripLeaderStatusDict = {}

            # Go through every column and assign the values from the row to the dictionary
            for colNum, colName in colToHeaderDict.items():
                if colName in tripTypes:
                    cellValue = statusInfoSheet.iloc[currentRow, colNum]
                    if cellValue in possibleStatuses or pd.isnull(cellValue):
                        tripLeaderStatusDict[colName] = cellValue
                    else:
                        messages.append(
                            f"Error: The value '{cellValue}' in the "
                            + f"'{colName}' column for UF ID '{statusInfoSheet.iloc[currentRow, ufID_Col]}' "
                            + "is not a valid trip status in the TripsAndLeaderStatusInfo document. Valid statuses are: 'LG', 'I', or an empty cell."
                        )
                        return None
                else:
                    # The column is not a trip type column
                    cellValue = statusInfoSheet.iloc[currentRow, colNum]

                    if pd.isnull(cellValue):
                        messages.append(
                            f"Error: The value in the '{colName}' column for UF ID: "
                            + f"{statusInfoSheet.iloc[currentRow, ufID_Col]} "
                            + "was empty in the TripsAndLeaderStatusInfo document. Please enter a value for this cell."
                        )
                        return None
                    else:
                        tripLeaderStatusDict[colName] = cellValue

            # Add the dictionary to the status dictionary
            # The key is the UF ID, the value is the dictionary of the trip leader's status
            statusDict[statusInfoSheet.iloc[currentRow, ufID_Col]] = (
                tripLeaderStatusDict
            )

            currentRow += 1

        return statusDict

    except Exception as e:
        messages.append(
            "Error: The trip leader status in the TripsAndLeaderStatusInfo document could not be read for "
            + f"{statusFilePath}. Exception: {str(e)}"
        )


# UF ID needs to be the first column in Trip Leader info sheet
