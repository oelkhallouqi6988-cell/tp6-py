
import unittest
from film import Film


class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film = Film(
            "Inception",
            "Christopher Nolan",
            2010,
            8.8
        )

    def test_creation(self):
        self.assertEqual(self.film.titre, "Inception")
        self.assertEqual(self.film.note, 8.8)

    def test_note_minimale(self):
        film = Film("Film A", "Auteur A", 2020, 0)
        self.assertEqual(film.note, 0)

    def test_note_maximale(self):
        film = Film("Film B", "Auteur B", 2020, 10)
        self.assertEqual(film.note, 10)

    def test_note_negative(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", 2020, -1)

    def test_note_superieure(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", 2020, 11)

    def test_note_type_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Auteur", 2020, "8")

    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Auteur", 2020, 8)

    def test_realisateur_vide(self):
        with self.assertRaises(ValueError):
            Film("Film", "", 2020, 8)

    def test_annee_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Auteur", "2020", 8)

    def test_immutabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 9.5

    def test_est_classique(self):
        film = Film("Titanic", "James Cameron", 1997, 7.8)
        self.assertTrue(film.est_classique())

    def test_non_classique(self):
        self.assertFalse(self.film.est_classique())

    def test_to_json(self):
        resultat = self.film.to_json()
        self.assertIn('"titre": "Inception"', resultat)

    def test_from_json(self):
        chaine = self.film.to_json()
        film2 = Film.from_json(chaine)

        self.assertEqual(film2, self.film)

    def test_tri_par_note(self):
        film1 = Film("Film A", "Auteur A", 2020, 6.5)
        film2 = Film("Film B", "Auteur B", 2020, 9.0)
        film3 = Film("Film C", "Auteur C", 2020, 7.5)

        films = sorted([film1, film2, film3])

        self.assertEqual(
            [f.note for f in films],
            [6.5, 7.5, 9.0]
        )


if __name__ == "__main__":
    unittest.main()
