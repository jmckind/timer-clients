#!/usr/bin/env python

from datetime import datetime, timedelta
import argparse, re, sys

class CountdownCommand(object):
    def __init__(self, options):
        self.delta = None
        self._parse_duration(options.duration.lower())

    def execute(self):
        self.start = datetime.now()
        self.end = self.start + self.delta

        print(self.start - )
        print(self.delta)
        while datetime.now() < self.end:
            remaining = timedelta(seconds=int(datetime.utcnow().time()))
            print("remaining: {}".format(remaining))

    def _parse_duration(self, duration):
        match = re.match('^([0-9]+)(mc|ms|s|m|h)$', duration, flags=re.IGNORECASE)
        if not match:
            raise ValueError('invalid duration')

        value = int(match.group(1))
        unit = str(match.group(2)).lower()

        if unit == 'mc':
            self.delta = timedelta(microseconds=value)
        elif unit == 'ms':
            self.delta = timedelta(milliseconds=value)
        elif unit == 's':
            self.delta = timedelta(seconds=value)
        elif unit == 'm':
            self.delta = timedelta(minutes=value)
        elif unit == 'h':
            self.delta = timedelta(hours=value)

def main():
    parser = argparse.ArgumentParser(description='A simple countdown timer')
    parser.add_argument('duration', help='the duration for the countdown timer')

    cmd = CountdownCommand(parser.parse_args())
    cmd.execute()

if __name__ == "__main__":
    main()
