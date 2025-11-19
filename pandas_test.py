import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("filename")
    _ = parser.add_argument("--genres", nargs="+", type=str)
    _ = parser.add_argument("--keywords", nargs="+", type=str)
    args = parser.parse_args()
    filename = args.filename
    genres = args.genres
    keywords = args.keywords

    df = pd.read_csv(filename, usecols=["id", "title", "genres", "keywords"])

    # filtered_df = df[df["genres"].str.contains(genre.capitalize(), na=False)]
    # filtered_df = df[df["keywords"].str.contains(keyword.lower(), na=False)]
    # print(df.loc[(df["genres"].str.contains(genre.capitalize(), na=False)) & (df["keywords"].str.contains(keyword.lower(), na=False))])
    print(
        df.loc[
            df["genres"].str.contains("".join([fr"(?=.*\b{g}\b)" for g in genres]), regex=True, na=False, case=False)
            & df["keywords"].str.contains("".join([fr"(?=.*\b{k}\b)" for k in keywords]), regex=True, na=False, case=False)
        ]
    )
    # print(df)


if __name__ == "__main__":
    main()
