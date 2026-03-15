from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Task:
   description: str
   time: str
   frequency: str
   priority: int
   status: str = "pending"
   completion_time: Optional[str] = None

@dataclass
class Pet:
   name: str
   type: str
   tasks: List[Task] = field(default_factory=list)

   def add_task(self, task: Task):
      self.tasks.append(task)

   def get_tasks(self) -> List[Task]:
      return self.tasks

class Owner:
   def __init__(self, name: str, preferences: Optional[str] = None):
      self.name = name
      self.preferences = preferences
      self.pets: List[Pet] = []

   def add_pet(self, pet: Pet):
      self.pets.append(pet)

   def get_all_tasks(self) -> List[Task]:
      tasks = []
      for pet in self.pets:
         tasks.extend(pet.get_tasks())
      return tasks

   def get_tasks_for_date(self, date_: date) -> List[Task]:
      return self.get_all_tasks()

class Scheduler:
   def detect_conflicts(self, tasks: List[Task]) -> List[str]:
      """Detects if two or more tasks are scheduled at the same time for the same or different pets."""
      warnings = []
      time_to_tasks = {}
      for pet in self.owner.pets:
         for task in pet.tasks:
            key = (task.time, pet.name)
            if task.time not in time_to_tasks:
               time_to_tasks[task.time] = []
            time_to_tasks[task.time].append((pet.name, task.description))
      # Check for conflicts (same time, more than one task)
      for time, task_list in time_to_tasks.items():
         if len(task_list) > 1:
            pets = ', '.join([f"{pet} ({desc})" for pet, desc in task_list])
            warnings.append(f"Conflict at {time}: Multiple tasks scheduled for {pets}.")
      return warnings
   
   def sort_by_time(self, tasks: List[Task]) -> List[Task]:
      """Sorts tasks by their time attribute (HH:MM format)."""
      return sorted(tasks, key=lambda t: t.time)

   def filter_tasks(self, tasks: List[Task], status: Optional[str] = None, pet_name: Optional[str] = None) -> List[Task]:
      """Filters tasks by completion status and/or pet name."""
      filtered = tasks
      if status is not None:
         filtered = [t for t in filtered if t.status == status]
      if pet_name is not None:
         # Find tasks belonging to the specified pet
         filtered = [t for t in filtered if any(pet.name == pet_name and t in pet.tasks for pet in self.owner.pets)]
      return filtered
   
   def __init__(self, owner: Owner):
      self.owner = owner

   def get_tasks_for_date(self, date_: date) -> List[Task]:
      return self.owner.get_tasks_for_date(date_)

   def organize_tasks(self, date_: date) -> List[Task]:
      tasks = self.get_tasks_for_date(date_)
      return sorted(tasks, key=lambda t: (t.priority, t.time))

   def mark_task_completed(self, task: Task, completion_time: Optional[str] = None):
      task.status = "completed"
      task.completion_time = completion_time

   def explain_plan(self, date_: date) -> str:
      return "Tasks are scheduled by priority and time."
