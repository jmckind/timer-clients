#!/usr/bin/env python

from datetime import datetime, timedelta
import argparse, re, sys

class CountdownCommand(object):
    def __init__(self, options):
        self.weeks = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        print(options)
        self._parse_options(options)

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

    def _parse_options(self, options):
        regex = re.compile('^([0-9]+)(ms|s|m|h|d|w)$', flags=re.IGNORECASE)

        for option in options:
            match = regex.match(option)
            value = int(match.group(1))
            unit = str(match.group(2)).lower()

            if unit == 's':
                self.seconds = value
            elif unit == 'm':
                self.minutes = value
            elif unit == 'h':
                self.hours = value
            elif unit == 'd':
                self.days = value
            elif unit == 'w':
                self.weeks = value

def main():
    if len(sys.argv) <= 1:
        raise ValueError('invalid duration')

    cmd = CountdownCommand(sys.argv[1:])
    cmd.execute()

if __name__ == "__main__":
    main()
