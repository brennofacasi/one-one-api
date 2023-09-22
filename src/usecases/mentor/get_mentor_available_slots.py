import datetime as dt


class GetMentorAvailableSlots:
    def __init__(self, availability_repository, slot_repository):
        self.availability_repository = availability_repository
        self.slot_repository = slot_repository

    def __flatten_list(self, matrix):
        """
        Flattens nested lists.
        """
        flat_list = []
        for row in matrix:
            flat_list.extend(row)
        return flat_list

    def __daterange(self, start_date, end_date):
        """
        Returns dates within a range.
        """
        for n in range(int((end_date - start_date).days)):
            yield start_date + dt.timedelta(n)
        yield end_date

    def __get_available_time_slots(self, date, start_time, end_time, slot_duration):
        """
        Get time slots based on duration and on the range of availability.
        """
        t_start = date.combine(date, start_time)
        t_end = date.combine(date, end_time)

        t_duration = dt.timedelta(minutes=slot_duration)

        slots = []

        period_start = t_start
        while period_start < t_end:
            period_end = min(period_start + t_duration, t_end)
            slots.append((period_start, period_end))
            period_start = period_end + dt.timedelta(minutes=10)

        return slots

    def execute(self, mentor_id, week_starts, week_ends, slot_duration):
        # Get mentor's availability by their id
        availabilities = self.availability_repository.find_by_mentor_id(
            mentor_id)

        # Create empty list of slots
        nested_list_of_slots = []

        for availability in availabilities:
            # Get time range per available day
            from_time = availability.from_time
            to_time = availability.to_time

            list = []

            # For each weekday, append available slots to empty list
            for single_date in self.__daterange(week_starts, week_ends):
                if single_date.weekday() == availability.week_day:
                    result = self.__get_available_time_slots(
                        single_date, from_time, to_time, slot_duration)
                    list.append(result)

            nested_list_of_slots.append(self.__flatten_list(list))

        list_of_slots = self.__flatten_list(nested_list_of_slots)

        # Get slots from repository that are already taken
        slots_repository = self.slot_repository
        reserved_slots = slots_repository.find_by_mentor_id(mentor_id)

        # Remove taken slots from available slots
        for slot in reserved_slots:
            reserved = (slot.start_time, slot.end_time)
            if reserved in list_of_slots:
                list_of_slots.remove(reserved)

        return list_of_slots
