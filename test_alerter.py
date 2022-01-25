import alerter

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 500

if __name__ == '__main__':
    alerter.alert_in_celcius(400.5)
    alerter.alert_in_celcius(303.6)
    print(f'{alerter.alert_failure_count} alerts failed.')
    assert(alerter.alert_failure_count>0)
    print('All is well (maybe!)')
