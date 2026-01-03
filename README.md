# CS310 - Movie Recommendation System
This is a group project for CS310 - Advanced Data Structures and Algorithms at UMass Boston. We were asked to solve a real world problem using algorithms discussed in class. Our group wanted to recommend movies, but only if they were on streaming services the user owned.

## How it works
We use a CSV file from [Kaggle](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) that contains the data required. We pre-processed the data so it only had the columns needed as well as added a column to track similarity.
Users input genre(s) and keyword(s) related to the movie they want to watch

## How to run it
```
# Clone the repo
git clone https://github.com/b-m-git-hub/cs310-movie-rec

# Navigate to the repo
cd cs310-movie-rec
```
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

To run the program and get recommendations:
```
python streaming_check.py (insert file name) --genres (insert genres) --keywords (insert keywords)
```
Remove parenthesis with actual names. An example input is below:
```
python streaming_check.py processed_movie_data.csv --genres action --keywords superhero city
```