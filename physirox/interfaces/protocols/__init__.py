"""Protocol interfaces for various capabilities within the Pyrox environment.
"""

# Coordinate imports for protocols that support points in a space.
from .coord import (
    ICoord2D,
    IArea2D,
)

# Spatial imports for protocols that support spatial objects.
from .spatial import (
    ISpatial2D,
    IRotatable,
    IDirectional2D,
    IZoomable,
)

# Kinematic imports for protocols that support kinematic objects.
from .kinematic import (
    IVelocity2D,
    IAngularVelocity,
    IKinematic2D,
)

# Physics imports for protocols that support physical objects.
from .physics import (
    BodyType,
    ColliderType,
    CollisionLayer,
    IMaterial,
    ICollider2D,
    IPhysicsBody2D,
    IRigidBody2D,
    IPhysicsEngine,
)

__all__ = [
    # Coordinate protocols
    "ICoord2D",
    "IArea2D",

    # Spatial protocols
    "ISpatial2D",
    "IRotatable",
    "IDirectional2D",
    "IZoomable",

    # Kinematic protocols
    "IVelocity2D",
    "IAngularVelocity",
    "IKinematic2D",

    # Physics protocols
    "BodyType",
    "ColliderType",
    "CollisionLayer",
    "IMaterial",
    "ICollider2D",
    "IRigidBody2D",
    "IPhysicsBody2D",
    "IPhysicsEngine",
]
