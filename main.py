"""Camera preview entry point for VJC Hoops AI."""

from collections.abc import Callable
from time import perf_counter
from typing import Any

from vjc_hoops_ai.application.use_cases import FrameManager
from vjc_hoops_ai.infrastructure.tracking import ObjectTracker, TrackedObject
from vjc_hoops_ai.infrastructure.video import CameraService
from vjc_hoops_ai.infrastructure.vision import PersonDetector


WINDOW_NAME = "VJC Hoops AI - Camera Preview"
QUIT_KEY = ord("q")


def create_frame_manager(camera_index: int = 0) -> FrameManager:
    camera = CameraService(camera_index=camera_index)
    return FrameManager(camera)


def create_person_detector() -> PersonDetector:
    return PersonDetector()


def create_object_tracker() -> ObjectTracker:
    return ObjectTracker()


def calculate_fps(previous_time: float, current_time: float) -> float:
    elapsed = current_time - previous_time
    if elapsed <= 0:
        return 0.0

    return 1.0 / elapsed


def draw_fps(frame_data: Any, fps: float, cv2_module: Any) -> Any:
    cv2_module.putText(
        frame_data,
        f"FPS: {fps:.1f}",
        (20, 40),
        cv2_module.FONT_HERSHEY_SIMPLEX,
        1.0,
        (0, 255, 0),
        2,
        cv2_module.LINE_AA,
    )
    return frame_data


def draw_tracked_objects(
    frame_data: Any,
    tracked_objects: list[TrackedObject],
    cv2_module: Any,
) -> Any:
    for tracked_object in tracked_objects:
        top_left = (tracked_object.x_min, tracked_object.y_min)
        bottom_right = (tracked_object.x_max, tracked_object.y_max)
        id_origin = (tracked_object.x_min, max(tracked_object.y_min - 35, 20))
        confidence_origin = (
            tracked_object.x_min,
            max(tracked_object.y_min - 10, 20),
        )

        cv2_module.rectangle(frame_data, top_left, bottom_right, (0, 255, 255), 2)
        cv2_module.putText(
            frame_data,
            f"ID {tracked_object.track_id}",
            id_origin,
            cv2_module.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2,
            cv2_module.LINE_AA,
        )
        cv2_module.putText(
            frame_data,
            f"person {tracked_object.confidence:.2f}",
            confidence_origin,
            cv2_module.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2,
            cv2_module.LINE_AA,
        )

    return frame_data


def run_camera_preview(
    camera_index: int = 0,
    frame_manager_factory: Callable[[int], FrameManager] = create_frame_manager,
    person_detector_factory: Callable[[], Any] = create_person_detector,
    object_tracker_factory: Callable[[], Any] = create_object_tracker,
    cv2_module: Any | None = None,
    time_provider: Callable[[], float] = perf_counter,
) -> None:
    if cv2_module is None:
        import cv2 as cv2_module

    previous_time = time_provider()
    person_detector = person_detector_factory()
    object_tracker = object_tracker_factory()

    with frame_manager_factory(camera_index) as frame_manager:
        while True:
            frame = frame_manager.read_next()
            if frame is None:
                break

            current_time = time_provider()
            fps = calculate_fps(previous_time, current_time)
            previous_time = current_time

            detections = person_detector.detect(frame.data)
            tracked_objects = object_tracker.update(detections)
            display_frame = draw_tracked_objects(
                frame.data,
                tracked_objects,
                cv2_module,
            )
            display_frame = draw_fps(display_frame, fps, cv2_module)
            cv2_module.imshow(WINDOW_NAME, display_frame)

            key = cv2_module.waitKey(1) & 0xFF
            if key == QUIT_KEY:
                break

    cv2_module.destroyAllWindows()


if __name__ == "__main__":
    run_camera_preview()
