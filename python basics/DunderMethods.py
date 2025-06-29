class students:
    def __init__(self, name: str, cohort: int, grade: float) -> None:
        self.name = name
        self.cohort = cohort
        self.grade = grade
    def __str__(self) -> str:
        return f'student {self.name} from {self.cohort} cohort has {self.grade} grade'
student: students = students('kevin', 4, 9.9)
print(student)
