"""
Scene management for field scene_object simulations.
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import (
    Callable,
    TypeVar,
)
from pyrox.interfaces import IConnectionRegistry
from physirox.interfaces import (
    IBasePhysicsBody,
    IPhysicsBody2D,
)
from physirox.interfaces.scene.sceneobject import ISceneObject
from physirox.interfaces.scene.compositesceneobject import ICompositeSceneObject
from physirox.interfaces.scene.scenegroup import ISceneGroup


T = TypeVar("T", bound=ISceneObject | ICompositeSceneObject | ISceneGroup)


class IScene(ABC):
    """Scene Interface for managing scene objects within a scene."""

    @abstractmethod
    def get_scene_object(self, scene_object_id: str) -> ISceneObject | ICompositeSceneObject | ISceneGroup | None: ...
    @abstractmethod
    def get_scene_objects(self) -> dict[str, ISceneObject | ICompositeSceneObject | ISceneGroup]: ...
    @abstractmethod
    def set_scene_objects(self, scene_objects: dict[str, T]) -> None: ...
    @abstractmethod
    def add_scene_object(self, scene_object: ISceneObject | ICompositeSceneObject | ISceneGroup) -> None: ...
    @abstractmethod
    def get_on_scene_object_added(self) -> list[Callable]: ...
    @abstractmethod
    def remove_scene_object(self, scene_object_id: str) -> None: ...
    @abstractmethod
    def get_on_scene_object_removed(self) -> list[Callable]: ...
    @abstractmethod
    def get_connection_registry(self) -> "IConnectionRegistry": ...
    @abstractmethod
    def set_connection_registry(self, registry: "IConnectionRegistry") -> None: ...
    @abstractmethod
    def get_on_scene_updated(self) -> list[Callable]: ...
    @abstractmethod
    def update(self, delta_time: float) -> None: ...
    @abstractmethod
    def to_dict(self) -> dict: ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "IScene": ...
    @abstractmethod
    def save(self, filepath: str | Path) -> None: ...

    @classmethod
    @abstractmethod
    def load(cls, filepath: str | Path) -> "IScene": ...

    # ------------------------------------------------------------------
    # Group convenience helpers
    # ------------------------------------------------------------------

    @abstractmethod
    def group_objects(self, object_ids: list[str], name: str = "Group", layer: int = 0) -> "ISceneGroup": ...
    @abstractmethod
    def ungroup(self, group_id: str) -> list[ISceneObject]: ...

    # ------------------------------------------------------------------
    # Property accessors
    # ------------------------------------------------------------------
    scene_objects = property(get_scene_objects, set_scene_objects)
    on_scene_object_added = property(get_on_scene_object_added)
    on_scene_object_removed = property(get_on_scene_object_removed)
    on_scene_updated = property(get_on_scene_updated)

    @property
    @abstractmethod
    def connection_registry(self) -> "IConnectionRegistry": ...

    @connection_registry.setter
    @abstractmethod
    def connection_registry(self, registry: "IConnectionRegistry") -> None: ...


class ISceneRunnerService(ABC):
    """ Service interface for running and managing scenes.
    """

    @classmethod
    @abstractmethod
    def get_scene(cls) -> IScene | None: ...

    @classmethod
    @abstractmethod
    def set_scene(cls, scene: IScene | None) -> None: ...

    @classmethod
    @abstractmethod
    def get_scene_filepath(cls) -> Path | None: ...

    @classmethod
    @abstractmethod
    def load_scene(cls, filepath: str | Path | None = None) -> None: ...

    @classmethod
    @abstractmethod
    def save_scene(cls, filepath: str | Path | None = None) -> None: ...

    @classmethod
    @abstractmethod
    def get_physics_engine(cls) -> object | None: ...

    @classmethod
    @abstractmethod
    def set_physics_engine(cls, physics_engine) -> None: ...

    @classmethod
    @abstractmethod
    def get_environment(cls) -> object | None: ...

    @classmethod
    @abstractmethod
    def set_environment(cls, environment: object) -> None: ...

    @classmethod
    @abstractmethod
    def set_update_rate(cls, fps: float) -> None: ...

    @classmethod
    @abstractmethod
    def get_update_rate(cls) -> float: ...

    @classmethod
    @abstractmethod
    def add_physics_body(cls, body: IBasePhysicsBody | IPhysicsBody2D) -> None: ...

    @classmethod
    @abstractmethod
    def remove_physics_body(cls, body: IBasePhysicsBody) -> None: ...

    @classmethod
    @abstractmethod
    def get_physics_stats(cls) -> dict: ...


__all__ = ["IScene"]
