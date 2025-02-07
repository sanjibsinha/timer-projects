import time

def countdown_timer(seconds):
    """
    Countdown timer for the given seconds.
    Args:
        seconds (int): Number of seconds to countdown.
    Returns:
        None
    """
    while seconds > 0:
        mins, secs = divmod(seconds, 60) # Get the minutes and seconds
        print(f"{mins:02d}:{secs:02d}", end='\r') # Print the time in MM:SS format
        time.sleep(1) # Wait for 1 second
        seconds -= 1 # Decrement the seconds
    print(f"00:00 - Time is up") # Print the final time