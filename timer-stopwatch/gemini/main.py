import time
import argparse
import sys

# Module 1: Core Timing Functions
class Timer:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0.0

    def start(self):
        """Starts the timer."""
        if self._start_time is not None:
            raise ValueError("Timer is already running.")
        self._start_time = time.perf_counter()

    def stop(self):
        """Stops the timer and returns elapsed time."""
        if self._start_time is None:
            raise ValueError("Timer is not running.")
        self._elapsed_time += time.perf_counter() - self._start_time
        self._start_time = None
        return self._elapsed_time

    def elapsed(self):
        """Returns elapsed time without stopping the timer."""
        if self._start_time is None:
            return self._elapsed_time
        return self._elapsed_time + (time.perf_counter() - self._start_time)

    def reset(self):
        """Resets the timer."""
        self._start_time = None
        self._elapsed_time = 0.0


# Module 2: CLI Interface
def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="CLI Timer/Stopwatch")
    group = parser.add_mutually_exclusive_group() # Timer and stopwatch can not work at the same time
    group.add_argument("-t", "--timer", type=float, help="Set a timer for seconds")
    group.add_argument("-s", "--stopwatch", action="store_true", help="Start a stopwatch")
    return parser.parse_args()


def run_timer(seconds):
    """Runs a timer for the specified duration."""
    print(f"Timer set for {seconds} seconds...")
    time.sleep(seconds) # sleep function pauses the execution of the current thread for the given number of seconds.
    print("Time's up!")

def run_stopwatch():
    """Runs a stopwatch."""
    timer = Timer()
    timer.start()
    print("Stopwatch started. Press Enter to stop.")
   
    input()  # Wait for user input
    
    elapsed_time = timer.stop()
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


# Module 3: Main Application Logic
def main():
    """Main function to orchestrate the application."""
    args = parse_arguments()

    if args.timer:
        run_timer(args.timer)
    elif args.stopwatch:
        run_stopwatch()
    else:
        print("No action specified. Use -t or -s.")
        sys.exit(1) # Exit with error code 1


if __name__ == "__main__":
    main()