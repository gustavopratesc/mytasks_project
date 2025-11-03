class Task:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def mark_as_completed(self):
        self.status = True

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status
        }