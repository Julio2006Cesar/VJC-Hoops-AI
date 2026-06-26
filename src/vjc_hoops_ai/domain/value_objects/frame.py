"""Frame value objects used by the analysis pipeline."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Frame:
    """Single video frame with transport metadata.

    The frame payload is intentionally typed as ``Any`` so the domain does not
    depend on OpenCV, NumPy or a specific camera SDK.
    """

    data: Any
    index: int
    timestamp_seconds: float | None = None
    source_id: str | None = None

    def __post_init__(self) -> None:
        if self.index < 0:
            raise ValueError("Frame index must be greater than or equal to 0.")

        if self.timestamp_seconds is not None and self.timestamp_seconds < 0:
            raise ValueError("Frame timestamp must be greater than or equal to 0.")
