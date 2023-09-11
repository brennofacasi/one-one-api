from src.usecases.ports import MentorRepository


class InMemoryMentorRepository(MentorRepository):
    def __init__(self):
        self.mentors = []

    def add(self, mentor):
        self.mentors.append(mentor)

    def find_by_email(self, mentor_email):
        for mentor in self.mentors:
            if mentor.email == mentor_email:
                return mentor

    def find_all(self):
        return self.mentors
