"""spaceconv - a unit converter for space-weather and solar wind quantities."""

# Each category maps a unit name to how many base units one of that unit equals.
# Converting is then just value * factor[from_unit] / factor[to_unit]
CONVERSIONS = {
    "distance": { # base unit: km
        "km": 1.0,
        "m": 0.001,
        "au": 149_597_870.7,
        "earth radius": 6_371.0,
        "light_minute": 17_987_547.48
    },
}


def find_category(unit):
    """Return the category a unit belongs to, or None if it's unknown."""
    for category, units in CONVERSIONS.items():
        if unit in units:
            return category
    return None


def convert(value, from_unit, to_unit):
    """Convert value from one unit to another within the same category."""
    from_category = find_category(from_unit)
    to_category = find_category(to_unit)

    if from_category is None:
        raise ValueError(f"Unknown unit: {from_unit}")
    if to_category is None:
        raise ValueError(f"Unknown unit: {to_unit}")
    if from_category != to_category:
        raise ValueError(f"Can't convert {from_category} to {to_category}")

    units = CONVERSIONS[from_category]
    return value * units[from_unit] / units[to_unit]