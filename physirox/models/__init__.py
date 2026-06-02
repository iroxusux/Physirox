"""models for pyrox"""

# ABCs, protocols and base classes
from .protocols import (
    # Coordinate components
    Coord2D,
    Area2D,
    # Spacial components
    Spatial2D,
    Rotatable,
    Zoomable,
    # Physics components
    Material,
    Collider2D,
    RigidBody2D,
    PhysicsBody2D
)

# Concrete physics body implementations
from .physics import (
    BasePhysicsBody,
    ConveyorBody,
    CrateBody,
    PhysicsSceneFactory,
    PhysicsSceneTemplate,
)

# GUI components
from .gui import (
    SceneViewerFrame,
)

# Scene components
from .scene import (
    Scene,
    SceneBinding,
    SceneBridge,
    SceneObject,
)


__all__ = [
    # Coordinate protocols
    'Coord2D',
    'Area2D',
    # Spatial protocols
    'Spatial2D',
    'Rotatable',
    'Zoomable',

    # GUI components
    'SceneViewerFrame',

    # Scene components
    'Scene',
    'SceneBinding',
    'SceneBridge',
    'SceneObject',

    # Physics components
    'Material',
    'Collider2D',
    'RigidBody2D',
    'PhysicsBody2D',

    # Concrete physics bodies
    'BasePhysicsBody',
    'ConveyorBody',
    'CrateBody',
    'PhysicsSceneFactory',
    'PhysicsSceneTemplate',
]
