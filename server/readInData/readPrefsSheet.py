import re
import pandas as pd


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
        tripCol = None
        tripRow = None
        for column in prefsSheet.columns:
            if foundTrip:
                break
            for row in range(5):
                cell_value = str(prefsSheet.at[row, column])
                if re.search(
                    r"trip", cell_value, re.IGNORECASE
                ):  # Use regex for case-insensitive search
                    tripCol = prefsSheet.columns.get_loc(column)  # Get the column index
                    tripRow = row
                    foundTrip = True  # Exit the row loop
                    break

        if tripCol is None or tripRow is None:
            messages.append(
                f"Error: The prefs sheet in {prefFilePath} does "
                + "not contain a column with 'trip' in the first 5 rows."
            )
            return None

        # Now we have the column and row of the cell with "trip" in it

        prefsDict = {}
        tripID = 0
        tripRow += 1  # Move to the next row to get the first trip

        # while the value of the trip cell is not empty
        while tripRow < len(prefsSheet) and not pd.isnull(
            prefsSheet.iloc[tripRow, tripCol]
        ):
            pref = prefsSheet.iloc[tripRow, tripCol + 1]

            if pref is None:
                # assume an empty preference is a 0
                pref = 0

            if not isinstance(pref, int) or pref > 5 or pref < 0:
                messages.append(
                    f"Error: For the prefs sheet in {prefFilePath}, "
                    + f" '{pref}' is not a valid rating for the trip: {prefsSheet.iloc[tripRow, tripCol]}."
                )
                return None

            prefsDict[tripID] = pref
            tripRow += 1
            tripID += 1

        return prefsDict

    except Exception as e:
        messages.append(
            "Error: The trip leader prefs could not be read for "
            + f"{prefFilePath}. Exception: {str(e)}"
        )


"""
Assumes the TRiP column's first row in the column is labeled TRiP
Assumes the column next to the TRiP column is the prefs column
Assumes the TRiPs are in the exact same order in every prefs sheet
    and in the same order as the info sheet 
Assumes there is an empty row after the last trip
    """
