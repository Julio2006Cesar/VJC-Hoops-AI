"""Camera-backed implementation of the video frame source port."""

from collections.abc import Callable
from typing import Any, Protocol

from vjc_hoops_ai.domain.value_objects import Frame


class CameraServiceError(RuntimeError):
    """Base error raised by the camera service."""


class CameraUnavailableError(CameraServiceError):
    """Raised when a camera cannot be opened."""


class CaptureDevice(Protocol):
    """Small subset of a camera capture object used by this adapter."""

    def isOpened(self) -> bool:
        """Return whether the capture device is available."""

    def read(self) -> tuple[bool, Any]:
        """Return the next raw camera frame."""

    def release(self) -> None:
        """Release the capture device."""


CaptureFactory = Callable[[int], CaptureDevice]


class CameraService:
    """OpenCV camera adapter that provides domain frames."""

    def __init__(
        self,
        camera_index: int = 0,
        capture_factory: CaptureFactory | None = None,
    ) -> None:
        if camera_index < 0:
            raise ValueError("Camera index must be greater than or equal to 0.")

        self._camera_index = camera_index
        self._capture_factory = capture_factory
        self._capture: CaptureDevice | None = None
        self._frame_index = 0

    @property
    def source_id(self) -> str:
        return f"camera:{self._camera_index}"

    @property
    def camera_index(self) -> int:
        return self._camera_index

    def open(self) -> None:
        if self._capture is not None:
            return

        capture = self._create_capture()
        if not capture.isOpened():
            capture.release()
            raise CameraUnavailableError(
                f"Camera with index {self._camera_index} is not available."
            )

        self._capture = capture
        self._frame_index = 0

    def read(self) -> Frame | None:
        if self._capture is None:
            self.open()

        if self._capture is None:
            raise CameraServiceError("Camera capture was not initialized.")

        success, raw_frame = self._capture.read()
        if not success:
            return None

        frame = Frame(
            data=raw_frame,
            index=self._frame_index,
            source_id=self.source_id,
        )
        self._frame_index += 1
        return frame

    def close(self) -> None:
        if self._capture is None:
            return

        self._capture.release()
        self._capture = None

    def _create_capture(self) -> CaptureDevice:
        if self._capture_factory is not None:
            return self._capture_factory(self._camera_index)

        import cv2

        return cv2.VideoCapture(self._camera_index)
