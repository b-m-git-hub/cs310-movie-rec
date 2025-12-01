import argparse
import math
import pandas as pd
import numpy as np
import re

def main():
    # Setup CLI.
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("filename")
    _ = parser.add_argument("--genres",   nargs="+", type=str)
    _ = parser.add_argument("--keywords", nargs="+", type=str)
    _ = parser.add_argument("--all",      action="store_true")
    args = parser.parse_args()
    filename: str       = args.filename
    genres:   list[str] = args.genres   if args.genres   else []
    keywords: list[str] = args.keywords if args.keywords else []
    all_terms = args.all

    # Read relevant columns from csv, drop NA values.
    df = pd.read_csv(
        filename, usecols=["id", "title", "genres", "keywords", "vote_average", "vote_count"], na_values=""
    )
    df = df.dropna(how="any")

    # Regex strings for genres / keywords.
    # Matches strings contain 1 or more genres / keywords.
    re_pat_genre_or   = "|".join(fr"\b{g}\b" for g in genres) if genres else r"(?!)"
    re_pat_keyword_or = "|".join(fr"\b{k}\b" for k in keywords) if keywords else r"(?!)"

    # Calculate similarity, i.e. number of matching genres / keywords scaled by rating.
    # NOTE: Probably shouldn't just scale by log(votes)
    df["similarity"] = (
        (
            df["genres"].str.count(re_pat_genre_or,   re.IGNORECASE) * 0.3
        + df["keywords"].str.count(re_pat_keyword_or, re.IGNORECASE) * 0.7
        ) * (df["vote_average"] / 10) * np.log10(df["vote_count"])
    )

    # len_user_genres   = len(genres)
    # len_user_keywords = len(keywords)
    # re_pat_genres   = re.compile(re_pat_genre_or,   re.IGNORECASE)
    # re_pat_keywords = re.compile(re_pat_keyword_or, re.IGNORECASE)
    #
    # # Jaccard similarity = |A & B| / (|A| + |B| - |A & B|)
    # # - A = user  genres / keywords
    # # - B = movie genres / keywords
    # def jaccard(genres: str, keywords: str, vote_average: str, vote_count: str) -> float:
    #     matching_genres   = sum(1 for _ in re.finditer(re_pat_genres,   genres))
    #     matching_keywords = sum(1 for _ in re.finditer(re_pat_keywords, keywords))
    #     count = matching_genres + matching_keywords
    #     # Hacky way to only count movies that match all genres / keywords.
    #     # Doesn't work well lol.
    #     if all_terms:
    #         matching_genres   = len_user_genres   if matching_genres   == len_user_genres   else 0
    #         matching_keywords = len_user_keywords if matching_keywords == len_user_keywords else 0
    #     similarity = (
    #         (matching_genres + matching_keywords) /
    #             (len_user_genres + len_user_keywords + len(genres.split(",")) + len(keywords.split(",")) - count)
    #     )
    #     # Scaling similarity by rating and vote count.
    #     # Also doesn't work well...
    #     return similarity * (float(vote_average) / 10) * math.log10(int(vote_count) + 1)
    #
    # # List comprehension is faster than df.apply.
    # df["similarity"] = [
    #     jaccard(g, k, va, vc) for g, k, va, vc in zip(df["genres"], df["keywords"], df["vote_average"], df["vote_count"])
    # ]

    # Print top 10 most similar movies.
    df = df.sort_values("similarity", ascending=False)
    print(df[["id", "title", "similarity", "genres", "keywords"]].head(10))


if __name__ == "__main__":
    main()
