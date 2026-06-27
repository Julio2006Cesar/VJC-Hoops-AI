"""Video adapters."""

from vjc_hoops_ai.infrastructure.video.camera_service import (
    CameraService,
    CameraServiceError,
    CameraUnavailableError,
)

__all__ = ["CameraService", "CameraServiceError", "CameraUnavailableError"]
