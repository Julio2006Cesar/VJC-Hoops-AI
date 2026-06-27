# Person Detector

Sprint 4 adds real-time person detection with Ultralytics YOLO.

The runtime flow is:

```text
CameraService -> FrameManager -> PersonDetector -> ObjectTracker -> OpenCV preview
```

No ball detection, rim detection, tracking or AI analytics are implemented in this sprint.

## Location

```text
src/vjc_hoops_ai/infrastructure/vision/person_detector.py
```

## Model

The default model is:

```text
yolov8n.pt
```

Ultralytics downloads this model automatically the first time `YOLO("yolov8n.pt")` runs if it is not already available locally. This requires internet access during the first run.

You can also pre-download it by running any Ultralytics command that references the model, for example:

```powershell
yolo predict model=yolov8n.pt source=0 classes=0
```

## Scope

`PersonDetector` requests only COCO class `0`, which corresponds to `person`.

The detector returns lightweight `PersonDetection` objects with:

- Bounding box coordinates.
- Confidence.

Tracking is handled separately by `ObjectTracker`; the detector does not assign identities. The OpenCV drawing remains in `main.py`, while YOLO remains inside the infrastructure vision adapter.

## Run

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python main.py
```

Press `q` to exit.

## Architecture Boundary

YOLO is imported only inside:

```text
src/vjc_hoops_ai/infrastructure/vision/person_detector.py
```

The domain and application layers do not import Ultralytics, YOLO or OpenCV.
