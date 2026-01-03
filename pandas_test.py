import argparse
import math
import os
import pandas as pd
import re

def main():
    # Setup CLI.
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("filename")
    _ = parser.add_argument("--genres",   nargs="+", type=str)
    _ = parser.add_argument("--keywords", nargs="+", type=str)
    args = parser.parse_args()
    filename: str       = args.filename
    genres:   list[str] = args.genres   if args.genres   else []
    keywords: list[str] = args.keywords if args.keywords else []

    if not os.path.exists(filename):
        print(f"ERROR: file {filename} does not exist.")
        return

    if not genres and not keywords:
        print("ERROR: must provide genres or keywords")
        return

    # Read relevant columns from csv, drop NA values.
    df = pd.read_csv(
        filename, usecols=["id", "title", "genres", "keywords", "vote_average", "vote_count"], na_values=""
    )
    df = df.dropna(how="any")

    # Regex strings for genres / keywords.
    # Matches strings contain 1 or more genres / keywords.
    re_pat_genres_str  = "|".join(fr"\b{g}\b" for g in genres)   if genres   else r"(?!)"
    re_pat_keyword_str = "|".join(fr"\b{k}\b" for k in keywords) if keywords else r"(?!)"
    re_pat_genres   = re.compile(re_pat_genres_str,  re.IGNORECASE)
    re_pat_keywords = re.compile(re_pat_keyword_str, re.IGNORECASE)

    # Cache lengths to reduce function calls in similarity scoring.
    len_user_genres   = len(genres)
    len_user_keywords = len(keywords)

    # Jaccard similarity = |A & B| / (|A| + |B| - |A & B|)
    # - A = user  genres / keywords
    # - B = movie genres / keywords
    def jaccard(genres: str, keywords: str, vote_average: str, vote_count: str) -> float:
        # Regex to count matching genres / keywords.
        matching_genres   = sum(1 for _ in re.finditer(re_pat_genres,   genres))
        matching_keywords = sum(1 for _ in re.finditer(re_pat_keywords, keywords))
        count = matching_genres + matching_keywords
        # Jaccard formula.
        similarity = (
            count /
                (len_user_genres + len_user_keywords + len(genres.split(",")) + len(keywords.split(",")) - count)
        )
        # Scale similarity by rating and vote count.
        return similarity * (float(vote_average) / 10) * math.log10(int(vote_count) + 1)

    # List comprehension is faster than df.apply.
    df["similarity"] = [
        jaccard(g, k, va, vc) for g, k, va, vc in zip(df["genres"], df["keywords"], df["vote_average"], df["vote_count"])
    ]

    # Print top 10 most similar movies.
    df = df.sort_values("similarity", ascending=False)
    # print(df[["id", "title", "similarity", "genres", "keywords"]].head(10))
    return df

if __name__ == "__main__":
    main()
