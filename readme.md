**create_students:**
this function takes the file name containing student logs and reads the information line by line, skipping the first line (with the next() function)
the line is split into its four components (ID, action code, entry, and timestamp) and read in succession (kept track of by a counter part_of_entry: ID 1, Action 2, Entry 3, Time 4):

for ID, if the student has already been added to the created input_info dictionary, we continue; if the student has not been added (both of which is checked by .keys() function, to search in O(1) if it exists already),
a dictionary with the student ID key is initialized (with the lowest and latest page #s as -1, and the scores/score count as 0) and added to input_info.

for action code, if it is P or S, their respective flag is_S or is_P is set to true so we can properly analyze the third element. we ignore T because it is of no use.

for the third element, if the action was P (based on the flag previously set), we compare the submitted page to the existing lowest value in the dictionary and added if the new page is the lowest- if it is the first page read, it is automatically added as the lowest. it is also automatically added as the latest no matter what.
if the action was S, we add the score to the total and increase the submission count for later use.
otherwise, we continue; no other information is required.

for the time stamp, it has no purpose, so we use this to reset the counter and continue to the next line to repeat for all lines.

the completed input info is then returned as a nested dictionary: {ID: {lateP, lowP, avgScore, scoreCount}}

**sort_students:**
this function iterates through every student in input_info and calculates the average score based on the total and score count. since the score count is
no longer needed, we delete this key.

however, to account for invalid students (those without P or S logs), we delete the student if they have a lowP of -1 or score count of 0 and do not calculate total.

this function then uses sorted(), a built in function, to organize the remaining students by lowest page, then latest page, then average.

**time complexity:**
create_students: reads each line once, therefore O(L) with L being the number of lines in the logs.
sort_students:
goes through every student to either calculate average or delete the student, therefore O(S) with S being the number of students.
then, sorts the students with the built in sorted function, which runs in O(Slog(S)) time - based on python documentation of the function
then, prints out each valid student ~O(S) as it goes through each student once
O(SlogS) + O(S) -> O(Slog(S))
sort_students combined overall, is O(Slog(S))


the total time complexity as a result (of both create and sort students) is O(Slog(S) + L)