class Mentor:
    def __init__(self, first_name, last_name, email, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id

    def set_id(self, id):
        self.id = id
