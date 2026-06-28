# 🏀 VJC Hoops AI

> **Una plataforma de entrenamiento de baloncesto con IA, desarrollada con visión artificial, aprendizaje profundo y tecnología de juegos.**

![Estado](https://img.shields.io/badge/Status-In%20Development-orange)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![YOLO](https://img.shields.io/badge/YOLO-Ultralytics-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red)
![Godot](https://img.shields.io/badge/Godot-4.x-purple)
![Licencia](https://img.shields.io/badge/License-MIT-blue)

---

# 📖 Resumen

**VJC Hoops AI** es una plataforma inteligente de entrenamiento de baloncesto que combina **Inteligencia Artificial**, **Visión por Computadora** y una **interfaz de juego 2D** para analizar el rendimiento del jugador en tiempo real.

El proyecto se divide en dos componentes principales:

* **Motor de IA (Python):** Responsable de la visión por computadora, la detección de jugadores, el seguimiento de objetos, la biomecánica, el análisis de tiros y las métricas de rendimiento.

* **Cliente de juego (Godot 4):** Responsable de la interfaz de usuario, los menús, la personalización de personajes, los paneles de control, el sistema de progresión y la experiencia general del usuario.

El objetivo es crear un asistente de baloncesto profesional capaz de ayudar a los jugadores a mejorar su mecánica de tiro mediante retroalimentación basada en IA.

--

# 🎯 Objetivos principales

* Detectar jugadores de baloncesto en tiempo real.

* Realizar un seguimiento constante de los jugadores a lo largo de los fotogramas.

* Detectar tiros de baloncesto.

* Calcular el porcentaje de acierto en los tiros.

* Estimar el ángulo de tiro y la mecánica de lanzamiento.

* Analizar la postura del jugador.
* Genera estadísticas de rendimiento automáticamente.

* Proporciona retroalimentación visual a través de una interfaz de juego interactiva.

* Admite futuras funciones multijugador, clasificaciones, logros y sincronización en la nube.

--

# 🏗️ Arquitectura del proyecto

El proyecto sigue la **Arquitectura Limpia** para mantener la lógica de negocio independiente de tecnologías externas.

```texto
Cámara

│

▼
Servicio de cámara

│

▼
Administrador de fotogramas

│

▼
Detector de personas (YOLO)

│
▼
Rastreador de objetos

│
▼
Módulos futuros
├── Detector de pelota
├── Estimación de pose
├── Detección de cancha
├── Detección de tiro
├── Estadísticas
└── Panel de control
```

La visualización y la interfaz del juego se desarrollaron de forma independiente utilizando **Godot 4**.

---

# 🛠️ Tecnologías

## Inteligencia Artificial

* Python
* OpenCV
* Ultralytics YOLO
* NumPy

## Desarrollo de Juegos

* Godot 4
* GDScript
* Pixel Art 2D

## Desarrollo

* Git
* GitHub
* Visual Studio Code
* Codex / ChatGPT

---
# 📂 Estructura del Repositorio

```texto
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

Se añadirán directorios adicionales durante el desarrollo:

```texto
juego/
assets/
sprites/
audio/
fonts/
effects/
```

---

# 🚀 Progreso actual

| Sprint | Funcionalidad | Estado |

| -------- | ---------------- | ----------- |

| Sprint 1 | Gestor de fotogramas | ✅ Completado |

| Sprint 2 | Servicio de cámara | ✅ Completado |

| Sprint 3 | Vista previa de vídeo | ✅ Completado |

| Sprint 4 | Detección de personas | ✅ Completado |

| Sprint 5 | Seguimiento de objetos | ✅ Completado |

| Sprint 6 | Estimación de pose | 🔄 Planificado |

| Sprint 7 | Detección de balón | 🔄 Planificado |

| Sprint 8 | Detección de cancha | 🔄 Planificado |

| Sprint 9 | Detección de tiro | 🔄 Planificado |

---

# ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Julio2006Cesar/VJC-Hoops-AI.git
cd VJC-Hoops-AI
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno:

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Instalar el proyecto:

```bash
pip install -e . ```

---

# ▶️ Ejecución

Iniciar la vista previa de la IA:

```bash
python main.py
```

La implementación actual ofrece:

* Captura de cámara web
* Detección de personas
* Identificadores de seguimiento persistentes
* Contador de FPS
* Visualización en tiempo real con OpenCV

---

# 🧪 Pruebas

Ejecutar todas las pruebas:

```bash
python -m unittest discover -s tests
```

---

# 📚 Documentación

El repositorio incluye documentación detallada en el directorio `docs/`.

La documentación futura también incluirá:

* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md

Estos documentos tienen como objetivo ayudar tanto a los desarrolladores como a los asistentes de IA a comprender y continuar el proyecto de forma coherente.

---

# 🎮 Próximas funciones

* Detección de baloncesto
* Estimación de pose
* Reconocimiento de tiros
* Análisis de trayectoria de tiro
* Biomecánica
* Panel de rendimiento
* Personalización de personajes
* Progresión del jugador
* Logros
* Desafíos multijugador
* Sincronización en la nube
* Compatibilidad con dispositivos móviles
* Asistente de IA para entrenadores

---

# 🤝 Contribuciones

Se agradecen las contribuciones, sugerencias y mejoras.

Antes de enviar cambios:

* Sigue la arquitectura del proyecto.

* Mantén los módulos independientes.

* Escribe pruebas al añadir nuevas funcionalidades.

* Actualiza la documentación si es necesario.

---

# 📄 Licencia

Este proyecto se publica bajo la Licencia MIT.

---

# 👨‍💻 Autor

**Julio César**

Creador de **VJC Hoops AI**

A lon