from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

def main():
   owner = Owner(name="Alex", preferences="Morning walks preferred")

   pet1 = Pet(name="Buddy", type="Dog")
   pet2 = Pet(name="Whiskers", type="Cat")

   owner.add_pet(pet1)
   owner.add_pet(pet2)

   task1 = Task(description="Feed breakfast", time="07:30", frequency="daily", priority=1)
   task2 = Task(description="Morning walk", time="08:00", frequency="daily", priority=2)
   task3 = Task(description="Litter box cleaning", time="09:00", frequency="daily", priority=3)

   pet1.add_task(task1)
   pet1.add_task(task2)
   pet2.add_task(task3)

   scheduler = Scheduler(owner)
   today = date.today()
   todays_tasks = scheduler.organize_tasks(today)

   print("Today's Schedule:")
   for task in todays_tasks:
      print(f"- {task.time}: {task.description} (Priority {task.priority})")

if __name__ == "__main__":
   main()
