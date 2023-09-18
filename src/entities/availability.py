import datetime as dt


class Availability:
    def __init__(self, mentor_id, week_day, from_time, to_time, id=None):
        self.mentor_id = mentor_id
        self.week_day = week_day
        self.from_time = from_time
        self.to_time = to_time
        self.id = id

    def get_from_time(self):
        return dt.datetime.strptime(self.from_time, '%H:%M:%S').time()

    def get_to_time(self):
        return dt.datetime.strptime(self.to_time, '%H:%M:%S').time()

    def set_id(self, id):
        self.id = id
