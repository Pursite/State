from abc import ABC, abstractmethod


# State Interface
class ElevatorState(ABC):
    @abstractmethod
    def move(self, elevator):
        pass

    @abstractmethod
    def stop(self, elevator):
        pass


# Concrete States
class IdleState(ElevatorState):
    def move(self, elevator):
        if elevator.requested_floor > elevator.current_floor:
            elevator.set_state(MovingUpState())
        elif elevator.requested_floor < elevator.current_floor:
            elevator.set_state(MovingDownState())
        else:
            print("Elevator is already on the requested floor.")

    def stop(self, elevator):
        print("Elevator is already idle.")


class MovingUpState(ElevatorState):
    def move(self, elevator):
        if elevator.current_floor < elevator.max_floor:
            elevator.current_floor += 1
            print(f"Moving up to floor {elevator.current_floor}")
            if elevator.current_floor == elevator.requested_floor:
                elevator.set_state(IdleState())
        else:
            print("Reached the top floor.")
            elevator.set_state(IdleState())

    def stop(self, elevator):
        print("Stopping the elevator while moving up.")
        elevator.set_state(IdleState())


class MovingDownState(ElevatorState):
    def move(self, elevator):
        if elevator.current_floor > elevator.min_floor:
            elevator.current_floor -= 1
            print(f"Moving down to floor {elevator.current_floor}")
            if elevator.current_floor == elevator.requested_floor:
                elevator.set_state(IdleState())
        else:
            print("Reached the bottom floor.")
            elevator.set_state(IdleState())

    def stop(self, elevator):
        print("Stopping the elevator while moving down.")
        elevator.set_state(IdleState())


# Context
class Elevator:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        self.requested_floor = min_floor
        self.state = IdleState()

    def set_state(self, state):
        self.state = state

    def request_floor(self, floor):
        if floor < self.min_floor or floor > self.max_floor:
            print(f"Invalid floor request. Floor must be between {self.min_floor} and {self.max_floor}.")
            return
        self.requested_floor = floor
        self.state.move(self)

    def stop(self):
        self.state.stop(self)


# Example usage
if __name__ == "__main__":
    elevator = Elevator(min_floor=1, max_floor=10)

    elevator.request_floor(5)  # Moving up to floor 5
    elevator.request_floor(3)  # Moving down to floor 3
    elevator.request_floor(10)  # Moving up to floor 10
    elevator.request_floor(1)  # Moving down to floor 1
    elevator.request_floor(15)  # Invalid floor request