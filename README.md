# CS310 - Movie Recommendation System
This is a group project for CS310 - Advanced Data Structures and Algorithms at UMass Boston. We were asked to solve a real world problem using an algorithm discussed in class. Our group wanted to recommend movies, but only if they were on streaming services the user owned.

## How it works
We use a CSV file from [Kaggle](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) that contains the data required. We pre-processed the data so it only had the columns needed as well as added a column to track similarity.

The user can input genre(s) and keyword(s) related to the movie they want to watch. The user is then prompted to put the names of the streaming services they own. Movies in the data set are then checked and given a similarity score using Jaccard similarity. The Jaccard similarity is then scaled by vote count and vote score to ensure movies that are actually likely to be on streaming services are recommended. The data set is sorted by similarity scores using quicksort. The result is a data set of movies sorted by descending similarity score.

Each movie is then checked using the TMDB REST API to see if the user owned streaming services have the movie. Movies on the user owned services are put into a dictionary containing movie name and streaming service to watch it on. After 10 movies are added to the dictionary, it stops checking and returns the top 10 movies. Since the data set is sorted by similarity, the top 10 movies will be in descending order of most similar movies.

## How to run it
Clone the repo:
```
git clone https://github.com/b-m-git-hub/cs310-movie-rec
```
Navigate to the cloned repo:
```
cd cs310-movie-rec
```
It is recommened you download the CSV file from Kaggle linked above as that is the same data used for this project. Other data might have differently named columns and not properly work. If you plan on pre-processing the data using the data_processing.py file from this project, then you should name the data set as movie_data.csv when downloading it. Ensure the CSV file is within the cs310-movie-rec folder.

It is recommended you create a virtual environment before installing dependecies.
```
python -m venv venv
```
Activate the virtual environment.

For Windows:
```
.\venv\Scripts\activate
```
For Linux/Mac:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
You must use your own API key from TMDB. It is free to get and can be done by going to the API section of your TMDB account. Check out the [TMDB FAQ](https://developer.themoviedb.org/docs/faq) for more information.

Once you have your key, open the streaming_check.py file and find the line that says API_KEY = "YOUR_API_KEY_HERE". Replace YOUR_API_KEY_HERE with your actual API key. Make sure your API key is inside the quotations and ensure that you save the file.

An optional but recommended step is to pre-process the data using the data_processing.py file. The file requires you to rename your data set to movie_data.csv if you have not done so already. Feel free to edit data_processing.py by locating the line that says file_path = "movie_data.csv" and modifying it to the name of your data set CSV file.
```
python data_processing.py
```

To run the program and get recommendations, simply use one of the examples below. Replace the parentheses with additional genres and keywords separated by a space. Do not include parentheses.

If data_processing.py was used, then use the following format:
```
python streaming_check.py processed_movie_data.csv --genres (insert genres) --keywords (insert keywords)
```
Otherwise, a more general format:
```
python streaming_check.py (insert file name) --genres (insert genres) --keywords (insert keywords)
```

## Credits

**The Movie Database (TMDB)**: This product uses the TMDB API but is not endorsed or certified by TMDB.

    <img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg" alt="TMDB Logo" width="100">