# Frame Manager

`Frame Manager` is the first Sprint 1 module for VJC Hoops AI. Its responsibility is to coordinate frame retrieval from a video source without coupling the application core to OpenCV.

## Location

```text
src/vjc_hoops_ai/
├── domain/value_objects/frame.py
├── application/ports/video_frame_source.py
└── application/use_cases/frame_manager.py
```

## Design

- `Frame` represents a single frame plus metadata.
- `VideoFrameSource` is the input port that future adapters must implement.
- `FrameManager` is the application use case that opens a source, reads frames and closes resources.

The frame payload uses a generic `data` field. This allows future adapters to provide NumPy arrays, decoded image buffers, camera SDK objects or test doubles without forcing OpenCV into the domain or application layers.

## Future adapters

Concrete implementations should live under `infrastructure/video/`, for example:

- USB camera source.
- IP camera stream source.
- Video file source.
- Recorded dataset source for tests and benchmarking.

Those adapters may use OpenCV internally, but they must return domain `Frame` objects through the `VideoFrameSource` port.

## Example

```python
from vjc_hoops_ai.application.use_cases import FrameManager

with FrameManager(source) as manager:
    for frame in manager.iter_frames(limit=300):
        process(frame)
```
