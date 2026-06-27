# 🏀 VJC Hoops AI

# PROJECT_CONTEXT.md

## Official Project Documentation

---

# Document Information

| Field                | Value              |
| -------------------- | ------------------ |
| Project Name         | VJC Hoops AI       |
| Version              | 1.0                |
| Project Status       | Pre-Alpha          |
| Architecture         | Clean Architecture |
| Programming Language | Python 3.11+       |
| Repository           | VJC-Hoops-AI       |
| Main Author          | Julio César        |
| Documentation Owner  | ChatGPT + Codex    |

---

# Table of Contents

1. Introduction
2. Project Vision
3. Mission
4. Long-Term Goals
5. Project Philosophy
6. Current Status
7. Project Scope
8. Architecture Overview
9. Folder Structure
10. Technology Stack
11. Development Principles
12. Sprint History
13. Future Roadmap
14. AI Development Rules

---

# 1. Introduction

## What is VJC Hoops AI?

VJC Hoops AI is a professional basketball analysis platform that combines Artificial Intelligence, Computer Vision, Game Development and Data Analytics.

Unlike traditional sports analysis software, the objective is not only to detect players or analyze videos.

The long-term vision is to build an entire ecosystem capable of:

* Detecting players.
* Detecting the basketball.
* Tracking every object.
* Calculating advanced basketball statistics.
* Assisting coaches with AI.
* Creating training reports automatically.
* Motivating athletes through gamification.
* Connecting real-world training with a video game.

This project is intentionally designed to be modular, scalable and maintainable for many years.

---

# 2. Project Vision

## Vision Statement

Create one of the most complete open basketball analysis platforms powered by Artificial Intelligence.

The project should eventually become useful for:

* Basketball coaches
* Players
* Basketball academies
* Universities
* Professional teams
* Amateur leagues
* Sports researchers

The software should be capable of analyzing complete games automatically while also providing an engaging experience inspired by modern video games.

---

# 3. Mission

The mission of VJC Hoops AI is to reduce the amount of manual work required to analyze basketball games.

Instead of spending hours reviewing videos, coaches should receive:

* Automatic statistics
* Shot charts
* Heat maps
* Player reports
* Training recommendations
* Performance evolution

Everything generated automatically by AI.

---

# 4. Long-Term Goals

The project roadmap extends far beyond simple player detection.

Final objectives include:

### Basketball Analysis

* Person Detection
* Ball Detection
* Hoop Detection
* Court Detection
* Player Tracking
* Ball Tracking
* Pose Estimation
* Shot Detection
* Rebound Detection
* Assist Detection
* Turnover Detection
* Foul Detection

### Statistics

* FG%
* 3PT%
* FT%
* Offensive Rating
* Defensive Rating
* Player Efficiency
* Shooting Charts
* Heat Maps

### Artificial Intelligence

* Training Recommendations
* Weakness Detection
* Automatic Highlights
* Tactical Suggestions

### Game Integration

A unique feature of VJC Hoops AI is that real-world training data will be connected to a future basketball RPG.

Players improve in real life.

Their in-game character improves as well.

---

# 5. Project Philosophy

Every architectural decision must follow the following philosophy.

## Rule 1

Code must be understandable.

Readable code is more valuable than clever code.

---

## Rule 2

Architecture comes before speed.

Never sacrifice architecture for quick implementations.

---

## Rule 3

The project must be modular.

Every module should be replaceable without affecting the rest of the system.

---

## Rule 4

Testing is mandatory.

Every feature should include automated tests whenever possible.

---

## Rule 5

Documentation is part of the product.

If a feature is undocumented, it is considered incomplete.

---

## Rule 6

Never break existing functionality.

Backward compatibility is important whenever practical.

---

# 6. Current Project Status

Current Version

Pre-Alpha

Completed Sprints

✔ Sprint 0 – Project Setup

✔ Sprint 1 – Frame Manager

✔ Sprint 2 – Camera Service

✔ Sprint 3 – Video Visualization

✔ Sprint 4 – Person Detection

✔ Sprint 5 – Object Tracking

