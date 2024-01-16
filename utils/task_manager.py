import os
import pickle


class TaskManager:
    def __init__(self,file_name = 'tasks.txt'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'rb' ) as file:
                return pickle.load(file)

        else:
            return []


    def save_task(self):
         with open(self.file_name, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False, 'subtasks': []})
        self.save_task()


    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.task[index]
            self.save_task()


    def mark_as_done(self, index):
        if 0 <= index <len(self.tasks):
            self.tasks[index]['done'] = True
            self.save_task()


    def add_subtask(self, index, sub_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['subtasks'].append({'subtask': sub_task, 'done': False})
            self.save_task()



    def mark_sub_task_as_done(self, index, sub_task_index):
        if 0 <= index <len(self.task) and 0 <= sub_task_index <len(self.task[index]['subtasks']):
            self.task[index]['sub tasks'][sub_task_index]['done'] = True
            save.save_tasks()


    def get_tasks(self):
        return self. tasks