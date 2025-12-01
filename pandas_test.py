import argparse
import pandas as pd
import numpy as np
import re

def main():
    # Setup CLI.
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("filename")
    _ = parser.add_argument("--genres",   nargs="+", type=str)
    _ = parser.add_argument("--keywords", nargs="+", type=str)
    args = parser.parse_args()
    filename: str       = args.filename
    genres:   list[str] = args.genres
    keywords: list[str] = args.keywords

    # Read relevant columns from csv, fill na values.
    # TODO: think more about how to cleanup data
    df = pd.read_csv(filename, usecols=["id", "title", "genres", "keywords", "vote_average", "vote_count"], na_values="")

    # Regex strings for genres / keywords.
    # Matches strings contain 1 or more genres / keywords.
    re_pat_genre   = "|".join(fr"\b{g}\b" for g in genres)
    re_pat_keyword = "|".join(fr"\b{k}\b" for k in keywords)

    # Calculate similarity, i.e. number of matching genres / keywords scaled by rating.
    # NOTE: is jaccard similarity necessary?
    # TODO: do more than number of matches?
    df["similarity"] = (
        (
            df["genres"].str.count(re_pat_genre,   re.IGNORECASE) * 0.3
        + df["keywords"].str.count(re_pat_keyword, re.IGNORECASE) * 0.7
        ) * (df["vote_average"] / 10) * np.log10(df["vote_count"])
    )

    # Print top 10 most similar movies.
    df = df.sort_values("similarity", ascending=False)
    print(df[["id", "title", "similarity"]].head(10))


if __name__ == "__main__":
    main()
