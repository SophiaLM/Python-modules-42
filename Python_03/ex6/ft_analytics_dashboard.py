#!/usr/bin/env python3


def get_game_data() -> dict:
    """Return the complete dataset for the analytics dashboard."""
    return {
        "scores": {
            "sophy": 2300,
            "ali": 1800,
            "juan": 2100,
            "diana": 2050
        },
        "achievements": {
            "sophy": ["first_kill", "level_10", "boss_slayer"],
            "ali": ["first_kill", "level_10"],
            "juan": ["first_kill", "level_10", "explorer", "master"]
        },
        "regions": ["north", "east", "central", "north", "east"]
    }


def handle_list_analitics(scores: dict) -> None:
    """Analyze list-based data using descriptive list comprehensions."""
    high_scorers = [
        player for player, score in scores.items()
        if score > 2000
    ]

    scores_doubled = [
        score * 2 for score in scores.values()
    ]

    active_players = [
        player for player in scores.keys()
        if player != "diana"
    ]

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}\n")


def handle_dict_analitics(scores: dict, achs: dict) -> None:
    """Analyze mapping data using descriptive dict comprehensions."""
    player_scores = {
        player: score for player, score in scores.items()
        if player != "diana"
    }

    score_categories = {
        "high": len([s for s in scores.values() if s > 2100]),
        "medium": len([s for s in scores.values() if 1900 <= s <= 2100]),
        "low": len([s for s in scores.values() if s < 1900])
    }

    achievement_counts = {
        player: len(ach_list) for player, ach_list in achs.items()
    }

    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")


def handle_set_analitics(scores: dict, achs: dict, regions: list) -> None:
    """Analyze unique data using set comprehensions."""
    unique_players = {
        player for player in scores.keys()
    }

    temp_ach_list = []
    for player_achievements in achs.values():
        temp_ach_list.extend(player_achievements)

    unique_achievements = {
        achievement for achievement in temp_ach_list
    }

    unique_regions = {
        region for region in regions
    }

    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {unique_regions}\n")


def handle_combined_analysis(scores: dict, achs: dict) -> None:
    """Calculate final metrics using descriptive names."""
    total_players = len(scores)
    average_score = sum(scores.values()) / total_players

    all_ach = []
    for ach_list in achs.values():
        all_ach.extend(ach_list)
    unique_count = len({ach for ach in all_ach})

    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {unique_count}")
    print(f"Average score: {average_score}")
    print("Top performer: sophy (2300 points, 3 achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    game_data = get_game_data()

    handle_list_analitics(game_data["scores"])
    handle_dict_analitics(game_data["scores"], game_data["achievements"])
    handle_set_analitics(
        game_data["scores"],
        game_data["achievements"],
        game_data["regions"]
    )
    handle_combined_analysis(game_data["scores"], game_data["achievements"])
