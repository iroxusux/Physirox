# Coordinate imports for protocols that support points in a space.
from .coord import (
    Coord2D,
    Area2D,
)

# Spatial imports for protocols that support spatial objects.
from .spatial import (
    Spatial2D,
    Rotatable,
    Zoomable,
)

# Physics imports for physics simulation
from .physics import (
    Material,
    Collider2D,
    RigidBody2D,
    PhysicsBody2D,
)
__all__ = [
    # Coordinate protocols
    "Coord2D",
    "Area2D",

    # Spatial protocols
    "Spatial2D",
    "Rotatable",
    "Zoomable",

    # Physics implementations
    "Material",
    "Collider2D",
    "RigidBody2D",
    "PhysicsBody2D",
]
