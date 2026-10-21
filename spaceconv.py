"""spaceconv - a unit converter for space-weather and solar wind quantities."""

import argparse
import sys

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
    "speed": { # base unit: km/s
        "km/s": 1.0,
        "m/s": 0.001,
        "km/h": 1 / 3600,
        "au/day": 149_597_870.7 / 86_400,
    },
    "magnetic_field": { # base unit: nT (nanotesla)
        "nT": 1.0,
        "T": 1e9,
        "gauss": 1e5,
    },
    "density": { # base unit: particles per cubic centimeter
        "per_cm3": 1.0,
        "per_m3": 1e-6,
    },
    "temperature": { # base unit: kelvin (plasma temperature)
        "K": 1.0,
        "MK": 1e6,
        "eV": 11_604.518,
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


def main():
    parser = argparse.ArgumentParser(
        description="Convert space weather and solar wind units."
    )
    parser.add_argument("value", type=float, help="number to convert")
    parser.add_argument("from_unit", help="unit to convert from")
    parser.add_argument("to_unit", help="unit to convert to")
    args = parser.parse_args()

    try:
        result = convert(args.value, args.from_unit, args.to_unit)
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    print(f"{args.value:g} {args.from_unit} = {result:.6g} {args.to_unit}")


if __name__ == "__main__":
    main()

