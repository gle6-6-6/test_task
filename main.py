from report_creator import get_reports
from file_creator import write_file


def main():
    reports = get_reports()
    write_file(reports)


if __name__ == "__main__":
    main()
