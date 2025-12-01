import pandas as pd

file_path = 'processed_movie_data.csv'

def load_data(file_path):
    # Read CSV file
    movieData = pd.read_csv(file_path)
    # Clean up if both the genre and keyword columns are empty
    movieData.dropna(subset=['genres', 'keywords'], how='all', inplace=True)
    return movieData

def main():
    movieData = load_data(file_path)
    # Shows all columns when printing
    pd.set_option('display.max_columns', None)
    # Saves the data, will overwrite the existing file
    movieData.to_csv('processed_movie_data.csv', index=False)
    print(movieData.head())

if __name__ == "__main__":
    main()
