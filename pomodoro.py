#!/usr/bin/env python3
"""Simple command-line Pomodoro timer."""
import time
import argparse
import sys

def countdown(seconds, label):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{label} {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print(f"{label} 00:00", end='\r')
    print()

def pomodoro(work, short_break, long_break, cycles):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}: Focus for {work // 60} minutes")
        countdown(work, "Work  ")
        if cycle < cycles:
            print(f"Take a short break for {short_break // 60} minutes")
            countdown(short_break, "Break ")
        else:
            print(f"Time for a long break: {long_break // 60} minutes")
            countdown(long_break, "Break ")
    print("Pomodoro session complete! Good job.")

def main():
    parser = argparse.ArgumentParser(description="Simple Pomodoro Timer")
    parser.add_argument("--work", type=int, default=25, help="Work duration in minutes")
    parser.add_argument("--short-break", type=int, default=5, help="Short break duration in minutes")
    parser.add_argument("--long-break", type=int, default=15, help="Long break duration in minutes")
    parser.add_argument("--cycles", type=int, default=4, help="Number of work sessions before the long break")
    args = parser.parse_args()

    work_sec = args.work * 60
    short_break_sec = args.short_break * 60
    long_break_sec = args.long_break * 60

    try:
        pomodoro(work_sec, short_break_sec, long_break_sec, args.cycles)
    except KeyboardInterrupt:
        print("\nTimer interrupted.")
        sys.exit(0)

if __name__ == "__main__":
    main()
