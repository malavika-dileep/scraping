# scheduler.py

import time
import schedule
import pandas as pd
from fetching import gettingdata
from trips import tripone

# Global variables
release = 2023
firsturl = "https://www.imdb.com/search/title/?title_type=feature,tv_series&year=2023-01-01,2023-12-31&explore=countries&countries=IN"
recordsinimdb = 2200

# Function to run the scraping job
def run_scraping_job():
    print("Starting scraping job...")
    try:
        # Call fetching.gettingdata to get TTN numbers
        movies_from_scrape = gettingdata(release, firsturl)
        
        # Read the existing CSV file
        existing_ttns = set(pd.read_csv('z1.csv')['TTN'].tolist())
        
        # Filter TTN numbers that are not in the CSV
        new_ttns = [movie[0] for movie in movies_from_scrape if movie[0] not in existing_ttns]
        
        # If there are new TTN numbers, get the full movie details
        new_movies = []
        if new_ttns:
            for ttn in new_ttns:
                movie_details = gettingdata(release, ttn)  # Assuming gettingdata can accept TTN and fetch details
                if movie_details:
                    new_movies.append(movie_details)
            print(f"Scraped {len(new_movies)} new movies.")
            # Print or process new movie details as needed
            for movie in new_movies:
                print("Movie Details:", movie)
        else:
            print("No new movies to scrape.")
    except Exception as e:
        print(f"An error occurred during scraping: {str(e)}")

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
