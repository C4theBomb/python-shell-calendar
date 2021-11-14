import unittest
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath("./src/"))
from scheduleOpenings import calendar_structure
from scheduleOpenings.calendar_structure import Event, Calendar


class TestCalendarStructure(unittest.TestCase):

    def setUp(self):
        self.data1 = {
            "name": "Test Event 1",
            "start_time": "01/01/2000 00:00:00",
            "end_time": "01/01/2001 00:00:00"
        }
        self.data2 = {
            "name": "Test Event 2",
            "start_time": "01/01/2001 00:00:00",
            "end_time": "01/01/2002 00:00:00"
        }
        self.calendar = Calendar("Test")

    def test_event_add(self):
        # Test Configuration and Setup
        self.data1 = {
            "name": "Test Event",
            "start_time": "01/01/2000 00:00:00",
            "end_time": "01/01/2001 00:00:00"
        }
        event = Event(
            self.data1["name"], self.data1["start_time"], self.data1["end_time"]
        )
        self.calendar.add_event(
            self.data1["name"], self.data1["start_time"], self.data1["end_time"]
        )

        # Test Assertions
        calendar_event = self.calendar.schedule[0]
        self.assertEqual(calendar_event.name, self.data1["name"])
        self.assertEqual(
            calendar_event.start_time,
            datetime.strptime(self.data1["start_time"], "%d/%m/%Y %H:%M:%S")
        )
        self.assertEqual(
            calendar_event.start_time,
            datetime.strptime(self.data1["start_time"], "%d/%m/%Y %H:%M:%S")
        )

    def test_event_delete(self):
        # Test Configuration and Setup
        self.calendar.schedule = [
            Event(
                self.data1["name"], self.data1["start_time"], self.data1["end_time"]
            )
        ]
        calendar_event = self.calendar.schedule[0]

        # Test Assertions
        self.calendar.delete_event(calendar_event.id)
        self.assertListEqual(self.calendar.schedule, [])

    def test_event_order(self):
        pass

    def test_event_print(self):
        pass

    def tearDown(self) -> None:
        del self.calendar