Current Development Stage

The software is capable of:

* Reading frames from a camera.
* Managing video frames.
* Detecting people using YOLO.
* Tracking detected players.
* Displaying detections in real time.

Current Pipeline

Camera

↓

FrameManager

↓

PersonDetector

↓

ObjectTracker

↓

Visualization

The project is stable enough to continue with Ball Detection.

---

# 7. Project Scope

This project is divided into two major systems.

## System A

Basketball Analysis Platform

Responsible for:

* AI
* Vision
* Statistics
* Reports

---

## System B

Basketball RPG

Responsible for:

* Character Progression
* Customization
* Inventory
* Experience
* Challenges
* Achievements
* Online Profile

These two systems are independent but connected through player progression.

---

# 8. Architecture Overview

The software follows Clean Architecture.

The goal is to isolate business logic from external technologies.

Layers

Presentation

↓

Application

↓

Domain

↓

Infrastructure

Responsibilities

Presentation

* User Interface
* Menus
* Game
* Desktop App

Application

* Use Cases
* Business Workflows

Domain

* Core Business Rules
* Entities
* Value Objects

Infrastructure

* Camera
* OpenCV
* YOLO
* Database
* File System
* APIs

Dependencies always point inward.

Domain never depends on Infrastructure.

---

# 9. Folder Structure

src/

```
vjc_hoops_ai/

    domain/

    application/

    infrastructure/

        video/

        vision/

        tracking/

    interfaces/

    config/
```

tests/

```
unit/

integration/
```

docs/

models/

data/

```
raw/

processed/
```

assets/

future/

This structure must remain organized as the project grows.

---

# 10. Technology Stack

Programming Language

Python 3.11+

Computer Vision

OpenCV

Object Detection

Ultralytics YOLO

Deep Learning

PyTorch

Numerical Computing

NumPy

Testing

unittest

Version Control

Git

Remote Repository

GitHub

IDE

Visual Studio Code

Artificial Intelligence Assistants

ChatGPT

Codex

Claude

Gemini

Cursor

---

# 11. Development Principles

Every contributor must respect these principles.

* Clean Architecture.
* SOLID principles.
* Dependency Inversion.
* Single Responsibility.
* Testability.
* Readability.
* Maintainability.
* Scalability.

Performance optimizations should never reduce maintainability unless absolutely necessary.

---

# 12. Sprint History

Sprint 0

Project initialization.

Sprint 1

Frame acquisition architecture.

Sprint 2

Camera abstraction.

Sprint 3

Video preview.

Sprint 4

Person detection.

Sprint 5

Object tracking.

Future sprints will continue expanding the AI pipeline.

---

# 13. Initial Roadmap

Sprint 6

Detection Manager

Sprint 7

Ball Detection

Sprint 8

Hoop Detection

Sprint 9

Ball Tracking

Sprint 10

Shot Detection

Sprint 11

Shot Classification

Sprint 12

Heat Maps

Sprint 13

Statistics Engine

Sprint 14

Player Reports

Sprint 15

Career Mode

Sprint 16

Character Customization

Sprint 17

Cloud Synchronization

Sprint 18

REST API

Sprint 19

Game Integration

Sprint 20

Version 1.0

---

# 14. Rules for Any AI

If an AI contributes to this repository, it must follow these rules.

NEVER:

* Import OpenCV into Domain.
* Import YOLO into Domain.
* Mix UI with business logic.
* Delete tests without replacement.
* Introduce unnecessary dependencies.

ALWAYS:

* Respect Clean Architecture.
* Update documentation.
* Add tests.
* Keep modules independent.
* Write readable code.
* Preserve project vision.

Before implementing a feature:

1. Understand the architecture.
2. Identify the correct layer.
3. Write or update tests.
4. Implement the feature.
5. Validate functionality.
6. Update documentation.
7. Commit using a clear sprint-based message.

---

# End of Part 1

The following sections (Parts 2, 3 and 4) expand the AI pipeline, RPG system, game design, customization, database, APIs, deployment strategy and long-term roadmap.
