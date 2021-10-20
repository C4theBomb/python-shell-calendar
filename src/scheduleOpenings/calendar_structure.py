from datetime import date
import uuid


class Calendar():
    def __init__(self, name):
        self.events = {}
        self.name = name

    def add_event(self, event_name, start_time, end_time):
        if self.events[event_name]:
            print("ERROR: Duplicate event, operation aborted")
        else:
            self.events[event_name] = Event(event_name, start_time, end_time)

    def delete_event(self, event_name):
        if self.events[event_name] == False:
            print("WARNING: No event exists, nothing deleted")
        else:
            self.events.pop(event_name)

    def print_events(self):
        for event_name, event in self.events:
            print(f"{event_name}: {event.__str__()}")


class Event():
    def __init__(self, id, name, start_time, end_time):
        self.id = uuid.int()
        self.name = name
        self.start_time = self.parse_time(start_time)
        self.end_time = self.parse_time(end_time)

    def __str__(self):
        return [self.name, self.start_time, self.end_time]

    def parse_time(time_str):
        obj_str = date.strptime(time_str, "%d/%m/%y %H:%M:%S")
        return obj_str
