class GetAvailabilities:
    def __init__(self, availabilities_repository):
        self.availabilities_repository = availabilities_repository

    def execute(self):
        repository = self.availabilities_repository
        return repository.get_all()
