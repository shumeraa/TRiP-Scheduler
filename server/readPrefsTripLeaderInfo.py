import os
import pandas as pd
import re


def readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages):
    """
    Reads and processes trip leader information from a given Excel sheet.

    This function searches for specific columns by name within the first 5 rows of the leaderInfoSheet,
    extracts relevant information (name, UFID, semesters left, trips assigned, dropped, and picked up, and co-leads),
    calculates a reliability score, and returns a dictionary containing this information. If any required information
    is missing, or if an error occurs during processing, an appropriate error message is appended to the messages list
    and the function returns None.

    Parameters:
    - leaderInfoSheet (DataFrame): The pandas DataFrame containing the trip leader information.
    - prefFilePath (str): The file path of the preferences file, used for error messaging.
    - messages (list): A list to which error messages will be appended.

    Returns:
    - dict: A dictionary containing the extracted information and calculated reliability score if successful, None otherwise.

    Raises:
    - Exception: Captures and logs any exception that occurs during the processing of the trip leader information.
    """
    try:
        # Find the first column with the value "name" in the first 5 rows
        for column in leaderInfoSheet.columns:
            if (
                leaderInfoSheet[column]
                .head(5)
                .astype(str)
                .str.contains("name", case=False, na=False)
                .any()
            ):
                titleCol = column
                break

        if not titleCol:
            messages.append(
                f"Error: The trip leader info sheet in {prefFilePath} does"
                + "not contain a column with 'name' in the first 5 rows."
            )
            return None

        name = findValue(leaderInfoSheet, titleCol, "name")
        ufid = findValue(leaderInfoSheet, titleCol, "ufid")
        # Getting class year and role status from other excel document
        semLeft = findValue(leaderInfoSheet, titleCol, "semesters left")
        tripsAssigned = findValue(leaderInfoSheet, titleCol, "assigned")
        tripsDropped = findValue(leaderInfoSheet, titleCol, "drop")
        pickUp = findValue(leaderInfoSheet, titleCol, "pick up")
        coLeads = findValue(leaderInfoSheet, titleCol, "three leaders", threeCells=True)

        data = {
            "name": name,
            "ufid": ufid,
            "semesters left": semLeft,
            "Trips Assigned": tripsAssigned,
            "Trips Dropped": tripsDropped,
            "Trips Picked Up": pickUp,
            "Co-Leads": coLeads,
        }

        for key, value in data.items():
            if value is None:
                messages.append(
                    f"Error: The trip leader info sheet in {prefFilePath}"
                    + f"does not contain a value for '{key}'."
                )
                return None

        reliabilityScore = pickUp - tripsDropped
        data.update({"Reliability Score": reliabilityScore})

        return data

    except Exception as e:
        messages.append(
            "Error: The trip leader info could not be read for"
            + f"{prefFilePath}. Exception: {str(e)}"
        )


def findValue(df, column, regex_string, threeCells=False):
    """
    Searches for a value in a DataFrame column matching a regex pattern and optionally returns adjacent values.

    This function searches a specified column in a pandas DataFrame for a value that matches a given regex pattern.
    If a match is found, the function returns the value in the next column or, if threeCells is True, values in the
    next three columns as a list. If no match is found, the function returns None.

    Parameters:
    - df (DataFrame): The pandas DataFrame to search.
    - column (str): The name of the column to search for the regex pattern.
    - regex_string (str): The regex pattern to search for within the specified column.
    - threeCells (bool, optional): If True, returns a list of values from the next three columns adjacent to the found value.
                                    Defaults to False.

    Returns:
    - The value found in the next column, a list of values from the next three columns if threeCells is True, or None if no match is found.

    Note:
    - This function prints the values found for the regex_string if threeCells is True.
    """
    
    try:
        # Find the index of the given column
        col_index = df.columns.get_loc(column)

        # Find the row where the regex string matches
        mask = df[column].astype(str).str.contains(regex_string, case=False, na=False)
        if mask.any():
            # Get the index of the first True value
            row_index = mask.idxmax()

            if (
                threeCells
            ):  # Check the next three columns, used for the three coleads and three promotion trips
                values = []
                for i in range(1, 4):  # Check the next three columns
                    if col_index + i < len(df.columns):
                        next_col_value = df.iloc[row_index, col_index + i]
                        if pd.notna(next_col_value):
                            values.append(next_col_value)
                print(f"Values for {regex_string}: {values}")
                return values
            else:
                # Return the value of the cell in the column to the right
                return df.iloc[row_index, col_index + 1]
        else:
            return None  # or you can choose to raise an exception or return another specific value
    except Exception:
        return None
