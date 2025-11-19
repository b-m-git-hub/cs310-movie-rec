import pandas as pd
import numpy as np

file_path = 'processed_movie_data.csv'

def load_data(file_path):
    #columns = ['id', 'title', 'genres', 'keywords', 'popularity']
    movieData = pd.read_csv(file_path) #usecols=columns
    movieData['similarity'] = np.nan
    return movieData

def main():
    movieData = load_data(file_path)
    pd.set_option('display.max_columns', None)
    #pd.reset_option('display.max_columns', None)
    #movieData.to_csv('processed_movie_data.csv', index=False)
    print(movieData.head())

if __name__ == "__main__":
    main()
