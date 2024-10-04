from time import localtime, time, sleep


class clock():
    def __init__(self,hour = 0,minute = 0,second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @classmethod
    def now(cls):
        clock_now = localtime(time())
        return cls(clock_now.tm_hour,clock_now.tm_min,clock_now.tm_sec)

    def run(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour}:{self.minute}:{self.second}'


def main():
    clock1 = clock.now()
    while True:
        print(clock1.show())
        sleep(1)
        clock1.run()

if __name__ == '__main__':
    main()