# main.py

import time
import schedule
import pandas as pd
from scheduler import run_scraping_job  # Import the function from scheduler.py

def main():
    # Schedule the scraping job to run every 12 hours
    schedule.every(12).hours.do(run_scraping_job)

    # Run the scraping job once initially
    run_scraping_job()

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("Keyboard interrupt. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
