# def parse_time(str_time):
    # '12:00:00'


import dateparser

f = open('sample.txt')
lines = f.readlines()
time_hash = {}

for line in lines:
    time_status = line.split('::')
    status = (time_status[1]).split('\n')[0]
    # print(status)
    # time = (time_status[0]).split('-')[1]
    # time = time.split(')')[0]
    # # print(time)
    # if status in time_hash:
    #     time_hash[status] -= parse_time(time)
    # else:
    #     time_hash[status] = time
    idx = 1
    time_hash[idx] = dateparser.parse(time_status[0])
    idx += 1


print(time_hash)
