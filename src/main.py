from calendarApp import shell, models


def main():
    calendar = models.Calendar("main")
    shell.main_screen(calendar)


if __name__ == "__main__":
    main()
