"""Frame Manager use case."""

from collections.abc import Iterator

from vjc_hoops_ai.application.ports import VideoFrameSource
from vjc_hoops_ai.domain.value_objects import Frame


class FrameManager:
    """Coordinates frame retrieval from a video source."""

    def __init__(self, source: VideoFrameSource) -> None:
        self._source = source
        self._is_open = False

    @property
    def source_id(self) -> str:
        return self._source.source_id

    def open(self) -> None:
        if self._is_open:
            return

        self._source.open()
        self._is_open = True

    def read_next(self) -> Frame | None:
        self.open()
        return self._source.read()

    def iter_frames(self, limit: int | None = None) -> Iterator[Frame]:
        if limit is not None and limit < 0:
            raise ValueError("Frame iteration limit must be greater than or equal to 0.")

        self.open()

        frames_read = 0
        while limit is None or frames_read < limit:
            frame = self._source.read()
            if frame is None:
                break

            frames_read += 1
            yield frame

    def close(self) -> None:
        if not self._is_open:
            return

        self._source.close()
        self._is_open = False

    def __enter__(self) -> "FrameManager":
        self.open()
        return self

    def __exit__(self, *args: object) -> None:
        self.close()
