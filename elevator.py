#Effecient Elevator Path Application
#I chose python because of familiarity and the versatility of it acting as both a scripting language and general purpose


class User:
    def __init__(self, id, call_time, start_floor, destination_floor):
        self.id = id
        self.call_time = call_time
        self.start_floor = start_floor
        self.destination_floor = destination_floor

    def __repr__(self):
        return "{user: %d, call_time: %d, start_floor: %d, self.destination_floor: %d}" % (self.id, self.call_time, self.start_floor, self.destination_floor)

class Elevator:
    def __init__(self):
        total_users = int(input("Enter the number of users who will use the elevator: "))
        self.time = 1
        self.current_floor = 1
        self.floor_count = 0
        self.ordered_list = []
        users = []

        for i in range(1, total_users + 1):
            while True:
                try:
                    call_time = int(input("Enter the call time (priority) of user %d (1-5): " % (i)))
                    if call_time < 1 or call_time > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Error! Only priority values 1 through 5 are allowed!")

            while True:
                try:
                    start_floor = int(input("Enter the starting floor of user %d (1-5): " % (i)))
                    if start_floor < 1 or start_floor > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Error! Only floors 1 through 5 are allowed!")

            while True:
                try:
                    destination_floor = int(input("Enter the destination floor of user %d (1-5): " % (i)))
                    if destination_floor < 1 or destination_floor > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Error! Only floors 1 through 5 are allowed!")

            users.append(User(i, call_time, start_floor, destination_floor))
        print(users, '\n')
        print('ELEVATOR STARTING ON FLOOR 1')
        results = self.calc_order(users)
        if not self.ordered_list:
            print('\nNO MORE ELEVATOR USERS')
        print('TOTAL FLOORS TRAVELED: ', results)

    def calc_order(self, users_list):
        if not users_list:
            return self.floor_count
        for user in users_list[:]: #pick up user
            if user.call_time == self.time: #onboard users with time priority
                if user.start_floor == self.current_floor: #user is on the current floor
                    self.ordered_list.append(user)
                    users_list.remove(user)
                    print('PICKED UP USER', user.id, 'ON FLOOR', user.start_floor)
                else: #pick user up from their starting floor
                    print('TRAVELING TO USER', user.id, '...\n')
                    self.floor_count += (abs(user.start_floor - self.current_floor))
                    self.current_floor = user.start_floor
                    self.ordered_list.append(user)
                    users_list.remove(user)
                    print('PICKED UP USER', user.id, 'ON FLOOR', user.start_floor)
            else:
                continue

        while self.ordered_list: #drop off user
            for user in self.ordered_list[:]:
                target_floor = self.get_target_floor(self.ordered_list) #calc shortest distance to destination
                if user.destination_floor == target_floor:
                    self.floor_count += (abs(target_floor - self.current_floor))
                    self.current_floor = user.destination_floor
                    self.ordered_list.remove(user)
                    print('DROPPED OFF USER', user.id, 'ON FLOOR', self.current_floor)

        if len(users_list) > 0:
            self.time += 1
            self.calc_order(users_list) #repeat method for each priority until no users are left
        return self.floor_count

    def get_target_floor(self, list): #built to handle multiple users with the same call_times to determine shortest distance between them & current floor
        if not list:
            return
        dist_dict = {}
        for user in list:
            diff = (abs(user.destination_floor - self.current_floor))
            dist_dict.update({user.destination_floor: diff})
        floor = min(dist_dict, key = lambda k: dist_dict[k])
        return floor

Elevator()
