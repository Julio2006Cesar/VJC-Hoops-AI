"""Ports for video frame sources."""

from typing import Protocol

from vjc_hoops_ai.domain.value_objects import Frame


class VideoFrameSource(Protocol):
    """Contract implemented by cameras, streams and video files."""

    @property
    def source_id(self) -> str:
        """Stable identifier for the frame source."""

    def open(self) -> None:
        """Prepare the source before reading frames."""

    def read(self) -> Frame | None:
        """Return the next frame, or ``None`` when the stream is exhausted."""

    def close(self) -> None:
        """Release resources held by the source."""
