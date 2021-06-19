class Tasks:
    def __init__(self, day, tasks):
        self.day = day    # str
        self.tasks = tasks    # list
        
        
    def __str__(self):
        n_tasks = len(self.tasks)
        strings_list = [f"{i+1}) {self.tasks[i]}\n" for i in range(n_tasks-1)]
        strings_list.append(f"{n_tasks}) {self.tasks[n_tasks-1]}")
        strings_list.insert(0, "Today:\n")
        return " ".join(strings_list)
        
tasks_list = ["Do yoga", "Make breakfast", "Learn basics of SQL", "Learn what is ORM"]
today = Tasks("Today", tasks_list)
print(today)