import datetime as dt


class GetMentorAvailableSlots:
    def __init__(self, mentor_id, week_starts, week_ends, slot_duration,
                 availability_repository, slot_repository):
        self.mentor_id = mentor_id
        self.week_starts = week_starts
        self.week_ends = week_ends
        self.slot_duration = slot_duration
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

    def __daterange(self):
        """
        Returns dates within a range.
        """
        start_date = self.week_starts
        end_date = self.week_ends

        for n in range(int((end_date - start_date).days)):
            yield start_date + dt.timedelta(n)
        yield end_date

    def __get_available_time_slots(self, date: dt.datetime, start_time: dt.time, end_time: dt.time):
        """
        Get time slots based on duration and on the range of availability.
        """
        t_start = date.combine(date, start_time)
        t_end = date.combine(date, end_time)
        t_duration = dt.timedelta(minutes=self.slot_duration)

        slots = []

        period_start = t_start
        while period_start < t_end:
            period_end = min(period_start + t_duration, t_end)
            slots.append((period_start, period_end))
            period_start = period_end

        return slots

    def perform(self):
        # Get mentor's availability by their id
        availabilities = self.availability_repository.find_by_mentor_id(
            self.mentor_id)

        # Create empty list of slots
        nested_list_of_slots = []

        for availability in availabilities:
            # Get time range per available day
            from_time = availability.get_from_time()
            to_time = availability.get_to_time()

            list = []

            # For each weekday, append available slots to empty list
            for single_date in self.__daterange():
                if single_date.weekday() == availability.week_day:
                    result = self.__get_available_time_slots(
                        single_date, from_time, to_time)
                    list.append(result)

            nested_list_of_slots.append(self.__flatten_list(list))

        list_of_slots = self.__flatten_list(nested_list_of_slots)

        # Get slots from repository that are already taken
        slots_repository = self.slot_repository
        reserved_slots = slots_repository.find_by_mentor_id(self.mentor_id)

        # Remove taken slots from available slots
        for slot in reserved_slots:
            reserved = (slot.start_time, slot.end_time)
            if reserved in list_of_slots:
                list_of_slots.remove(reserved)

        return list_of_slots
