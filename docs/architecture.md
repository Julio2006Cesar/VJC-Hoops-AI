# Architecture Notes

VJC Hoops AI is organized around Clean Architecture boundaries.

The domain layer must not import OpenCV, YOLO, MediaPipe, FastAPI, PostgreSQL drivers, or filesystem-specific implementations.

Application use cases coordinate domain concepts through ports. Infrastructure modules provide concrete adapters for video processing, computer vision models and persistence. Interface modules expose the application through APIs or command-line entry points.
