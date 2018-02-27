#!/usr/bin/env python
import time
import pprint as pp
import sensors


class Guardian(object):
    """HomeGuardian is a security system for python"""
    def __init__(self):
        super(Guardian, self).__init__()
        self.binary_sensors_names = [
            "bsensor1", "bsensor2", "bsensor3"
        ]
        self.numeric_sensors_names = [
            "nsensor1", "nsensor2", "nsensor3"
        ]
        self.numeric_sensors = []
        self.binary_sensors = []
        self.sensors = {}
        self.sensors["binary"] = {}
        self.sensors["numeric"] = {}

    def create_sensors(self):
        for name in self.numeric_sensors_names:
            self.numeric_sensors.append(
                sensors.mocksensors.MockNumericSensor(name)
            )
        for name in self.binary_sensors_names:
            self.binary_sensors.append(
                sensors.mocksensors.MockBinarySensor(name)
            )
        pass

    def get_state(self):
        # update sensors
        for sensor in self.binary_sensors:
            sensor.update_state()
            self.sensors["binary"][sensor.name] = sensor.get_state()

        for sensor in self.numeric_sensors:
            sensor.update_value()
            self.sensors["numeric"][sensor.name] = sensor.get_value()
        return self.sensors

    def main(self):
        # crearsensores
        self.create_sensors()
        while True:
            state = self.get_state()
        #       if condiciones:
        #           notificar()
        #       sleep(1)
            pp.pprint(state, indent=4,width=30)
            for bs in self.sensors["binary"]:
                if self.sensors["binary"][bs]:
                    print "*",
                else:
                    print ".",
            print
            time.sleep(1)
        pass

if __name__ == '__main__':
    guardian = Guardian()
    guardian.main()
