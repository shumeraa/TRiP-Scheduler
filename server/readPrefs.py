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
        
        

        if not tripCol:
            messages.append(
                f"Error: The prefs sheet in {prefFilePath} does"
                + "not contain a column with 'trip' in the first 5 rows."
            )
            return None

    except Exception as e:
        messages.append(
            "Error: The trip leader prefs could not be read for "
            + f"{prefFilePath}. Exception: {str(e)}"
        )


# def find
