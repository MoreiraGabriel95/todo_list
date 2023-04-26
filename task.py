class Task:
    def __init__(self, description, deadline, language):
        self.description = description
        self.deadline = deadline
        self.completed = False
        self.language = language

    def __str__(self):
        if self.completed:
            status = f"[x] {self.description}"
        else:
            status = f"[ ] {self.description}"
        return f"{status} - Deadline: {self.deadline}"

    def toggle_completion(self):
        self.completed = not self.completed

    def to_dict(self):
        return {
            "description": self.description,
            "deadline": self.deadline,
            "completed": self.completed,
            "language": self.language
        }

