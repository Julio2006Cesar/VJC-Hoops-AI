import unittest

from vjc_hoops_ai.application.use_cases import FrameManager
from vjc_hoops_ai.domain.value_objects import Frame


class FakeFrameSource:
    def __init__(self, frames: list[Frame], source_id: str = "fake-source") -> None:
        self._frames = frames
        self._cursor = 0
        self._open_count = 0
        self._close_count = 0
        self._source_id = source_id

    @property
    def source_id(self) -> str:
        return self._source_id

    @property
    def open_count(self) -> int:
        return self._open_count

    @property
    def close_count(self) -> int:
        return self._close_count

    def open(self) -> None:
        self._open_count += 1

    def read(self) -> Frame | None:
        if self._cursor >= len(self._frames):
            return None

        frame = self._frames[self._cursor]
        self._cursor += 1
        return frame

    def close(self) -> None:
        self._close_count += 1


class FrameManagerTest(unittest.TestCase):
    def test_read_next_opens_source_once(self) -> None:
        source = FakeFrameSource([Frame(data="frame-0", index=0)])
        manager = FrameManager(source)

        frame = manager.read_next()
        manager.read_next()

        self.assertEqual(frame, Frame(data="frame-0", index=0))
        self.assertEqual(source.open_count, 1)

    def test_iter_frames_reads_until_source_is_exhausted(self) -> None:
        source = FakeFrameSource(
            [
                Frame(data="frame-0", index=0, timestamp_seconds=0.0),
                Frame(data="frame-1", index=1, timestamp_seconds=0.033),
            ]
        )
        manager = FrameManager(source)

        frames = list(manager.iter_frames())

        self.assertEqual([frame.index for frame in frames], [0, 1])
        self.assertEqual([frame.data for frame in frames], ["frame-0", "frame-1"])

    def test_iter_frames_respects_limit(self) -> None:
        source = FakeFrameSource(
            [
                Frame(data="frame-0", index=0),
                Frame(data="frame-1", index=1),
                Frame(data="frame-2", index=2),
            ]
        )
        manager = FrameManager(source)

        frames = list(manager.iter_frames(limit=2))

        self.assertEqual([frame.index for frame in frames], [0, 1])

    def test_context_manager_closes_source(self) -> None:
        source = FakeFrameSource([Frame(data="frame-0", index=0)])

        with FrameManager(source) as manager:
            self.assertEqual(manager.read_next(), Frame(data="frame-0", index=0))

        self.assertEqual(source.open_count, 1)
        self.assertEqual(source.close_count, 1)

    def test_frame_rejects_negative_index(self) -> None:
        with self.assertRaisesRegex(ValueError, "index"):
            Frame(data="invalid", index=-1)


if __name__ == "__main__":
    unittest.main()
