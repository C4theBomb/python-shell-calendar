from scheduleOpenings import shell, calendar_structure


def main():
    calendar = calendar_structure.Calendar("main")
    shell.main_screen(calendar)


if __name__ == "__main__":
    main()
