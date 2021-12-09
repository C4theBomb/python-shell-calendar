from calendarApp import shell, models
import os


def main():
    os.system("clear")
    calendar = models.Calendar("main")
    shell.main_screen(calendar)


if __name__ == "__main__":
    main()
