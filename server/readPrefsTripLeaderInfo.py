import os
import pandas as pd
import re


def readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages):
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
