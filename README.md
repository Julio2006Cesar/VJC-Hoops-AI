# VJC Hoops AI

Aplicacion profesional para analisis de rendimiento en baloncesto mediante Inteligencia Artificial y Vision por Computadora.

El objetivo de este repositorio es preparar una base limpia, modular y escalable para construir progresivamente deteccion de jugadores, balon, aro, cancha, trayectorias, precision de tiro, Shot Meter, estadisticas, heatmaps, minimapa e integracion futura con un videojuego pixel art.

## Estado actual

Fase inicial de arquitectura.

No se implementa IA todavia. El proyecto queda preparado para comenzar el desarrollo profesional sin acoplar logica de dominio a librerias externas.

## Stack previsto

- Python
- OpenCV
- Ultralytics YOLO
- NumPy
- MediaPipe
- FastAPI
- PostgreSQL

## Arquitectura

El proyecto sigue una orientacion de Clean Architecture:

```text
src/vjc_hoops_ai/
├── domain/              # Reglas y conceptos centrales del negocio
├── application/         # Casos de uso y puertos
├── infrastructure/      # OpenCV, YOLO, video, persistencia e integraciones
├── interfaces/          # API, CLI y adaptadores de entrada
└── config/              # Configuracion de la aplicacion
```

### Capas

- `domain`: entidades, value objects y contratos propios del analisis de baloncesto.
- `application`: orquestacion de casos de uso sin depender de frameworks externos.
- `infrastructure`: implementaciones concretas con OpenCV, YOLO, MediaPipe, almacenamiento y servicios externos.
- `interfaces`: puntos de entrada como FastAPI o CLI.
- `config`: configuracion centralizada por entorno.

## Estructura

```text
vjc-hoops-ai/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── models/
├── src/
│   └── vjc_hoops_ai/
│       ├── application/
│       │   ├── ports/
│       │   └── use_cases/
│       ├── config/
│       ├── domain/
│       │   ├── entities/
│       │   ├── repositories/
│       │   └── value_objects/
│       ├── infrastructure/
│       │   ├── computer_vision/
│       │   ├── persistence/
│       │   └── video/
│       └── interfaces/
│           ├── api/
│           └── cli/
├── tests/
│   ├── integration/
│   └── unit/
├── .env.example
├── .gitignore
├── pyproject.toml
└── requirements.txt
```

## Instalacion local

Desde la carpeta del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests
```

## Ejecutar Visualizacion De Video

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
python main.py
```

La aplicacion abre `CameraService(camera_index=0)`, conecta la fuente con `FrameManager`, detecta personas, mantiene IDs de seguimiento, muestra FPS sobre la imagen y se cierra al presionar `q`.

## Principios de desarrollo

- Mantener el dominio independiente de OpenCV, YOLO, MediaPipe, FastAPI y PostgreSQL.
- Introducir dependencias externas solo dentro de `infrastructure` o `interfaces`.
- Crear casos de uso antes de conectar frameworks.
- Evitar notebooks como fuente principal de logica de produccion.
- Versionar codigo y configuracion, no videos, datasets, pesos de modelos ni artefactos generados.

## Roadmap tecnico

1. Definir entidades de dominio: jugador, balon, aro, cancha, tiro y frame analizado.
2. Crear puertos de deteccion y procesamiento de video.
3. Implementar adaptadores con OpenCV.
4. Integrar YOLO para deteccion de objetos.
5. Incorporar MediaPipe para analisis corporal si aplica.
6. Calcular trayectorias y metricas de tiro.
7. Exponer casos de uso mediante FastAPI.
8. Persistir sesiones, eventos y estadisticas en PostgreSQL.
9. Preparar salida compatible con visualizaciones, heatmaps, minimapa y videojuego pixel art.

## Modulos iniciales

- Frame Manager: coordinacion de lectura de frames desde fuentes de video sin acoplar el nucleo a OpenCV. Ver `docs/frame-manager.md`.
- Camera Service: adaptador de infraestructura para camaras locales mediante OpenCV. Ver `docs/camera-service.md`.
- Video Visualization: aplicacion minima para comprobar camara, frame manager y FPS en ventana OpenCV. Ver `docs/video-visualization.md`.
- Person Detector: adaptador YOLO para detectar unicamente personas en tiempo real. Ver `docs/person-detector.md`.
- Object Tracker: motor simple de seguimiento por IoU para mantener IDs entre frames. Ver `docs/object-tracker.md`.

## Convenciones

- Codigo fuente en `src/`.
- Tests unitarios en `tests/unit/`.
- Tests de integracion en `tests/integration/`.
- Videos originales en `data/raw/`.
- Datos procesados en `data/processed/`.
- Pesos de modelos en `models/`.

Los directorios `data/` y `models/` estan preparados, pero sus contenidos pesados quedan fuera de Git por defecto.
