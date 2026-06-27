"""YOLO-backed person detector."""

from collections.abc import Callable, Sequence
from dataclasses import dataclass
from typing import Any


PERSON_CLASS_ID = 0
DEFAULT_MODEL_PATH = "yolov8n.pt"


@dataclass(frozen=True, slots=True)
class PersonDetection:
    """Person detection produced by the infrastructure YOLO adapter."""

    x_min: int
    y_min: int
    x_max: int
    y_max: int
    confidence: float


ModelLoader = Callable[[str], Any]


class PersonDetector:
    """Detect people using an Ultralytics YOLO model."""

    def __init__(
        self,
        model_path: str = DEFAULT_MODEL_PATH,
        model_loader: ModelLoader | None = None,
    ) -> None:
        self._model_path = model_path
        self._model = self._load_model(model_loader)

    @property
    def model_path(self) -> str:
        return self._model_path

    def detect(self, frame_data: Any) -> list[PersonDetection]:
        results = self._model(frame_data, classes=[PERSON_CLASS_ID], verbose=False)
        detections: list[PersonDetection] = []

        for result in results:
            boxes = getattr(result, "boxes", None)
            if boxes is None:
                continue

            coordinates = _as_sequence(getattr(boxes, "xyxy", []))
            confidences = _as_sequence(getattr(boxes, "conf", []))
            class_ids = _as_sequence(getattr(boxes, "cls", []))

            for xyxy, confidence, class_id in zip(coordinates, confidences, class_ids):
                if int(class_id) != PERSON_CLASS_ID:
                    continue

                x_min, y_min, x_max, y_max = xyxy
                detections.append(
                    PersonDetection(
                        x_min=int(x_min),
                        y_min=int(y_min),
                        x_max=int(x_max),
                        y_max=int(y_max),
                        confidence=float(confidence),
                    )
                )

        return detections

    def _load_model(self, model_loader: ModelLoader | None) -> Any:
        if model_loader is not None:
            return model_loader(self._model_path)

        from ultralytics import YOLO

        return YOLO(self._model_path)


def _as_sequence(value: Any) -> Sequence[Any]:
    if hasattr(value, "cpu"):
        value = value.cpu()

    if hasattr(value, "numpy"):
        value = value.numpy()

    if hasattr(value, "tolist"):
        return value.tolist()

    return value
