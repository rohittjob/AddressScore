from datetime import datetime, timedelta
from time import sleep, time



def get_now():
    return datetime.now()


def alarm(proc_name, set_time):
    print "Alarm set for '" + proc_name + "' at " + str(set_time)
    while True:
        if datetime.now() >= set_time:
            break
        remain = set_time - datetime.now()
        sleep(remain.seconds)
    print "Alarm Rings..."




def get_time():
    return datetime.now().time().strftime('%H:%M:%S')



# %%%%%%%%%%%%%%%%%%%%%%%%% EXECUTION TIME FUNCTIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


start_time = None
end_time = None


def time_taken():
    global start_time, end_time
    seconds = end_time - start_time
    minutes = seconds/60
    hours = int(minutes/60)
    minutes = int(minutes - hours*60)
    seconds = int(seconds - minutes*60 - hours*60*60)

    print 'Time to execute = ' + str(hours) + ':' + str(minutes) + ':' + str(seconds)


def start():
    global start_time
    start_time = time()


def stop():
    global end_time
    end_time = time()
    time_taken()