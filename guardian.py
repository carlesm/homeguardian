#!/usr/bin/env python
import time

import sensors


class Guardian(object):
    """HomeGuardian is a security system for python"""
    def __init__(self):
        super(Guardian, self).__init__()

    def create_sensors(self):
        self.mbs = sensors.mocksensors.MockBinarySensor("sensor1")
        self.mns = sensors.mocksensors.MockNumericSensor("sensor2")
        pass

    def get_state(self):
        # update sensors
        self.mbs.update_state()
        self.mns.update_value()
        # get values from sensors
        value1 = self.mbs.get_state()
        value2 = self.mns.get_value()
        return (value1, value2)

    def main(self):
        # crearsensores
        self.create_sensors()
        while True:
            state = self.get_state()
        #       if condiciones:
        #           notificar()
        #       sleep(1)
            print(state)
            time.sleep(1)
        pass

if __name__ == '__main__':
    guardian = Guardian()
    guardian.main()
