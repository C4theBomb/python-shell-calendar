# AP CSP Create Task Written Response Answers

## 3a.

1. The overall purpose of the program is to help users organize their tasks.
2. The functionality of the program is to organize user-inputted tasks by their start time.
3. The input of the program demonstrated in the video includes:
    - The input at the beginning the dictates what path the program takes (create event, delete event, edit event, print calendar, exit)
    - The output is a message that prints based off of what what you pick in the input. The user input selecting the create event prints the event creation sequence.

## 3b.

3. My list name is called 'schedule'.
4. The each Event() object in the list represents each individual event in a calendar.
5. This list manages complexity because it allows for easy sorting and access of the events in the calendar and stores more data than can be held in an individual variable.

## 3c.

3. The 'delete_event' procedure takes a list of ids to remove from the schedule. The procedure then makes sure that all of the ids are valid, deleting if they are, and throwing an error if they are not.
4. The 'schedule' list filtered down using the 'event_ids' list, which contains the object ids of the events to be deleted from the schedule, to create the 'doomed_events' list. A list called 'doomed_event_ids' is then created by accessing the 'id' property of each object in the list. It then makes sure that every id in 'doomed_event_ids' is in the schedule. Then it removes all of the doomed events from 'doomed_events' from the 'schedule' list.

## 3d.

1. The first call has a list of multiple events ids that are all included in the schedule list. The second call has a list of multiple event ids, one of which is not included in the schedule list.
    - calendar.delete_event(["63580c28-8463-4e6e-b6eb-996390107828", "12580d28-8463-4e6e-b6eb-996390107568"])
        - NOTE: Both items in the list are valid object ids in the schedule list.
    - calendar.delete_event(["63532c28-8463-4e6e-b6eb-996390107828", "15860d28-8463-4e6e-b6eb-996390107568"])
        - NOTE: The first item in the list represents a valid object id, while the second object id is invalid and not included in the list.
2. Both calls test to see if the event_ids given are included in the 'schedule' list. The first call has all valid object ids, so the else statement resolves to true and the top part of the if statment runs. The second call has an invalid object id, so the if statment will resolve to false and the else part runs.
3. The result of the first call is the removal of the events from the 'schedule' list, then the printing of the text in the upper if statement. The results of the second call is the printing of the text in the else statement.
