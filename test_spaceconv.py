import unittest

from spaceconv import convert


class TestConvert(unittest.TestCase):
    def test_au_to_km(self):
        self.assertAlmostEqual(convert(1, "au", "km"), 149_597_870.7)

    def test_solar_wind_speed(self):
        # A typical 450 km/s solar wind covers about 0.26 AU per day
        self.assertAlmostEqual(convert(450, "km/s", "au/day"), 0.2599, places=4)

    def test_gauss_to_nT(self):
        self.assertAlmostEqual(convert(1, "gauss", "nT"), 100_000)

    def test_unknown_unit(self):
        with self.assertRaises(ValueError):
            convert(1, "furlong", "km")

    def test_mismatched_categories(self):
        with self.assertRaises(ValueError):
            convert(1, "km", "nT")


if __name__ == "__main__":
    unittest.main()