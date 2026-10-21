# spaceconv

A small command-line unit converter for space-weather and solar wind quantities —
the kinds of units that show up when working with spacecraft data such as solar
wind speed, interplanetary magnetic field strength, plasma density, and plasma
temperature.

## Supported units

| Category       | Units                                          |
|----------------|------------------------------------------------|
| distance       | `km`, `m`, `au`, `earth_radius`, `light_minute` |
| speed          | `km/s`, `m/s`, `km/h`, `au/day`                |
| magnetic_field | `nT`, `T`, `gauss`                             |
| density        | `per_cm3`, `per_m3`                            |
| temperature    | `K`, `MK`, `eV`                                |

## Usage

Requires Python 3.8 or newer. No extra packages needed.

```
python spaceconv.py 450 km/s au/day
450 km/s = 0.259897 au/day

python spaceconv.py 1 eV K
1 eV = 11604.5 K

python spaceconv.py --list
```

Converting between different categories (for example `km` to `nT`) prints an error.

## Running the tests

```
python -m unittest
```

## About

Built as a hands-on project for learning Git and GitHub: incremental commits,
feature branches, pull requests, resolving a merge conflict, issues, and tags.
