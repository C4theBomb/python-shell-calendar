import sys
import os
from io import StringIO
from datetime import datetime
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("./src/"))
from calendarApp.models import Event, Calendar


class CalendarModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            "name": "Test Event 1",
            "start_time": "01/01/2000 00:00:00",
            "end_time": "01/01/2001 00:00:00"
        }
        cls.data2 = {
            "name": "Test Event 2",
            "start_time": "01/01/2001 00:00:00",
            "end_time": "01/01/2002 00:00:00"
        }

    @classmethod
    def tearDownClass(cls):
        del cls.data1
        del cls.data2

    def setUp(self):
        self.calendar = Calendar("Test")

    def tearDown(self):
        del self.calendar

    def test_event_add(self):
        # Test Configuration and Setup
        with patch('sys.stdout', StringIO()) as print_output:

            # Test Function
            self.calendar.add_event(
                self.data1["name"], self.data1["start_time"], self.data1["end_time"])
            calendar_event = self.calendar.schedule[0]

            # Test Assertions
            self.assertEqual(
                f"[INFO] Event {self.data1['name']} added", print_output.getvalue().rstrip())
            self.assertEqual(self.data1["name"], calendar_event.name)

    def test_event_delete(self):
        # Test Configuration and Setup
        self.calendar.schedule = [
            Event(
                self.data1["name"], self.data1["start_time"], self.data1["end_time"])
        ]
        calendar_event = self.calendar.schedule[0]

        with patch('sys.stdout', StringIO()) as print_output:
            # Test Function
            self.calendar.delete_event([str(calendar_event.id)])

            # Test Assertions
            self.assertEqual(
                f"[INFO] Event(s) ['{calendar_event.id}'] removed", print_output.getvalue().rstrip())
            self.assertFalse(self.calendar.schedule)

    def test_event_order(self):
        # Test Configuration and Setup
        self.calendar.schedule = [
            Event(
                self.data2["name"], self.data2["start_time"], self.data2["end_time"]),
            Event(
                self.data1["name"], self.data1["start_time"], self.data1["end_time"])
        ]

        # Test Function
        self.calendar.order_events()

        # Test Assertions
        self.assertLess(
            self.calendar.schedule[0].start_time, self.calendar.schedule[1].start_time)

    def test_event_print(self):
        # Test Configuration and Setup
        self.calendar.schedule = [
            Event(
                self.data1["name"], self.data1["start_time"], self.data1["end_time"]),
            Event(
                self.data2["name"], self.data2["start_time"], self.data2["end_time"])
        ]

        # Test Assertions
        with patch('sys.stdout', StringIO()) as print_output:
            self.calendar.print_events()
            self.assertTrue(self.data1["name"] in print_output.getvalue())
            self.assertTrue(self.data2["name"] in print_output.getvalue())


if __name__ == "__main__":
    unittest.main()
