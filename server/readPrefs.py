
import os
import pandas as pd
import re

def readPrefFolder(prefsDirectoryPath):
    messages = []
    # Check if the directory exists
    if os.path.isdir(prefsDirectoryPath):
        # Check if the directory contains at least one file
        if any(os.listdir(prefsDirectoryPath)):
            for file in os.listdir(prefsDirectoryPath):
                if not file.startswith("~") and file.endswith(".xlsx"):
                    messages.append("Reading file: " + file)
                    readPrefFile(os.path.join(prefsDirectoryPath, file), messages)
                #else:
                    #messages.append("The file is not an Excel file.")
                    #commented out because of temp files
                    
            messages.append("All files have been read.")
        else:
            messages.append("The directory is empty.")
    else:
        messages.append("The directory does not exist.")
    
    return messages
        
        
        
def readPrefFile(prefFilePath, messages):
    try:
        df = pd.ExcelFile(prefFilePath, engine='openpyxl')
        
        sheetNames = df.sheet_names 
        lowercase_sheetnames = [name.lower() for name in sheetNames]
        
        if re.search(r"prefs", lowercase_sheetnames[0]):
            prefsIndex = 0
            leaderInfoIndex = 1
        else:
            prefsIndex = 1
            leaderInfoIndex = 0
        
        prefsSheet = pd.read_excel(prefFilePath, sheet_name= sheetNames[prefsIndex])
        leaderInfoSheet = pd.read_excel(prefFilePath, sheet_name= sheetNames[leaderInfoIndex])
        
        readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages)
        
        messages.append("The file was read successfully.")    
        
        #NEED TO HANDLE ERROR IN leaderInfoSheet
        
    except:
        messages.append(f"Error: {prefFilePath} could not be read and {os.path.exists(prefFilePath)}.")
        
        
def readInTripLeaderInfo(leaderInfoSheet, prefFilePath, messages):
    try:
        # Find the first column with a non-missing value in the first 5 rows
        for column in leaderInfoSheet.columns:
            if leaderInfoSheet[column].head(5).astype(str).str.contains('name', case=False, na=False).any():
                titleCol = column
                break
        
        if not titleCol:
            messages.append(f"Error: The trip leader info sheet in {prefFilePath} does not contain a column with 'name'.")
            return None
        
        name = findValue(leaderInfoSheet, titleCol, "name")
        ufid = findValue(leaderInfoSheet, titleCol, "ufid")
        semLeft = findValue(leaderInfoSheet, titleCol, "semesters left")
        tripsAssigned = findValue(leaderInfoSheet, titleCol, "assigned")
        tripsDropped = findValue(leaderInfoSheet, titleCol, "drop")
        pickUp = findValue(leaderInfoSheet, titleCol, "pick up")
        coLeads = findValue(leaderInfoSheet, titleCol, "three leaders", threeCells=True)
        #reliabilityScore
        
        data = {"name" : name, "ufid" : ufid, "semesters left" : semLeft, "Trips Assigned" : tripsAssigned, "Trips Dropped" : tripsDropped, "Trips Picked Up" : pickUp, "Co-Leads" : coLeads}
        
        for key, value in data.items():
            if value is None:
                messages.append(f"Error: The trip leader info sheet in {prefFilePath} does not contain a value for '{key}'.")
        

        
        # match = leaderInfoSheet[titleCol].head(20)       
        # if match.any():
        #     first_index = match.idxmax()  # Get the first True index
        #     print(f"The first row in column '{titleCol}' that contains 'name' is at index {first_index}:")
        #     print(leaderInfoSheet.loc[first_index])
        # else:
        #     print(f"No rows in the first 20 of column contain 'name'.")
        
        
                
    except:
        messages.append(f"Error: The trip leader info could not be read for {prefFilePath}.")
        

def findValue(df, column, regex_string, threeCells=False):
    try:
        # Find the index of the given column
        col_index = df.columns.get_loc(column)

        # Find the row where the regex string matches
        mask = df[column].astype(str).str.contains(regex_string, case=False, na=False)
        if mask.any():
            # Get the index of the first True value
            row_index = mask.idxmax()

            if threeCells: # Check the next three columns, used for the three coleads and three promotion trips
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
    except:
        return None
    
# Test
output = readPrefFolder("Example_Data\prefs")
for message in output:
    print(message)

#RULES:
# it can only read xlsx files
#there can only be two sheets in the prefs file
# the prefs sheet has "prefs" in the name, the trip leader info does not have "prefs" in the name
#the first non-empty column in the trip leader info sheet must 
