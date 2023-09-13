from datetime import datetime

import requests

from settings import USER_URL, TASK_URL
from user import User


def get_reports():
    reports = []
    users_response = get_response(USER_URL)
    tasks_response = get_response(TASK_URL)
    valid_tasks = get_valid_tasks(tasks_response)

    for user_response in users_response:
        if not user_is_valid(user_response):
            continue

        user_tasks = get_task_for_user(user_response, valid_tasks)
        context = User(user_response, user_tasks)
        report = report_maker(context)

        reports.append(report)

    return reports


def get_response(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def user_is_valid(user_response):
    if user_response.get("name") and user_response.get("username"):
        return True
    return False


def get_valid_tasks(tasks):
    """Возвращает задачи, которые прошли проверку"""
    result = []

    for task in tasks:
        if task.get("title") and task.get("userId"):
            result.append(task)

    return result


def get_task_for_user(user, todos):
    return list(filter(lambda task: user.get("id") == task.get("userId"), todos))


def report_maker(context):
    file_name = f"{context.username}"
    report_text = f"# Отчёт для {context.company_name}.\n"
    time_create = datetime.now().strftime('%d.%m.%y %H:%M')
    report_text += f"{context.name} <{context.email}> {time_create}\n"
    report_text += f"Всего задач: {context.get_number_tasks()}\n"
    report_text += "\n"
    report_text += f"## Актуальные задачи ({context.get_number_uncompleted_tasks()}):\n"
    for task in context.get_uncompleted_tasks():
        title = get_formatted_title(task.get('title'))
        report_text += f"- {title}\n"
    report_text += "\n"
    report_text += f"## Завершённые задачи ({context.get_number_completed_tasks()}):\n"
    for task in context.get_completed_tasks():
        title = get_formatted_title(task.get('title'))
        report_text += f"- {title}\n"

    return {"file_name": file_name, "report_text": report_text}


def get_formatted_title(title):
    if len(title) > 46:
        return title[:46] + "…"
    return title

