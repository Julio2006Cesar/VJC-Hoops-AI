import unittest
from dataclasses import dataclass

from vjc_hoops_ai.infrastructure.tracking import ObjectTracker


@dataclass(frozen=True)
class Detection:
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidence: float


class ObjectTrackerTest(unittest.TestCase):
    def test_assigns_unique_id_to_new_detection(self) -> None:
        tracker = ObjectTracker()

        tracks = tracker.update([Detection(10, 10, 50, 50, 0.9)])

        self.assertEqual(len(tracks), 1)
        self.assertEqual(tracks[0].track_id, 1)

    def test_keeps_same_id_for_overlapping_detection(self) -> None:
        tracker = ObjectTracker(iou_threshold=0.2)

        first_tracks = tracker.update([Detection(10, 10, 50, 50, 0.9)])
        second_tracks = tracker.update([Detection(12, 12, 52, 52, 0.88)])

        self.assertEqual(first_tracks[0].track_id, second_tracks[0].track_id)

    def test_assigns_different_ids_to_separate_people(self) -> None:
        tracker = ObjectTracker()

        tracks = tracker.update(
            [
                Detection(10, 10, 50, 50, 0.9),
                Detection(100, 100, 150, 150, 0.8),
            ]
        )

        self.assertEqual([track.track_id for track in tracks], [1, 2])

    def test_recovers_same_id_when_detection_returns_before_budget_expires(self) -> None:
        tracker = ObjectTracker(max_missing_frames=2, iou_threshold=0.2)

        initial_tracks = tracker.update([Detection(10, 10, 50, 50, 0.9)])
        tracker.update([])
        recovered_tracks = tracker.update([Detection(11, 11, 51, 51, 0.92)])

        self.assertEqual(initial_tracks[0].track_id, recovered_tracks[0].track_id)

    def test_removes_track_after_missing_frame_budget(self) -> None:
        tracker = ObjectTracker(max_missing_frames=1)

        tracker.update([Detection(10, 10, 50, 50, 0.9)])
        self.assertEqual(tracker.update([]), [])
        self.assertEqual(tracker.update([]), [])
        new_tracks = tracker.update([Detection(10, 10, 50, 50, 0.9)])

        self.assertEqual(new_tracks[0].track_id, 2)

    def test_rejects_invalid_configuration(self) -> None:
        with self.assertRaisesRegex(ValueError, "IoU threshold"):
            ObjectTracker(iou_threshold=1.5)

        with self.assertRaisesRegex(ValueError, "Max missing"):
            ObjectTracker(max_missing_frames=-1)


if __name__ == "__main__":
    unittest.main()
