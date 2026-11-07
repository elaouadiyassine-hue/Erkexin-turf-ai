from dataclasses import dataclass
from typing import List


@dataclass
class Horse:
    number: int
    name: str
    odds: float
    form_score: float
    rating: float


def calculate_score(horse: Horse) -> float:
    score = (
        horse.form_score * 0.40
        + horse.rating * 0.40
        + (100 / horse.odds) * 0.20
    )
    return round(score, 2)


def analyze_races(horses: List[Horse]):
    ranked = sorted(
        horses,
        key=calculate_score,
        reverse=True
    )

    main_selection = ranked[:5]
    reserves = ranked[5:8]

    return main_selection, reserves


if __name__ == "__main__":
    print("ERKEXIN TURF AI")
    print("محرك تحليل سباقات الخيل جاهز")
