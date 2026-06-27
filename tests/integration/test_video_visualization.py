import unittest
from collections.abc import Iterator
from typing import Any

import main
from vjc_hoops_ai.domain.value_objects import Frame
from vjc_hoops_ai.infrastructure.tracking import TrackedObject
from vjc_hoops_ai.infrastructure.vision import PersonDetection


class FakeFrameManager:
    def __init__(self, frames: list[Frame]) -> None:
        self._frames = frames
        self._cursor = 0
        self.closed = False

    def __enter__(self) -> "FakeFrameManager":
        return self

    def __exit__(self, *args: object) -> None:
        self.closed = True

    def read_next(self) -> Frame | None:
        if self._cursor >= len(self._frames):
            return None

        frame = self._frames[self._cursor]
        self._cursor += 1
        return frame


class FakeCv2:
    FONT_HERSHEY_SIMPLEX = 0
    LINE_AA = 16

    def __init__(self, keys: list[int]) -> None:
        self._keys = keys
        self._cursor = 0
        self.displayed_frames: list[Any] = []
        self.rectangle_calls: list[tuple[Any, tuple[int, int], tuple[int, int]]] = []
        self.text_calls: list[tuple[Any, str]] = []
        self.destroyed_windows = False

    def putText(
        self,
        frame_data: Any,
        text: str,
        origin: tuple[int, int],
        font_face: int,
        font_scale: float,
        color: tuple[int, int, int],
        thickness: int,
        line_type: int,
    ) -> None:
        self.text_calls.append((frame_data, text))

    def imshow(self, window_name: str, frame_data: Any) -> None:
        self.displayed_frames.append((window_name, frame_data))

    def rectangle(
        self,
        frame_data: Any,
        top_left: tuple[int, int],
        bottom_right: tuple[int, int],
        color: tuple[int, int, int],
        thickness: int,
    ) -> None:
        self.rectangle_calls.append((frame_data, top_left, bottom_right))

    def waitKey(self, delay: int) -> int:
        if self._cursor >= len(self._keys):
            return main.QUIT_KEY

        key = self._keys[self._cursor]
        self._cursor += 1
        return key

    def destroyAllWindows(self) -> None:
        self.destroyed_windows = True


def fixed_times(values: list[float]) -> Iterator[float]:
    for value in values:
        yield value

    while True:
        yield values[-1]


class FakePersonDetector:
    def __init__(self, detections: list[PersonDetection]) -> None:
        self._detections = detections
        self.detected_frames: list[Any] = []

    def detect(self, frame_data: Any) -> list[PersonDetection]:
        self.detected_frames.append(frame_data)
        return self._detections


class FakeObjectTracker:
    def __init__(self, tracks: list[TrackedObject]) -> None:
        self._tracks = tracks
        self.received_detections: list[list[PersonDetection]] = []

    def update(self, detections: list[PersonDetection]) -> list[TrackedObject]:
        self.received_detections.append(detections)
        return self._tracks


class VideoVisualizationTest(unittest.TestCase):
    def test_run_camera_preview_displays_frames_and_stops_on_q(self) -> None:
        fake_manager = FakeFrameManager(
            [
                Frame(data="frame-0", index=0),
                Frame(data="frame-1", index=1),
            ]
        )
        fake_cv2 = FakeCv2(keys=[-1, main.QUIT_KEY])
        fake_detector = FakePersonDetector(
            [PersonDetection(10, 20, 30, 40, confidence=0.95)]
        )
        fake_tracker = FakeObjectTracker(
            [TrackedObject(1, 10, 20, 30, 40, confidence=0.95)]
        )
        times = fixed_times([10.0, 10.5, 11.0])

        main.run_camera_preview(
            camera_index=0,
            frame_manager_factory=lambda _: fake_manager,
            person_detector_factory=lambda: fake_detector,
            object_tracker_factory=lambda: fake_tracker,
            cv2_module=fake_cv2,
            time_provider=lambda: next(times),
        )

        self.assertEqual(
            fake_cv2.displayed_frames,
            [
                (main.WINDOW_NAME, "frame-0"),
                (main.WINDOW_NAME, "frame-1"),
            ],
        )
        self.assertEqual(fake_detector.detected_frames, ["frame-0", "frame-1"])
        self.assertEqual(
            fake_tracker.received_detections,
            [
                [PersonDetection(10, 20, 30, 40, confidence=0.95)],
                [PersonDetection(10, 20, 30, 40, confidence=0.95)],
            ],
        )
        self.assertEqual(fake_cv2.rectangle_calls[0], ("frame-0", (10, 20), (30, 40)))
        self.assertEqual(fake_cv2.text_calls[0], ("frame-0", "ID 1"))
        self.assertEqual(fake_cv2.text_calls[1], ("frame-0", "person 0.95"))
        self.assertEqual(fake_cv2.text_calls[2], ("frame-0", "FPS: 2.0"))
        self.assertTrue(fake_manager.closed)
        self.assertTrue(fake_cv2.destroyed_windows)


if __name__ == "__main__":
    unittest.main()
