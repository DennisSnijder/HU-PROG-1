import datetime

runners = open('runners.txt', 'a')

hours: str = input('How many hours ? : ')
minutes: str = input('How many minutes? : ')
seconds: str = input('How many seconds? : ')
name: str = input('Name : ')

formatted_time: datetime = datetime.datetime(2017, 9, 23, int(hours), int(minutes), int(seconds))

runners.write(str(formatted_time) + ", " + name + '\n')
runners.close()
