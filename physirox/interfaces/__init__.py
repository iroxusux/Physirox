"""Pure interface definitions for Pyrox framework.

This module provides abstract interfaces that eliminate circular dependencies
between services and models while maintaining clean architectural boundaries.

The interfaces follow the Interface Segregation Principle (ISP) and Dependency
Inversion Principle (DIP) to create a loosely-coupled, extensible system.

Key Design Principles:
    - Interfaces contain only method signatures, no implementations
    - No imports from pyrox.services or pyrox.models modules
    - Pure abstractions with minimal external dependencies
    - Forward-compatible design for future enhancements
    - Properties used and implimented for attribute access where appropriate

Interface Categories:
    - GUI: Backend, window, menu, and component abstractions
    - Services: Environment, logging, configuration, and utility interfaces
    - Application: Task, factory, and application lifecycle interfaces
    - Configuration: Settings, environment, and state management interfaces
    - Events: Observer patterns, subscriptions, and notification interfaces
"""

# Protocols
from .protocols import (
    # Coordinate imports for protocols that support points in a space.
    ICoord2D,
    IArea2D,

    # Spatial imports for protocols that support spatial objects.
    ISpatial2D,
    IRotatable,
    IDirectional2D,
    IZoomable,

    # Kinematic imports for protocols that support kinematic objects.
    IVelocity2D,
    IAngularVelocity,
    IKinematic2D,

    # Physics imports for protocols that support physical objects.
    BodyType,
    ColliderType,
    CollisionLayer,
    IMaterial,
    ICollider2D,
    IPhysicsBody2D,
    IRigidBody2D,
    IPhysicsEngine,
)

# Physics interfaces
from .physics import IBasePhysicsBody

# Scene interfaces
from .scene import (
    IScene,
    ISceneObject,
    ISceneObjectFactory,
    ISceneRunnerService,
    BindingDirection,
    ISceneBinding,
    ISceneBridge,
    ISceneBoundLayer,
    ICompositeSceneObject,
    ISceneGroup,
)

from .gui.viewport import IViewport

from pyrox.interfaces import CardinalDirection, Connection, IHasCanvas


__all__ = (
    # Coordinate protocols
    'ICoord2D',
    'IArea2D',
    # Spatial protocols
    'ISpatial2D',
    'IRotatable',
    'IDirectional2D',
    'IZoomable',
    # Kinematic protocols
    'IVelocity2D',
    'IAngularVelocity',
    'IKinematic2D',
    # Physics protocols
    'BodyType',
    'ColliderType',
    'CollisionLayer',
    'IMaterial',
    'ICollider2D',
    'IPhysicsBody2D',
    'IRigidBody2D',
    'IPhysicsEngine',

    # Physics Interfaces
    'IBasePhysicsBody',

    # Scene Interfaces
    'IScene',
    'ISceneObject',
    'ISceneObjectFactory',
    'ISceneRunnerService',
    'BindingDirection',
    'ISceneBinding',
    'ISceneBridge',
    'ISceneBoundLayer',
    'ICompositeSceneObject',
    'ISceneGroup',

    # GUI Interfaces
    'IViewport',

    # pyrox re-imports
    'CardinalDirection',
    'Connection',
    'IHasCanvas',

)
