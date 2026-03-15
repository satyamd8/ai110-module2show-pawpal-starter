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
