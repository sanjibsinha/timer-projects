# creating a stopwatch
import time

def stopwatch():
    """
    Function to create a stopwatch.
    """
    start_time = time.time()
    print("Stopwatch started. Press CTRL+C to stop.")
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60) # Get the minutes and seconds
            print(f"{mins:02f}:{secs:02f}", end='\r') # Print the time in MM:SS format
            time.sleep(0.1) # Wait for 0.1 seconds
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")