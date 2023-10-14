import time
import schedule
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame
import fetching
import trips
import runner


# Global variables
release = 2023
firsturl = "https://www.imdb.com/search/title/?title_type=feature,tv_series&year=2023-01-01,2023-12-31&explore=countries&countries=IN"
recordsinimdb = 2200

def run_scraping_job():
    print("Starting scraping job...")
    start_time = time.time()
    runner.fetch('z1', firsturl, recordsinimdb, release)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Scraping job completed in {elapsed_time} seconds.")


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
