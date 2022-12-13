"""
...JSON classes are pydantic classes for working with Django models.

Classes have fields that are stored in db and affect salary.
"""
from pydantic import BaseModel


class WorkerJSON(BaseModel):
    status: str
    months_experience: int
    wage_rate: int


class SubjectJSON(BaseModel):
    title: str


class TeacherJSON(WorkerJSON):
    completed_courses: int
    has_classroom: bool
    subjects: list[SubjectJSON]
    course_increase: int
    service_years: int
    service_years_increase: int
    classroom_increase: int
    seniors_group_increase: int
    juniors_group_increase: int
    checking_notebooks_subjects: list[SubjectJSON]
    checking_notebooks_increase: int
    students_number_needed_for_increase_for_checking_notebooks: int


class CookJSON(WorkerJSON):
    is_chief: bool
    chief_increase: int
