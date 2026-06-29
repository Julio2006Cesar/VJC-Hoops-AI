"""
===========================================================
 VJC Hoops AI
 Project Structure Generator

 Este script crea automáticamente toda la estructura
 oficial del proyecto.

 Autor: VJC Company
===========================================================
"""

from pathlib import Path


PROJECT_STRUCTURE = [
    # ------------------------------------------------------------------
    # Assets
    # ------------------------------------------------------------------
    "assets",
    "assets/fonts",
    "assets/icons",
    "assets/images",
    "assets/images/backgrounds",
    "assets/images/characters",
    "assets/images/ui",
    "assets/images/logos",
    "assets/shaders",
    "assets/sounds",
    "assets/sounds/music",
    "assets/sounds/sfx",
    "assets/videos",

    # ------------------------------------------------------------------
    # Config
    # ------------------------------------------------------------------
    "config",
    "config/camera",
    "config/game",
    "config/ia",
    "config/logging",

    # ------------------------------------------------------------------
    # Data
    # ------------------------------------------------------------------
    "data",
    "data/datasets",
    "data/exports",
    "data/imports",
    "data/profiles",
    "data/sessions",
    "data/statistics",

    # ------------------------------------------------------------------
    # Docs
    # ------------------------------------------------------------------
    "docs",
    "docs/images",
    "docs/manuals",

    # ------------------------------------------------------------------
    # Logs
    # ------------------------------------------------------------------
    "logs",

    # ------------------------------------------------------------------
    # Models
    # ------------------------------------------------------------------
    "models",
    "models/ball",
    "models/person",
    "models/rim",

    # ------------------------------------------------------------------
    # Source
    # ------------------------------------------------------------------
    "src",

    "src/application",
    "src/application/ai",
    "src/application/camera",
    "src/application/profile",
    "src/application/session",
    "src/application/shots",
    "src/application/statistics",
    "src/application/training",

    "src/domain",
    "src/domain/entities",
    "src/domain/events",
    "src/domain/exceptions",
    "src/domain/interfaces",
    "src/domain/services",
    "src/domain/value_objects",

    "src/infrastructure",
    "src/infrastructure/camera",
    "src/infrastructure/database",
    "src/infrastructure/detectors",
    "src/infrastructure/storage",
    "src/infrastructure/tracking",

    "src/presentation",
    "src/presentation/api",
    "src/presentation/godot",
    "src/presentation/ui",

    "src/shared",
    "src/shared/constants",
    "src/shared/helpers",
    "src/shared/logger",
    "src/shared/utils",

    # ------------------------------------------------------------------
    # Tests
    # ------------------------------------------------------------------
    "tests",
    "tests/integration",
    "tests/performance",
    "tests/unit",

    # ------------------------------------------------------------------
    # Scripts
    # ------------------------------------------------------------------
    "scripts",

    # ------------------------------------------------------------------
    # Tools
    # ------------------------------------------------------------------
    "tools",

    # ------------------------------------------------------------------
    # GitHub
    # ------------------------------------------------------------------
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
]


def create_structure():
    root = Path.cwd()

    created = 0

    print("\n==========================================")
    print("  VJC Hoops AI")
    print("  Creating project structure...")
    print("==========================================\n")

    for folder in PROJECT_STRUCTURE:
        path = root / folder

        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"✅ {folder}")
            created += 1
        else:
            print(f"⚪ {folder} (already exists)")

    print("\n==========================================")
    print(f"Folders created: {created}")
    print("Project structure ready.")
    print("==========================================\n")


if __name__ == "__main__":
    create_structure()