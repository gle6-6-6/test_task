import os
from datetime import datetime


def write_file(reports):
    if not os.path.isdir("tasks"):
        os.mkdir("tasks")

    for report in reports:
        file_name = f"tasks/{report.get('file_name')}.txt"
        if os.path.exists(file_name):
            old_time_creation = get_formatted_date(file_name)
            new_file_name = f"tasks/old_{report.get('file_name')}_{old_time_creation}.txt"
            os.rename(file_name, new_file_name)
        with open(f"{file_name}", "w", encoding='utf-8') as file:
            file.write(report.get('report_text'))


def get_formatted_date(file_name):
    if os.name == "nt":
        # Получение времени создания старого файла и перевод в нужный формат
        # Вместо знака ":" стоит "-" для операционной системы Windows

        old_time_creation = datetime.fromtimestamp(os.path.getctime(file_name)).strftime("%Y-%m-%dT%H-%M")
    else:
        old_time_creation = datetime.fromtimestamp(os.path.getctime(file_name)).strftime("%Y-%m-%dT%H:%M")

    return old_time_creation