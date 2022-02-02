import test_alerter
from abc import ABC, abstractmethod


global celcius_threshold, alert_failure_count
celcius_threshold = 100
alert_failure_count = 0

class abstraction(ABC):
    @abstractmethod
    def network_alert_stub(self):
        pass

class network_real_implementation(abstraction):
    def network_alert_stub(self,celcius):
        global celcius_threshold
        print('Call from real Implementation')
        print(f'ALERT: Temperature is {celcius} celcius')
        # Return 200 for ok
        # Return 500 for not-ok
        # stub always succeeds and returns 200
        if celcius<celcius_threshold:
            return 200
        else:
            return 500

class network_stub_testing(abstraction):
    def network_alert_stub(self,celcius):
        global celcius_threshold
        print('Call from stub for testing')
        print(f'ALERT: Temperature is {celcius} celcius')
        # Return 200 for ok
        # Return 500 for not-ok
        # stub always succeeds and returns 200
        if celcius<celcius_threshold:
            return 200
        else:
            return 500
    
class Alerter:
    def __init__(self, farenheit, a:abstraction):
        self.farenheit = farenheit
        self.network = a
        
    def convert_farenheit_to_celcius(self):
        return ((self.farenheit - 32) * 5 / 9)
    
    def alert_in_celcius(self):
        self.celcius = self.convert_farenheit_to_celcius()
    
        self.returnCode = self.network.network_alert_stub(self.celcius)

        
        if self.returnCode != 200:
            # non-ok response is not an error! Issues happen in life!
            # let us keep a count of failures to report
            # However, this code doesn't count failures!
            # Add a test below to catch this bug. Alter the stub above, if needed.
            global alert_failure_count
            alert_failure_count += 0

if __name__ == '__main__':
    real_network_object = network_real_implementation()
    #Test with real network implementation 
    alerter_object_1 = Alerter(400.5, real_network_object)
    alerter_object_1.alert_in_celcius()
    alerter_object_1 = Alerter(303.6, real_network_object)
    alerter_object_1.alert_in_celcius()
    print(f'{alert_failure_count} alerts failed.')
    assert(alert_failure_count==2)
    print('All is well (maybe!)')

    stub_network_object = network_stub_testing()
    #Test with real network implementation 
    alerter_object_3 = Alerter(400.5, stub_network_object)
    alerter_object_3.alert_in_celcius()
    alerter_object_4 = Alerter(303.6, stub_network_object)
    alerter_object_4.alert_in_celcius()
    print(f'{alert_failure_count} alerts failed.')
    assert(alert_failure_count==2)
    print('All is well (maybe!)')
