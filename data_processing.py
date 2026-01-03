import pandas as pd

file_path = "movie_data.csv"

def load_data(file_path):
    columns = ["id", "title", "genres", "keywords", "vote_count", "vote_average"]
    movieData = pd.read_csv(file_path, usecols=columns, na_values = "")
    movieData["similarity"] = 0.0
    return movieData

def main():
    movieData = load_data(file_path)
    movieData.to_csv("processed_movie_data.csv", index=False)
    print("Success")

if __name__ == "__main__":
    main()
