import unittest
from typing import Any

from vjc_hoops_ai.infrastructure.vision import PERSON_CLASS_ID, PersonDetector


class FakeBoxes:
    def __init__(
        self,
        xyxy: list[list[float]],
        conf: list[float],
        cls: list[int],
    ) -> None:
        self.xyxy = xyxy
        self.conf = conf
        self.cls = cls


class FakeResult:
    def __init__(self, boxes: FakeBoxes | None) -> None:
        self.boxes = boxes


class FakeModel:
    def __init__(self, results: list[FakeResult]) -> None:
        self.results = results
        self.calls: list[dict[str, Any]] = []

    def __call__(
        self,
        frame_data: Any,
        classes: list[int],
        verbose: bool,
    ) -> list[FakeResult]:
        self.calls.append(
            {"frame_data": frame_data, "classes": classes, "verbose": verbose}
        )
        return self.results


class PersonDetectorTest(unittest.TestCase):
    def test_loads_model_once_at_startup(self) -> None:
        load_calls: list[str] = []

        def loader(model_path: str) -> FakeModel:
            load_calls.append(model_path)
            return FakeModel([])

        detector = PersonDetector(model_path="test-model.pt", model_loader=loader)

        detector.detect("frame-0")
        detector.detect("frame-1")

        self.assertEqual(load_calls, ["test-model.pt"])

    def test_detect_filters_person_class(self) -> None:
        model = FakeModel(
            [
                FakeResult(
                    FakeBoxes(
                        xyxy=[[10.2, 20.8, 30.9, 40.1], [1.0, 2.0, 3.0, 4.0]],
                        conf=[0.91, 0.42],
                        cls=[PERSON_CLASS_ID, 32],
                    )
                )
            ]
        )
        detector = PersonDetector(model_loader=lambda _: model)

        detections = detector.detect("frame-data")

        self.assertEqual(len(detections), 1)
        self.assertEqual(detections[0].x_min, 10)
        self.assertEqual(detections[0].y_min, 20)
        self.assertEqual(detections[0].x_max, 30)
        self.assertEqual(detections[0].y_max, 40)
        self.assertEqual(detections[0].confidence, 0.91)
        self.assertEqual(model.calls[0]["classes"], [PERSON_CLASS_ID])
        self.assertFalse(model.calls[0]["verbose"])

    def test_detect_returns_empty_list_when_result_has_no_boxes(self) -> None:
        detector = PersonDetector(model_loader=lambda _: FakeModel([FakeResult(None)]))

        self.assertEqual(detector.detect("frame-data"), [])


if __name__ == "__main__":
    unittest.main()
