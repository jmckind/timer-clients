
from datetime import datetime, timedelta
from timer_clients import BaseTimer

class CountdownTimer(BaseTimer):
    def __init__(self, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def execute(self):
        self.start = datetime.now()
        self.end = self.start + timedelta(
            weeks=self.weeks,
            days=self.days,
            hours=self.hours,
            minutes=self.minutes,
            seconds=self.seconds
        )

        print("start: {}".format(self.start))
        print("  end: {}".format(self.end))

        while True:
            now = datetime.now()
            if now >= self.end:
                break

            print("remaining: {}".format(self.end - now))
