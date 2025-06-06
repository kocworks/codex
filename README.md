# Pomodoro Timer

This repository contains a simple command-line Pomodoro timer written in Python.

## Usage

Run the script using Python 3:

```bash
python3 pomodoro.py [options]
```

Options:

- `--work`: work duration in minutes (default: 25)
- `--short-break`: short break duration in minutes (default: 5)
- `--long-break`: long break duration in minutes (default: 15)
- `--cycles`: number of work sessions before the long break (default: 4)

Example:

```bash
python3 pomodoro.py --work 25 --short-break 5 --long-break 15 --cycles 4
```

Press `Ctrl+C` to interrupt the timer.
