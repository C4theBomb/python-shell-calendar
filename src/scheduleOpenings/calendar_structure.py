from datetime import datetime
import uuid


class Calendar():
    def __init__(self, name):
        self.schedule = []
        self.name = name

    def add_event(self, event_name, start_time, end_time):
        if list(filter(lambda event: (event.name == event_name), self.schedule)):
            print("ERROR: Duplicate event, operation aborted")
        else:
            event = Event(uuid.uuid4(), event_name, start_time, end_time)
            self.schedule.append(event)
            print("INFO: Event added")
            self.order_events()

    def delete_event(self, event_name):
        if self.events[event_name] == False:
            print("WARNING: No event exists, nothing deleted")
        else:
            self.events.pop(event_name)

    def print_events(self):
        pass

    def order_events(self):
        for event in self.schedule:
            print(event)


class Event():
    def __init__(self, id, name, start_time, end_time):
        self.id = uuid.uuid4()
        self.name = name
        self.start_time = self.parse_time(start_time)
        self.end_time = self.parse_time(end_time)

    def __str__(self):
        return [self.name, self.start_time, self.end_time]

    def parse_time(self, time_str):
        obj_str = datetime.strptime(time_str, "%d/%m/%Y %H:%M:%S")
        return obj_str
