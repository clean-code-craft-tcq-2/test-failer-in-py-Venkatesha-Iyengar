import test_alerter

alert_failure_count = 0
flag_run_from_main_code= False

def network_alert_temporary_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    if flag_run_from_main_code:
        returnCode = network_alert_temporary_stub(celcius)

    else:
        #Running from some other script(Test-Script)
        returnCode = test_alerter.network_alert_stub(celcius)
        
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0

if __name__ == '__main__':
    flag_run_from_main_code = True
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)
    print(f'{alert_failure_count} alerts failed.')
    assert(alert_failure_count>0)
    print('All is well (maybe!)')
