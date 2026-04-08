#!/usr/bin/env python3
import sys


def validate_arg() -> None | list:
    """
    Validate arg and return it into a list
    """
    scores = []
    invalid_argv = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            invalid_argv.append(arg)
            continue
    len_invalid_argv = len(invalid_argv)
    if len_invalid_argv == len(sys.argv):
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return None
    if len_invalid_argv > 0:
        print(f"Invalid argument: {invalid_argv}")
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return None
    return (scores)


def score_analitics(scores: list[int]) -> None:
    """
    Calculate and display detailed statistics from a list of scores.
    """
    num_players = len(scores)
    total_scores = sum(scores)
    avarage_score = total_scores / num_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Score processed: {sys.argv[1:]}")
    print(f"Total playes: {num_players}")
    print(f"Total score: {total_scores}")
    print(f"Avarage score: {avarage_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    if len(sys.argv) > 2:
        score = validate_arg()
        if score is not None:
            score_analitics(score)
    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
