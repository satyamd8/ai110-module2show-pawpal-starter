from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

def test_mark_task_completed():
   task = Task(description="Test Task", time="10:00", frequency="daily", priority=1)
   owner = Owner(name="Test Owner")
   pet = Pet(name="Test Pet", type="Dog")
   owner.add_pet(pet)
   pet.add_task(task)
   scheduler = Scheduler(owner)
   scheduler.mark_task_completed(task, completion_time="10:30")
   assert task.status == "completed"
   assert task.completion_time == "10:30"

def test_add_task_increases_pet_task_count():
   pet = Pet(name="Test Pet", type="Cat")
   initial_count = len(pet.tasks)
   task = Task(description="Feed", time="08:00", frequency="daily", priority=2)
   pet.add_task(task)
   assert len(pet.tasks) == initial_count + 1
