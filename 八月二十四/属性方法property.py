class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print('connercting airline company api.....')
        print(f'checking flight {self.flight_name} status')
        return 1


    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 0:
            print('flight got canceled')
        elif status == 1:
            print('flight is arrived')
        elif status == 2:
            print('flight has departured already')
        else:
            print('cannot confirm the flight status...,please check later')

    @flight_status.setter
    def flight_status(self, status):
        print(f'changing flight status = {status}')


f = Flight('Ford')
f.flight_status
f.flight_status = 2
f.flight_status


