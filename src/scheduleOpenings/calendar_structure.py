from datetime import datetime
import uuid


class Calendar():
    def __init__(self, name):
        self.schedule = []
        self.name = name

    def add_event(self, event_name, start_time, end_time):
        if list(filter(lambda event: (event.name == event_name), self.schedule)):
            print("[ERROR] Duplicate event, operation aborted")
        else:
            event = Event(event_name, start_time, end_time)
            self.schedule.append(event)
            print("[INFO] Event added")
            self.order_events()

    def delete_event(self, event_id):
        event = list(filter(lambda event: (
            event.id == event_id), self.schedule))
        if event:
            self.schedule.remove(event[0])
            print("[INFO] Event removed")
        else:
            print("[WARNING] No such event exists. Operation aborted.")

    def print_events(self):
        for event in self.schedule:
            print(event)

    def order_events(self):
        self.schedule.sort(key=(lambda event: event.start_time))


class Event():
    def __init__(self, name, start_time, end_time):
        self.id = uuid.uuid4()
        self.name = name
        self.start_time = self.parse_time(start_time)
        self.end_time = self.parse_time(end_time)

    def __str__(self):
        return f"Event ID: {self.id} \n\tName: {self.name} \n\tTime:{self.start_time} to {self.end_time}"

    def parse_time(self, time_str):
        obj_str = datetime.strptime(time_str, "%d/%m/%Y %H:%M:%S")
        return obj_str
