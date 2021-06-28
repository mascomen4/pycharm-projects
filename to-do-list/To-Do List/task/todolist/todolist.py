from dataclasses import replace

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import delete
from datetime import datetime, date, timedelta

MONTHS = {i: date(2001, i, 13).strftime("%b") for i in range(1, 13)}
engine = create_engine("sqlite:///todo.db?check_same_thread=False")

Base = declarative_base()


class Todo(Base):
    __tablename__ = "task"
    # Primary key says that this column is primary key
    id = Column(Integer, primary_key=True)
    task = Column(String, default="Nothing to do!")
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


# Create all the tables
Base.metadata.create_all(engine)

# Create the session with the database, using engine
Session = sessionmaker(bind=engine)
session = Session()


# Creating a row of the table:


def print_menu():
    print("")
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")


def perform_choice():
    print_menu()
    choice = int(input())
    if choice == 1:
        # Show today's tasks
        today = datetime.now().date()
        today_str = today.strftime("%d %b")
        print(f"\nToday {today_str}:")
        rows = session.query(Todo).filter(Todo.deadline == today).all()
        if rows:
            for i, row in enumerate(rows):
                print(f"{i + 1}. {row.task}")
        else:
            print("Nothing to do!")
        return 0

    elif choice == 2:
        # Show weeks tasks
        # Select the days of the current week. Select current day + 7 days.
        today = datetime.today().date()
        for delta in range(7):
            query = session.query(Todo)
            current_day = today + timedelta(delta)
            rows = query.filter(Todo.deadline == current_day).all()
            str_day = current_day.strftime("%A %d %b")
            print(f"\n{str_day}:")
            if rows:
                for i, row in enumerate(rows):
                    if row.task == "Nothing to do!":
                        string = f"{row.task}"
                    else:
                        string = f"{i + 1}. {row.task}"
                    print(string)
            else:
                print("Nothing to do!")
        return 0

    elif choice == 3:
        print("\nAll tasks:")
        rows = session.query(Todo).order_by(Todo.deadline).all()
        if rows:
            for i, row in enumerate(rows):
                deadline = row.deadline.strftime('%d %b')
                deadline_row = deadline[:3].replace('0', '') + deadline[3:]
                print(f"{i + 1}. {row.task}. {deadline_row}")
        else:
            print("Nothing to do!")
        return 0

    elif choice == 4:
        # Show missed tasks: get all the tasks that has the deadline less than today's date
        print("Missed tasks:")
        today = datetime.today()
        rows = session.query(Todo).filter(Todo.deadline < today).all()
        if rows:
            for i, row in enumerate(rows):
                deadline = row.deadline.strftime('%d %b')
                deadline_row = deadline[:3].replace('0', '') + deadline[3:]
                print(f"{i + 1}. {row.task}. {deadline_row}")
        else:
            print("Nothing is missed!")
        return 0

    elif choice == 5:
        # Add task
        print("\nEnter task")
        string = input()
        print("Enter deadline")
        deadline = datetime.strptime(input(), "%Y-%m-%d")
        new_row = Todo(task=string, deadline=deadline)
        session.add(new_row)
        session.commit()
        print("The task has been added!")
        return 0
    elif choice == 6:
        rows = session.query(Todo).order_by(Todo.deadline).all()
        if rows:
            print("Choose the number of the task you want to delete:")
            for i, row in enumerate(rows):
                deadline = row.deadline.strftime('%d %b')
                deadline_row = deadline[:3].replace('0', '') + deadline[3:]
                print(f"{i + 1}. {row.task}. {deadline_row}")
            delete_choice = int(input())
            try:
                session.query(Todo).filter(Todo.task == rows[delete_choice - 1].task
                                           and Todo.deadline == rows[delete_choice].deadline).delete()
                session.commit()
                print('The task has been deleted!')
            except:
                print("Sorry, there's no such row")
            return 0
    elif choice == 0:
        print("\nBye!")
        return 1


# tasks_list = ["Do yoga", "Make breakfast", "Learn basics of SQL", "Learn what is ORM"]
# print("Today:")
# for i,task in enumerate(tasks_list):
#     print(f"{i+1}) {task}")

if __name__ == "__main__":
    while True:
        if perform_choice():
            break
