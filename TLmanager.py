import math

import detection

AVG_TIMES = {"car": 5, "bus": 9, "truck": 9, "motorcycle": 4}

DENUM = 2
EXTRA_TIME = 5
MULTIPLIER = .5


class TLmanager:
    def __init__(self):
        self.avg_time = AVG_TIMES
        self.allotment_queue = [1] * 4
        self.prev_alloted = None

    def get_alloted_time(self, vehicle_count: dict):
        # Vehicle_count should be in the format -
        # {"car": x, "bus": x, "truck": x, "motorcycle": x}

        car_count, car_time = self.avg_time["car"], vehicle_count["car"]
        bus_count, bus_time = self.avg_time["bus"], vehicle_count["bus"]
        truck_count, truck_time = self.avg_time["truck"], vehicle_count["truck"]
        motorcycle_count, motorcycle_time = self.avg_time["motorcycle"], vehicle_count["motorcycle"]

        alloted_time = (car_count * car_time +
                        bus_count * bus_time +
                        truck_count * truck_time +
                        motorcycle_time * motorcycle_count) / DENUM

        alloted_time = math.ceil(alloted_time) + 5

        return alloted_time

    def select_tl(self, allt_times: list):
        allt_wait_time = [allt * Qmul for allt, Qmul in zip(allt_times, self.allotment_queue)]
        max_allt = max(allt_wait_time)
        idx = allt_wait_time.index(max_allt)

        while idx == self.prev_alloted:
            allt_wait_time[idx] = 0
            idx = allt_wait_time.index(max(allt_wait_time))

        self.allotment_queue = [1 if i == idx else x + MULTIPLIER for i, x in enumerate(self.allotment_queue)]

        # print(self.allotment_queue)
        self.prev_alloted = idx
        return idx, allt_times[idx]

#
# class CreateGraph:
#     def __init__(self):

