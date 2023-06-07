def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    counter = 0
    for start_time, exit_time in permanence_period:
        if not isinstance(start_time, int) or not isinstance(exit_time, int):
            return None
        if start_time <= target_time <= exit_time:
            counter += 1
    return counter


#  peaple = len(permanence_period, target_time)
#  raise NotImplementedError
