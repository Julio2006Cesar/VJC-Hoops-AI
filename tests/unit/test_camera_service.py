import unittest
from typing import Any

from vjc_hoops_ai.domain.value_objects import Frame
from vjc_hoops_ai.infrastructure.video import CameraService, CameraUnavailableError


class FakeCapture:
    def __init__(self, opened: bool = True, frames: list[Any] | None = None) -> None:
        self._opened = opened
        self._frames = frames or []
        self._cursor = 0
        self.release_count = 0

    def isOpened(self) -> bool:
        return self._opened

    def read(self) -> tuple[bool, Any]:
        if self._cursor >= len(self._frames):
            return False, None

        frame = self._frames[self._cursor]
        self._cursor += 1
        return True, frame

    def release(self) -> None:
        self.release_count += 1


class CameraServiceTest(unittest.TestCase):
    def test_opens_camera_with_default_index(self) -> None:
        requested_indexes: list[int] = []

        def factory(index: int) -> FakeCapture:
            requested_indexes.append(index)
            return FakeCapture(frames=["raw-frame"])

        service = CameraService(capture_factory=factory)

        frame = service.read()

        self.assertEqual(requested_indexes, [0])
        self.assertEqual(frame, Frame(data="raw-frame", index=0, source_id="camera:0"))

    def test_opens_camera_with_custom_index(self) -> None:
        requested_indexes: list[int] = []

        def factory(index: int) -> FakeCapture:
            requested_indexes.append(index)
            return FakeCapture(frames=["raw-frame"])

        service = CameraService(camera_index=2, capture_factory=factory)

        frame = service.read()

        self.assertEqual(requested_indexes, [2])
        self.assertEqual(frame.source_id, "camera:2")

    def test_returns_none_when_camera_has_no_more_frames(self) -> None:
        service = CameraService(capture_factory=lambda _: FakeCapture(frames=[]))

        self.assertIsNone(service.read())

    def test_raises_when_camera_is_unavailable(self) -> None:
        capture = FakeCapture(opened=False)
        service = CameraService(capture_factory=lambda _: capture)

        with self.assertRaisesRegex(CameraUnavailableError, "not available"):
            service.open()

        self.assertEqual(capture.release_count, 1)

    def test_close_releases_capture(self) -> None:
        capture = FakeCapture(frames=["raw-frame"])
        service = CameraService(capture_factory=lambda _: capture)

        service.open()
        service.close()

        self.assertEqual(capture.release_count, 1)

    def test_rejects_negative_camera_index(self) -> None:
        with self.assertRaisesRegex(ValueError, "Camera index"):
            CameraService(camera_index=-1)


if __name__ == "__main__":
    unittest.main()
