# Prefs Files: 
## The files that contain a trip leader's rankings of each trip on one sheet, and information about the trip leader on the other
    - Must be xlsx files
    - Must all be in the same format
    - Must contain two sheets (a sheet is a single page within an Excel workbook)
    - The sheets can be in any order
    - The sheet that contains a trip leader's ranking for a trip must have the word "prefs" in in the title (case does not matter)
    - The other sheet can have any name and will be assumed to be the "Trip leader info" sheet

## The sheet that contains the prefs:
    - The column to the right of the column that has the trip names must be the prefs column 
    - the prefs column numbers must be from 0 to 5 (an empty cell )
    - 0 means a leader cannot lead the trip, a 1 is the lowest rating, and a 5 is the best rating 
    - an empty pref rating will be considered a 0
    - the order of the trips are used for mapping the pref to the trip, so the trips can be named anything as long as they are in the same order as in the TripsAndLeaderStatusInfo document



