from .binary import BinarySensor
from .numeric import NumericSensor


class MockBinarySensor(BinarySensor):
    """MockBinarySensor."""
    def __init__(self, name):
        super(MockBinarySensor, self).__init__(name)

    def update_state(self):
        self.state = not self.state


class MockNumericSensor(NumericSensor):
    """MockNumericSensor."""
    def __init__(self, name):
        super(MockNumericSensor, self).__init__(name)

    def update_value(self):
        self.value += 0.1
