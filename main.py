from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

def main():
   owner = Owner(name="Alex", preferences="Morning walks preferred")

   pet1 = Pet(name="Buddy", type="Dog")
   pet2 = Pet(name="Whiskers", type="Cat")

   owner.add_pet(pet1)
   owner.add_pet(pet2)


   # Add tasks out of order
   task1 = Task(description="Feed breakfast", time="07:30", frequency="daily", priority=1)
   task2 = Task(description="Morning walk", time="08:00", frequency="daily", priority=2)
   task3 = Task(description="Litter box cleaning", time="09:00", frequency="daily", priority=3)
   # Add two tasks at the same time to test conflict detection
   task4 = Task(description="Evening walk", time="18:00", frequency="daily", priority=2)
   task5 = Task(description="Dinner", time="19:00", frequency="daily", priority=1)
   task6 = Task(description="Vet appointment", time="08:00", frequency="once", priority=1)

   pet1.add_task(task2)  # 08:00
   pet1.add_task(task1)  # 07:30
   pet1.add_task(task4)  # 18:00
   pet1.add_task(task5)  # 19:00
   pet2.add_task(task3)  # 09:00
   pet2.add_task(task6)  # 08:00 (conflict with pet1's Morning walk)
   scheduler = Scheduler(owner)
   today = date.today()
   all_tasks = scheduler.get_tasks_for_date(today)

   # Detect and print conflicts
   conflicts = scheduler.detect_conflicts(all_tasks)
   if conflicts:
      print("\nTask Conflicts Detected:")
      for warning in conflicts:
         print(warning)
   else:
      print("\nNo task conflicts detected.")

   # Demonstrate sorting by time
   print("\nAll Tasks (Unsorted):")
   for task in all_tasks:
      print(f"- {task.time}: {task.description} (Status: {task.status})")

   sorted_tasks = scheduler.sort_by_time(all_tasks)
   print("\nAll Tasks (Sorted by Time):")
   for task in sorted_tasks:
      print(f"- {task.time}: {task.description} (Status: {task.status})")

   # Mark some tasks as completed
   scheduler.mark_task_completed(task2, completion_time="08:10")
   scheduler.mark_task_completed(task3, completion_time="09:05")

   # Demonstrate filtering by status
   completed_tasks = scheduler.filter_tasks(all_tasks, status="completed")
   print("\nCompleted Tasks:")
   for task in completed_tasks:
      print(f"- {task.time}: {task.description} (Status: {task.status})")

   # Demonstrate filtering by pet name
   buddy_tasks = scheduler.filter_tasks(all_tasks, pet_name="Buddy")
   print("\nTasks for Buddy:")
   for task in buddy_tasks:
      print(f"- {task.time}: {task.description} (Status: {task.status})")

if __name__ == "__main__":
   main()
