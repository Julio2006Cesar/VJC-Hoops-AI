# Object Tracker

Sprint 5 adds a small tracking engine for maintaining object identity across frames.

The runtime flow is:

```text
CameraService -> FrameManager -> PersonDetector -> ObjectTracker -> OpenCV preview
```

No ball detection, rim detection or shot analysis is implemented in this sprint.

## Location

```text
src/vjc_hoops_ai/infrastructure/tracking/object_tracker.py
```

## Design

`ObjectTracker` is independent from YOLO and from `PersonDetector`. It accepts any detection object with:

- `x_min`
- `y_min`
- `x_max`
- `y_max`
- `confidence`

This means detections from `PersonDetector` work today, and future ball or rim detectors can be connected later without changing the tracker contract.

## Tracking Strategy

The current implementation uses IoU matching:

- Existing tracks are matched to new detections by bounding box overlap.
- Each new unmatched detection receives a unique ID.
- Tracks can survive a configurable number of missing frames.
- If a track is missing longer than `max_missing_frames`, it is removed.

This is intentionally simple and dependency-free. It can later be replaced by a stronger tracker such as ByteTrack, SORT or DeepSORT behind the same module boundary.

## Visualization

`main.py` draws:

- Bounding box.
- Track ID above the box.
- Person confidence.
- FPS counter.

## Tests

Unit tests validate:

- Unique ID assignment.
- ID persistence across overlapping detections.
- Multiple people.
- Missing-frame recovery.
- Track removal after the missing-frame budget expires.
