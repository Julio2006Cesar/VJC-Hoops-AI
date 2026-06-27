"""Simple IoU-based object tracker."""

from dataclasses import dataclass
from typing import Protocol


class BoundingBoxDetection(Protocol):
    """Detection shape consumed by the tracker."""

    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidence: float


@dataclass(frozen=True, slots=True)
class TrackedObject:
    """Detection with a stable tracking identity."""

    track_id: int
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidence: float
    missing_frames: int = 0


@dataclass(slots=True)
class _TrackState:
    track_id: int
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidence: float
    missing_frames: int = 0

    def update(self, detection: BoundingBoxDetection) -> None:
        self.x_min = detection.x_min
        self.y_min = detection.y_min
        self.x_max = detection.x_max
        self.y_max = detection.y_max
        self.confidence = detection.confidence
        self.missing_frames = 0

    def mark_missing(self) -> None:
        self.missing_frames += 1

    def to_tracked_object(self) -> TrackedObject:
        return TrackedObject(
            track_id=self.track_id,
            x_min=self.x_min,
            y_min=self.y_min,
            x_max=self.x_max,
            y_max=self.y_max,
            confidence=self.confidence,
            missing_frames=self.missing_frames,
        )


class ObjectTracker:
    """Maintain object identity between frames using bounding box overlap."""

    def __init__(
        self,
        iou_threshold: float = 0.3,
        max_missing_frames: int = 5,
    ) -> None:
        if not 0 <= iou_threshold <= 1:
            raise ValueError("IoU threshold must be between 0 and 1.")

        if max_missing_frames < 0:
            raise ValueError("Max missing frames must be greater than or equal to 0.")

        self._iou_threshold = iou_threshold
        self._max_missing_frames = max_missing_frames
        self._next_track_id = 1
        self._tracks: list[_TrackState] = []

    def update(self, detections: list[BoundingBoxDetection]) -> list[TrackedObject]:
        unmatched_track_indexes = set(range(len(self._tracks)))
        unmatched_detection_indexes = set(range(len(detections)))
        matches = self._match_detections(detections)

        for track_index, detection_index in matches:
            self._tracks[track_index].update(detections[detection_index])
            unmatched_track_indexes.discard(track_index)
            unmatched_detection_indexes.discard(detection_index)

        for track_index in unmatched_track_indexes:
            self._tracks[track_index].mark_missing()

        for detection_index in unmatched_detection_indexes:
            self._tracks.append(self._create_track(detections[detection_index]))

        self._tracks = [
            track
            for track in self._tracks
            if track.missing_frames <= self._max_missing_frames
        ]

        return [
            track.to_tracked_object()
            for track in self._tracks
            if track.missing_frames == 0
        ]

    def reset(self) -> None:
        self._next_track_id = 1
        self._tracks = []

    def _match_detections(
        self,
        detections: list[BoundingBoxDetection],
    ) -> list[tuple[int, int]]:
        candidates: list[tuple[float, int, int]] = []
        for track_index, track in enumerate(self._tracks):
            for detection_index, detection in enumerate(detections):
                score = _calculate_iou(track, detection)
                if score >= self._iou_threshold:
                    candidates.append((score, track_index, detection_index))

        candidates.sort(reverse=True, key=lambda candidate: candidate[0])

        matched_tracks: set[int] = set()
        matched_detections: set[int] = set()
        matches: list[tuple[int, int]] = []

        for _, track_index, detection_index in candidates:
            if track_index in matched_tracks or detection_index in matched_detections:
                continue

            matched_tracks.add(track_index)
            matched_detections.add(detection_index)
            matches.append((track_index, detection_index))

        return matches

    def _create_track(self, detection: BoundingBoxDetection) -> _TrackState:
        track = _TrackState(
            track_id=self._next_track_id,
            x_min=detection.x_min,
            y_min=detection.y_min,
            x_max=detection.x_max,
            y_max=detection.y_max,
            confidence=detection.confidence,
        )
        self._next_track_id += 1
        return track


def _calculate_iou(
    first: BoundingBoxDetection,
    second: BoundingBoxDetection,
) -> float:
    intersection_x_min = max(first.x_min, second.x_min)
    intersection_y_min = max(first.y_min, second.y_min)
    intersection_x_max = min(first.x_max, second.x_max)
    intersection_y_max = min(first.y_max, second.y_max)

    intersection_width = max(0, intersection_x_max - intersection_x_min)
    intersection_height = max(0, intersection_y_max - intersection_y_min)
    intersection_area = intersection_width * intersection_height

    first_area = _calculate_area(first)
    second_area = _calculate_area(second)
    union_area = first_area + second_area - intersection_area

    if union_area <= 0:
        return 0.0

    return intersection_area / union_area


def _calculate_area(box: BoundingBoxDetection) -> int:
    return max(0, box.x_max - box.x_min) * max(0, box.y_max - box.y_min)
