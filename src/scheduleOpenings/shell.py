def main_screen(calendar):
    print("What would you like to do? ")
    print("\ta) Add event")
    print("\ta) Edit event")
    print("\tb) Print events")
    print("\tc) Exit")
    answer = input(" $ ")

    if "a" in answer:
        add_event(calendar)
    elif "b" in answer:
        pass
    elif "c" in answer:
        pass
    else:
        pass


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
    main_screen(calendar)


def edit_event(calendar):
    pass


def print_events(calendar):
    pass
