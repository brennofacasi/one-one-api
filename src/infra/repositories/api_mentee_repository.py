import requests
from src.entities import Mentee
from src.usecases.ports import MenteeRepository


class ApiMenteeRepository(MenteeRepository):
    def __init__(self):
        res = requests.get(
            'https://dummyjson.com/users?limit=15&select=firstName,lastName,email,company')
        data = res.json()
        self.users = data['users']

    def get_all(self):
        result = []
        for user in self.users:
            mentee = Mentee(user['firstName'], user['lastName'],
                            user['email'], user['company']['name'])
            result.append(mentee.toJSON(user['id']))
        return result

    def find_by_email(self, email):
        # TO DO - Implement
        return super().find_by_email(email)

    def find_by_id(self, id):
        # TO DO - Implement
        return super().find_by_id(id)
