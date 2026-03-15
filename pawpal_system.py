from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

@dataclass
class Pet:
   name: str
   type: str

@dataclass
class Task:
   name: str
   duration: int  # in minutes
   priority: int

class Owner:
   def __init__(self, name: str, preferences: Optional[str] = None):
      self.name = name
      self.preferences = preferences
      self.pet: Optional[Pet] = None
      self.tasks: List[Task] = []

   def add_pet(self, pet: Pet):
      self.pet = pet

   def add_task(self, task: Task):
      self.tasks.append(task)

class Schedule:
   def __init__(self, date_: date, tasks: Optional[List[Task]] = None):
      self.date = date_
      self.tasks = tasks if tasks else []

   def generate_plan(self):
      # Placeholder for scheduling logic
      pass

   def explain_plan(self):
      # Placeholder for explanation logic
      pass
