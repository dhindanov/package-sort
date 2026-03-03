"""
### Objective

Imagine you work in Smarter Technology’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.
"""

from enum import Enum


class PackageCategory(str, Enum):
    """
    Enum representing the physical destination stacks in the factory.
    Inheriting from 'str' makes it JSON serializable for APIs.
    """
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


def sort(width: float, height: float, length: float, mass: float) -> str:
    # 1. Input validation
    if any(v <= 0 for v in (width, height, length)):
        raise ValueError("Package dimensions must be positive.")
    if mass < 0:
        raise ValueError("Package weight cannot be negative.")

    # 1. Classification Logic
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20

    # 2. Dispatch Logic using Enum members
    if is_bulky and is_heavy:
        return PackageCategory.REJECTED
    if is_bulky or is_heavy:
        return PackageCategory.SPECIAL
    return PackageCategory.STANDARD
