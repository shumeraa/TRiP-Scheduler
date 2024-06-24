import re


def readInPrefs(prefsSheet, prefFilePath, messages):
    """
    Read in the trip leader preferences from the prefs sheet by:
    1. Finding the column and row of the cell with "trip" in it by
        searching the first 5 rows of each column in the sheet.
    2. Creating a dict that maps trip names to preference for that trip


    Args:
        prefsSheet (Pandas Df): the sheet containing the trip leader preferences
        prefFilePath (string): file path of the pregs sheet
        messages (list of strings): list of messages to be displayed to the user

    Returns:
        dict{string : int }: a dictionary containing the trip leader preferences
    """
    try:
        # Find the first column with the value "trip" in the first 5 rows
        foundTrip = False
        for column in prefsSheet.columns:
            if foundTrip:
                break
            for row in range(5):
                cell_value = str(prefsSheet.at[row, column])
                if re.search(
                    r"trip", cell_value, re.IGNORECASE
                ):  # Use regex for case-insensitive search
                    tripCol = column
                    tripRow = row
                    foundTrip = True  # Exit the row loop
                    break

        # Now we have the column and row of the cell with "trip" in it
        print(f"Trip column: {tripCol}, Trip row: {tripRow}")

        prefsDict = {}
        tripID = 0
        tripRow += 1  # Move to the next row to get the first trip

        # while the value of the cell is not empty
        while prefsSheet.iloc[tripRow, tripCol] is not None:
            pref = prefsSheet.iloc[tripRow, tripCol + 1]

            if not pref:
                messages.append(
                    f"Error: The prefs sheet in {prefFilePath} does "
                    + f"not contain a preference for trip {prefsSheet.iloc[tripRow, tripCol]}."
                )
                return None

            prefsDict[tripID] = pref
            tripRow += 1

        print(prefsDict)

        if not tripCol:
            messages.append(
                f"Error: The prefs sheet in {prefFilePath} does "
                + "not contain a column with 'trip' in the first 5 rows."
            )
            return None

    except Exception as e:
        messages.append(
            "Error: The trip leader prefs could not be read for "
            + f"{prefFilePath}. Exception: {str(e)}"
        )


""" 
TODO: IF RETURN NONE TO NOT GO TO NEXT FILE
Assumes the TRiP column's first row in the column is labeled TRiP
Assumes the column next to the TRiP column is the prefs column
Assumes the TRiPs are in the exact same order in every prefs sheet
    and in the same order as the info sheet 
    """
