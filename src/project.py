"""Project 2 starter code: Moonlight Museum After Dark.

Students should implement all required behavior in this file.
Use stdlib only.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    """A museum artifact stored in the archive BST."""

    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    """A request to inspect or repair an artifact."""

    artifact_id: int
    description: str


class TreeNode:
    """A node for the artifact BST."""

    def __init__(
        self,
        artifact: Artifact,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    """Binary search tree keyed by artifact_id."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        """Insert an artifact.

        Return True if the artifact was inserted.
        Return False if an artifact with the same ID already exists.
        """
        raise NotImplementedError

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        """Return the matching artifact, or None if it does not exist."""
        raise NotImplementedError

    def inorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using inorder traversal."""
        raise NotImplementedError

    def preorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using preorder traversal."""
        raise NotImplementedError

    def postorder_ids(self) -> list[int]:
        """Return a list of artifact IDs using postorder traversal."""
        raise NotImplementedError


class RestorationQueue:
    """FIFO queue of restoration requests."""

    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        """Add a request to the back of the queue."""
        raise NotImplementedError

    def process_next_request(self) -> RestorationRequest | None:
        """Remove and return the next request, or None if the queue is empty."""
        raise NotImplementedError

    def peek_next_request(self) -> RestorationRequest | None:
        """Return the next request without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the queue has no requests."""
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of queued requests."""
        raise NotImplementedError


class ArchiveUndoStack:
    """LIFO stack of recent archive actions."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        """Push an action onto the stack."""
        raise NotImplementedError

    def undo_last_action(self) -> str | None:
        """Remove and return the most recent action, or None if empty."""
        raise NotImplementedError

    def peek_last_action(self) -> str | None:
        """Return the most recent action without removing it, or None if empty."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the stack has no actions."""
        raise NotImplementedError

    def size(self) -> int:
        """Return the number of stored actions."""
        raise NotImplementedError


class ExhibitNode:
    """A node in the singly linked exhibit route."""

    def __init__(self, stop_name: str, next_node: ExhibitNode | None = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    """Singly linked list of exhibit stops."""

    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        """Add a stop to the end of the route."""
        raise NotImplementedError

    def remove_stop(self, stop_name: str) -> bool:
        """Remove the first matching stop.

        Return True if a stop was removed.
        Return False if the stop does not exist.
        """
        raise NotImplementedError

    def list_stops(self) -> list[str]:
        """Return the route as a list of stop names in order."""
        raise NotImplementedError

    def count_stops(self) -> int:
        """Return the number of stops in the route."""
        raise NotImplementedError


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    """Return a dictionary counting artifacts in each category."""
    raise NotImplementedError



def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    """Return a set of all rooms used by the given artifacts."""
    raise NotImplementedError



def sort_artifacts_by_age(
    artifacts: list[Artifact],
    descending: bool = False,
) -> list[Artifact]:
    """Return a new list of artifacts sorted by age.

    If descending is False, sort from youngest to oldest.
    If descending is True, sort from oldest to youngest.
    """
    raise NotImplementedError



def linear_search_by_name(
    artifacts: list[Artifact],
    name: str,
) -> Artifact | None:
    """Return the first artifact with an exact matching name, or None."""
    raise NotImplementedError



def demo_museum_night() -> None:
    """Run a small integration demo showing the system working together."""
    raise NotImplementedError
