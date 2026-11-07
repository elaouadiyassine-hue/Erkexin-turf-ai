
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Horse:
    number: int
    name: str
    odds: float
    form_score: float
    rating: float


def calculate_score(horse: Horse) -> float:
    if horse.odds <= 0:
        raise ValueError(
            f"Odds غير صالحة للحصان {horse.name}"
        )

    if not 0 <= horse.form_score <= 100:
        raise ValueError("Form score يجب أن يكون بين 0 و100")

    if not 0 <= horse.rating <= 100:
        raise ValueError("Rating يجب أن يكون بين 0 و100")

    score = (
        horse.form_score * 0.40
        + horse.rating * 0.40
        + (100 / horse.odds) * 0.20
    )

    return round(score, 2)


def analyze_races(
    horses: List[Horse]
) -> Tuple[List[Horse], List[Horse]]:

    valid_horses = []

    for horse in horses:
        try:
            calculate_score(horse)
            valid_horses.append(horse)
        except (ValueError, TypeError):
            continue

    ranked = sorted(
        valid_horses,
        key=calculate_score,
        reverse=True
    )

    main_selection = ranked[:5]
    reserves = ranked[5:8]

    return main_selection, reserves


if __name__ == "__main__":
    print("ERKEXIN TURF AI")
    print("محرك تحليل سباقات الخيل جاهز")
    
