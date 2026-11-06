
from dataclasses import dataclass, asdict, replace
import json

@dataclass(frozen=True, slots=True, order=True)
class Livre:
    titre: str
    auteur: str
    annee: int
    prix: float

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)

    def promo(self, prix_reduit):
        """Retourne un nouveau livre avec un prix réduit."""
        if prix_reduit < 0:
            raise ValueError("Le prix doit être positif.")
        return replace(self, prix=prix_reduit)


def charger_livre(json_string):
    """Reconstitue un objet Livre depuis une chaîne JSON."""
    donnees = json.loads(json_string)
    return Livre(**donnees)


# Création d'un livre
livre = Livre("1984", "George Orwell", 1949, 9.90)

# Sérialisation JSON
print(livre.to_json())

# Promotion
livre_promo = livre.promo(7.50)
print(livre_promo)

# Vérification de l'immuabilité
print(livre.prix)  # 9.9
print(livre_promo.prix)  # 7.5

# Chargement depuis JSON
livre_restaure = charger_livre(livre.to_json())
print(livre_restaure)

# Comparaison des livres
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 12.0)

livres = sorted([livre, livre2])
print(livres)
