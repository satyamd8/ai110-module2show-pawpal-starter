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

def test_sort_by_time():
   tasks = [
      Task(description="Walk", time="09:00", frequency="daily", priority=2),
      Task(description="Feed", time="08:00", frequency="daily", priority=1),
      Task(description="Play", time="10:00", frequency="daily", priority=3),
   ]
   owner = Owner(name="Owner")
   pet = Pet(name="Pet", type="Dog")
   for t in tasks:
      pet.add_task(t)
   owner.add_pet(pet)
   scheduler = Scheduler(owner)
   sorted_tasks = scheduler.sort_by_time(tasks)
   times = [t.time for t in sorted_tasks]
   assert times == ["08:00", "09:00", "10:00"]

def test_organize_tasks_by_priority_and_time():
   tasks = [
      Task(description="Feed", time="09:00", frequency="daily", priority=2),
      Task(description="Walk", time="08:00", frequency="daily", priority=1),
      Task(description="Play", time="10:00", frequency="daily", priority=1),
   ]
   owner = Owner(name="Owner")
   pet = Pet(name="Pet", type="Dog")
   for t in tasks:
      pet.add_task(t)
   owner.add_pet(pet)
   scheduler = Scheduler(owner)
   organized = scheduler.organize_tasks(date.today())
   # Should be sorted by priority (1, 1, 2) and then by time (08:00, 10:00, 09:00)
   assert [t.description for t in organized] == ["Walk", "Play", "Feed"]

def test_detect_conflicts_same_time_same_pet():
   owner = Owner(name="Owner")
   pet = Pet(name="Pet", type="Dog")
   t1 = Task(description="Feed", time="08:00", frequency="daily", priority=1)
   t2 = Task(description="Walk", time="08:00", frequency="daily", priority=2)
   pet.add_task(t1)
   pet.add_task(t2)
   owner.add_pet(pet)
   scheduler = Scheduler(owner)
   warnings = scheduler.detect_conflicts(pet.tasks)
   assert any("08:00" in w for w in warnings)

def test_detect_conflicts_same_time_different_pets():
   owner = Owner(name="Owner")
   pet1 = Pet(name="Doggo", type="Dog")
   pet2 = Pet(name="Kitty", type="Cat")
   t1 = Task(description="Feed", time="09:00", frequency="daily", priority=1)
   t2 = Task(description="Feed", time="09:00", frequency="daily", priority=1)
   pet1.add_task(t1)
   pet2.add_task(t2)
   owner.add_pet(pet1)
   owner.add_pet(pet2)
   scheduler = Scheduler(owner)
   all_tasks = pet1.tasks + pet2.tasks
   warnings = scheduler.detect_conflicts(all_tasks)
   assert any("09:00" in w for w in warnings)

def test_filter_tasks_by_status_and_pet():
   owner = Owner(name="Owner")
   pet1 = Pet(name="Doggo", type="Dog")
   pet2 = Pet(name="Kitty", type="Cat")
   t1 = Task(description="Feed", time="07:00", frequency="daily", priority=1, status="completed")
   t2 = Task(description="Walk", time="08:00", frequency="daily", priority=2, status="pending")
   pet1.add_task(t1)
   pet2.add_task(t2)
   owner.add_pet(pet1)
   owner.add_pet(pet2)
   scheduler = Scheduler(owner)
   filtered = scheduler.filter_tasks(pet1.tasks + pet2.tasks, status="completed", pet_name="Doggo")
   assert filtered == [t1]

def test_empty_tasks():
   owner = Owner(name="Owner")
   pet = Pet(name="Pet", type="Dog")
   owner.add_pet(pet)
   scheduler = Scheduler(owner)
   assert scheduler.organize_tasks(date.today()) == []

# Recurrence logic: simulate daily recurrence by adding tasks for multiple days
def test_recurrence_daily_tasks():
   owner = Owner(name="Owner")
   pet = Pet(name="Pet", type="Dog")
   # Simulate adding a daily recurring task for 3 days
   for i in range(3):
      d = date(2026, 3, 15 + i)
      task = Task(description="Feed", time="08:00", frequency="daily", priority=1)
      pet.add_task(task)
   owner.add_pet(pet)
   scheduler = Scheduler(owner)
   all_tasks = scheduler.get_tasks_for_date(date(2026, 3, 16))
   # Should include a task for the 16th
   assert any(t for t in all_tasks if t.description == "Feed")
