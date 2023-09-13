class User:
    def __init__(self, source_user, user_tasks):
        self.username = source_user.get("username")
        self.name = source_user.get("name")
        self.email = source_user.get("email")
        self.company_name = source_user.get("company").get("name")
        self.tasks = user_tasks

    def get_number_tasks(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return list(filter(lambda task: task.get("completed") == True, self.tasks))

    def get_number_completed_tasks(self):
        return len(self.get_completed_tasks())

    def get_uncompleted_tasks(self):
        return list(filter(lambda task: task.get("completed") == False, self.tasks))

    def get_number_uncompleted_tasks(self):
        return len(self.get_uncompleted_tasks())
