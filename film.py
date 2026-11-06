
from dataclasses import dataclass, asdict
import json


@dataclass(frozen=True, slots=True)
class Film:
    titre: str
    realisateur: str
    annee: int
    note: float

    def __post_init__(self):
        if not isinstance(self.titre, str) or not self.titre.strip():
            raise ValueError("Le titre doit être une chaîne non vide.")

        if not isinstance(self.realisateur, str) or not self.realisateur.strip():
            raise ValueError("Le réalisateur doit être une chaîne non vide.")

        if type(self.annee) is not int or self.annee <= 0:
            raise ValueError("L'année doit être un entier positif.")

        if isinstance(self.note, bool) or not isinstance(self.note, (int, float)):
            raise TypeError("La note doit être numérique.")

        if not 0 <= self.note <= 10:
            raise ValueError("La note doit être entre 0 et 10.")

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def est_classique(self):
        return self.annee < 2000

    @classmethod
    def from_json(cls, chaine_json):
        donnees = json.loads(chaine_json)
        return cls(**donnees)

    def __lt__(self, autre):
        if not isinstance(autre, Film):
            return NotImplemented
        return self.note < autre.note
