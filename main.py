
from scraper import read_imdb_csv
from fetcher import fetch_metadata
from cleaner import clean_data
from eda import eda
from hypothesis_tests import test_hypotheses
from visualizer import visualization
from advanced_eda import eda_and_analysis

def main():
    try:
        # Step 1: Read IMDb ratings from CSV
        file_path = 'mylist.csv'  # Adjust the path as needed
        print("Reading IMDb ratings from CSV...")
        ratings_df = read_imdb_csv(file_path)
        print("CSV reading completed.")
        print(ratings_df.head())

        # Step 2: Fetch metadata using IMDbPY
        print("Fetching metadata from IMDb...")
        metadata_df = fetch_metadata(ratings_df)
        print("Metadata fetching completed.")

        # Step 3: Clean the data
        print("Cleaning the data...")
        cleaned_df = clean_data(metadata_df)
        print("Data cleaning completed.")

        # Step 4: Perform exploratory data analysis (EDA)
        print("Performing Exploratory Data Analysis...")
        eda(cleaned_df)
        print("EDA completed.")

        # Step 5: Perform advanced EDA and analysis
        print("Performing Advanced EDA and Analysis...")
        eda_and_analysis(cleaned_df)
        print("Advanced EDA and Analysis completed.")

        # Step 6: Test hypotheses
        print("Testing hypotheses...")
        test_hypotheses(cleaned_df)
        print("Hypothesis testing completed.")

        # Step 7: Extended visualization
        print("Creating extended visualizations...")
        visualization(cleaned_df)
        print("Visualizations completed.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()