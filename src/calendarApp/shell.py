def main_screen(calendar):
    while True:
        print("What would you like to do? ")
        print("\ta) Add event")
        print("\tb) Delete event")
        print("\tc) Print events")
        print("\td) Exit")
        answer = input(" $ ")

        if "a" in answer:
            add_event(calendar)
        elif "b" in answer:
            delete_event(calendar)
        elif "c" in answer:
            print_events(calendar)
        else:
            break


def add_event(calendar):
    print("What is the name of the event that you would like to add?")
    name = input(" $ ")
    print("When does your event start? FORMAT: dd/mm/yyyy hh:mm:ss")
    start_time = input(" $ ")
    print("When does your event end? FORMAT: dd/mm/yyyy hh:mm:ss")
    end_time = input(" $ ")
    try:
        calendar.add_event(name, start_time, end_time)
    except ValueError:
        print("Check your inputs, they don't seem to be in the right format.")


def delete_event(calendar):
    calendar.print_events()
    print("What is the ID of the event(s) you would like to delete? Separate ids with ,.")
    event_ids = input(" $ ")
    event_ids = event_ids.split(",")
    calendar.delete_event(event_ids)


def print_events(calendar):
    calendar.print_events()
