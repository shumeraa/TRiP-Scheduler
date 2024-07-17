# Prefs Files: 
## The files that contain a trip leader's rankings of each trip on one sheet, and information about the trip leader on the other
- Must be xlsx files
- Must all be in the same format
- Must contain two sheets (a sheet is a single page within an Excel workbook)
- The sheets can be in any order
- The sheet that contains a trip leader's ranking for a trip must have the word "prefs" in in the title (case does not matter)
- The other sheet can have any name and will be assumed to be the "Trip leader info" sheet

## The sheet that contains the prefs:
- must contain a column with the header "trip" (case does not matter) that has all of the trip names in it
- The column to the right of the column that has the trip names must be the prefs column 
- the prefs column numbers must be from 0 to 5 (an empty cell )
- 0 means a leader cannot lead the trip, a 1 is the lowest rating, and a 5 is the best rating 
- an empty pref rating will be considered a 0
- the order of the trips are used for mapping the pref to the trip, so the trips can be named anything as long as they are in the same order as in the TripsAndLeaderStatusInfo document
- you can add more columns if you'd like, but if they have "trip" in their header, be sure that they are after the "trip" column

## The sheet that contains the trip leader's info:
- "Name" must be in the same column as the rest of the column headers (everything is based on the same column "Name" is in)
- For example, going down it must be "Name", then "UFID", and so on
- The columns we are extracting information from are: name, ufid, semesters left, Trips Assigned, Trips Dropped, Trips Picked Up, Co-Leads
- only these columns are allowed to use these words (in any context): name, ufid, semesters left, trips assigned, drop, pick up, three leaders.
- this is because the program works by looking for these key words. For example, if a cell in the same column as "Name" includes the word "drop", the value in the cell to the right will be considered as the value for "Trips Dropped"
- The values to the right of their respective header (for example the right of "Name") is the value for that header
- Empty values will cause an error
- reliability score is calculated as tripsPickedUp - tripsDropped


