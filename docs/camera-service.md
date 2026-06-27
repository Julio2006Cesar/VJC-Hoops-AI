# Camera Service

`CameraService` is the Sprint 2 infrastructure adapter for reading frames from a local camera.

## Location

```text
src/vjc_hoops_ai/infrastructure/video/camera_service.py
```

## Responsibility

The service implements the `VideoFrameSource` port expected by `FrameManager`.

It opens a camera by index, reads raw frames through OpenCV and wraps each result in a domain `Frame`.

## Architecture Boundary

OpenCV is used only inside the infrastructure adapter. The domain and application layers continue to depend only on project-owned contracts and value objects.

`cv2` is imported lazily when a real camera capture is created. This keeps unit tests independent from a physical camera and from OpenCV runtime availability.

## Usage

```python
from vjc_hoops_ai.application.use_cases import FrameManager
from vjc_hoops_ai.infrastructure.video import CameraService

camera = CameraService(camera_index=0)

with FrameManager(camera) as frames:
    frame = frames.read_next()
```

## Errors

If the requested camera cannot be opened, the service raises `CameraUnavailableError`.

## Testing Strategy

Unit tests inject a fake capture factory instead of touching a real camera. Hardware-facing smoke tests should be added later as optional integration tests once the application has a CLI or diagnostics command.
