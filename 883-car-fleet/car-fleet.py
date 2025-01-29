class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first element is the closest car
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleetStack = []

        for car in cars:
            if len(fleetStack) == 0:
                fleetStack.append(car)
                continue
            
            currentCarDuration = (target - car[0]) / car[1] # float division
            limitingCarDuration =  (target - fleetStack[-1][0]) / fleetStack[-1][1]

            if currentCarDuration > limitingCarDuration:
                fleetStack.append(car) # current car is the latest limiting car
            else:
                continue # it joins the fleet
        
        return len(fleetStack)