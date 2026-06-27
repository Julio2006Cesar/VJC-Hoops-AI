# Video Visualization

Sprint 3 adds a minimal camera preview application. Sprint 4 extends it with person detection, and Sprint 5 adds object tracking:

```text
CameraService -> FrameManager -> PersonDetector -> ObjectTracker -> OpenCV window
```

No ball tracking, rim detection, court detection or tracking logic is included yet.

## Entry Point

```text
main.py
```

The entry point initializes `CameraService(camera_index=0)`, wraps it with `FrameManager`, loads `PersonDetector` once, initializes `ObjectTracker`, displays camera frames in an OpenCV window, draws person bounding boxes with track IDs and overlays real-time FPS.

Press `q` to close the preview.

## Run

From the project root:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python main.py
```

If camera index `0` is not available, `CameraService` raises `CameraUnavailableError`.

## Architecture Boundary

OpenCV remains limited to:

- `src/vjc_hoops_ai/infrastructure/video/camera_service.py`
- `main.py`

YOLO remains limited to:

- `src/vjc_hoops_ai/infrastructure/vision/person_detector.py`

The domain and application layers do not import OpenCV or YOLO.

## Testing

The integration test injects fake frame and display adapters, so it can verify the preview loop without requiring a physical webcam or GUI window.
