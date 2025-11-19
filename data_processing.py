import pandas as pd

file_path = 'processed_movie_data.csv'

def load_data(file_path):
    #columns = ['id', 'title', 'genres', 'keywords', 'popularity']
    movieData = pd.read_csv(file_path) #usecols=columns
    return movieData

def main():
    movieData = load_data(file_path)
    pd.set_option('display.max_columns', None)
    #pd.reset_option('display.max_columns', None)
    print(movieData.head())

if __name__ == "__main__":
    main()
