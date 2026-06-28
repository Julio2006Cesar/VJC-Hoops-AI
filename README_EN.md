# 🏀 VJC Hoops AI

> **An AI-powered basketball training platform built with Computer Vision, Deep Learning, and Game Technology.**

![Status](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Godot](https://img.shields.io/badge/Godot-4.x-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Overview

**VJC Hoops AI** is an intelligent basketball training platform that combines **Artificial Intelligence**, **Computer Vision**, and a **2D game interface** to analyze player performance in real time.

The project is divided into two major components:

* **AI Engine (Python):** Responsible for computer vision, player detection, object tracking, biomechanics, shot analysis, and performance metrics.
* **Game Client (Godot 4):** Responsible for the user interface, menus, character customization, dashboards, progression system, and overall user experience.

The goal is to create a professional basketball assistant capable of helping players improve their shooting mechanics through AI-powered feedback.

---

# 🎯 Main Objectives

* Detect basketball players in real time.
* Track players consistently across frames.
* Detect basketball shots.
* Calculate shooting percentage.
* Estimate shooting angle and release mechanics.
* Analyze player posture.
* Generate performance statistics automatically.
* Provide visual feedback through an interactive game interface.
* Support future multiplayer, rankings, achievements, and cloud synchronization.

---

# 🏗️ Project Architecture

The project follows **Clean Architecture** to keep business logic independent from external technologies.

```text
Camera
   │
   ▼
CameraService
   │
   ▼
FrameManager
   │
   ▼
PersonDetector (YOLO)
   │
   ▼
ObjectTracker
   │
   ▼
Future Modules
   ├── Ball Detector
   ├── Pose Estimation
   ├── Court Detection
   ├── Shot Detection
   ├── Statistics
   └── Dashboard
```

The visualization and game interface are developed independently using **Godot 4**.

---

# 🛠️ Technologies

## Artificial Intelligence

* Python
* OpenCV
* Ultralytics YOLO
* NumPy

## Game Development

* Godot 4
* GDScript
* 2D Pixel Art

## Development

* Git
* GitHub
* Visual Studio Code
* Codex / ChatGPT

---

# 📂 Repository Structure

```text
VJC-Hoops-AI/

src/
tests/
docs/
models/
data/

README.md
PROJECT_CONTEXT.md
PROJECT_ARCHITECTURE.md
ROADMAP.md
```

Additional directories will be added during development:

```text
game/
assets/
sprites/
audio/
fonts/
effects/
```

---

# 🚀 Current Progress

| Sprint   | Feature          | Status      |
| -------- | ---------------- | ----------- |
| Sprint 1 | Frame Manager    | ✅ Completed |
| Sprint 2 | Camera Service   | ✅ Completed |
| Sprint 3 | Video Preview    | ✅ Completed |
| Sprint 4 | Person Detection | ✅ Completed |
| Sprint 5 | Object Tracking  | ✅ Completed |
| Sprint 6 | Pose Estimation  | 🔄 Planned  |
| Sprint 7 | Ball Detection   | 🔄 Planned  |
| Sprint 8 | Court Detection  | 🔄 Planned  |
| Sprint 9 | Shot Detection   | 🔄 Planned  |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Julio2006Cesar/VJC-Hoops-AI.git
cd VJC-Hoops-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the project:

```bash
pip install -e .
```

---

# ▶️ Running

Launch the AI preview:

```bash
python main.py
```

The current implementation provides:

* Webcam capture
* Person detection
* Persistent tracking IDs
* FPS counter
* Live OpenCV visualization

---

# 🧪 Testing

Run all tests:

```bash
python -m unittest discover -s tests
```

---

# 📚 Documentation

The repository includes detailed documentation inside the `docs/` directory.

Future documentation will also include:

* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md

These documents are intended to help both developers and AI assistants understand and continue the project consistently.

---

# 🎮 Future Features

* Basketball detection
* Pose estimation
* Shot recognition
* Shooting trajectory analysis
* Biomechanics
* Performance dashboard
* Character customization
* Player progression
* Achievements
* Multiplayer challenges
* Cloud synchronization
* Mobile support
* Coach AI Assistant

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Before submitting changes:

* Follow the project architecture.
* Keep modules independent.
* Write tests when adding new functionality.
* Update documentation if necessary.

---

# 📄 License

This project is released under the MIT License.

---

# 👨‍💻 Author

**Julio César**

Creator of **VJC Hoops AI**

A long-term project focused on combining Artificial Intelligence, Computer Vision, and Game Development to create an intelligent basketball training platform.
