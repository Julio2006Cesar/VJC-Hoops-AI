# ROADMAP.md

# Hoja de Ruta Oficial de VJC Hoops AI

**Versión:** 1.0

**Estado:** En planificación

**Última actualización:** Junio 2026

---

# Índice

1. Introducción
2. Metodología de desarrollo
3. Organización de los Sprints
4. Sprint 0 – Preparación del proyecto
5. Sprint 1 – Arquitectura base
6. Sprint 2 – Cliente Godot
7. Sprint 3 – Comunicación Python ↔ Godot
8. Sprint 4 – Captura de cámara
9. Sprint 5 – Detección de personas
10. Sprint 6 – Detección del balón
11. Sprint 7 – Detección del aro
12. Sprint 8 – Seguimiento de objetos
13. Sprint 9 – Detección de tiros
14. Sprint 10 – Estadísticas
15. Sprint 11 – Dashboard
16. Sprint 12 – Personalización del jugador
17. Sprint 13 – Optimización
18. Sprint 14 – Beta pública
19. Sprint 15 – Versión 1.0
20. Evolución futura

---

# 1. Introducción

## 1.1 Propósito

Este documento define la hoja de ruta oficial para el desarrollo de VJC Hoops AI.

Su objetivo es organizar el trabajo en etapas claras y progresivas, permitiendo que cualquier desarrollador o Inteligencia Artificial conozca el estado del proyecto, las prioridades y los objetivos de cada fase.

El roadmap complementa a `PROJECT_CONTEXT.md` y `PROJECT_ARCHITECTURE.md`.

Mientras esos documentos describen la visión y la arquitectura del sistema, este documento explica **qué se desarrollará, en qué orden y con qué criterios de finalización**.

---

## 1.2 Objetivos

El roadmap tiene los siguientes objetivos.

* Organizar el desarrollo en etapas.
* Reducir la improvisación.
* Priorizar funcionalidades.
* Facilitar la colaboración.
* Permitir la continuidad entre diferentes IA y desarrolladores.
* Mantener un historial claro del progreso.

---

# 2. Metodología de Desarrollo

El proyecto seguirá una metodología basada en Sprints.

Cada Sprint tendrá un objetivo concreto y deberá finalizar con una funcionalidad completamente operativa y documentada.

Todos los Sprints utilizarán la siguiente plantilla.

* Objetivo.
* Descripción.
* Prioridad.
* Dependencias.
* Archivos implicados.
* Tareas principales.
* Criterios de aceptación.
* Riesgos.
* Estado.
* Notas para futuras IA.

Ningún Sprint deberá considerarse finalizado si no cumple sus criterios de aceptación y la documentación correspondiente.

---

# 3. Organización de los Sprints

El desarrollo seguirá un enfoque incremental.

Cada Sprint añadirá nuevas capacidades sin comprometer la estabilidad del sistema.

Antes de comenzar un Sprint deberán cumplirse las siguientes condiciones.

* El Sprint anterior debe estar finalizado.
* La documentación debe estar actualizada.
* Las pruebas del Sprint anterior deben ejecutarse correctamente.
* Los cambios deben estar registrados en `CHANGELOG.md`.

Esta disciplina permitirá mantener un proyecto ordenado y facilitará el trabajo colaborativo entre personas e Inteligencias Artificiales.

---
# 4. Sprint 0 — Preparación del Proyecto

## Estado

🟡 Pendiente

---

## Objetivo

Preparar toda la infraestructura del proyecto antes de escribir la primera línea de código funcional.

Este Sprint establece las bases del repositorio, la documentación, la estructura de carpetas y las herramientas que utilizará el proyecto durante todo su ciclo de vida.

---

## Descripción

Durante este Sprint no se desarrollará ninguna funcionalidad del juego.

El objetivo consiste en construir un entorno profesional de trabajo que permita desarrollar el proyecto de forma organizada, escalable y mantenible.

Todo el equipo de desarrollo y cualquier Inteligencia Artificial deberá utilizar esta configuración como punto de partida.

---

## Herramientas

* Git
* GitHub
* Visual Studio Code
* Python 3.x
* Godot Engine 4.x
* Entorno Virtual (venv)
* GitHub Desktop (opcional)

---

## Documentación

Crear los siguientes documentos.

* README.md
* README_EN.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md
* LICENSE (cuando corresponda)

---

## Organización Inicial

Crear la estructura oficial del proyecto.

```text
src/
assets/
models/
data/
tests/
logs/
config/
docs/
```

---

## Configuración Inicial

Crear.

* Entorno Virtual.
* requirements.txt.
* .gitignore.
* Primera estructura del proyecto.

---

## Tareas

* Crear repositorio.
* Configurar Git.
* Crear documentación.
* Configurar Python.
* Configurar Godot.
* Configurar VSCode.
* Definir arquitectura.
* Publicar primera versión en GitHub.

---

## Archivos Esperados

README.md

README_EN.md

PROJECT_CONTEXT.md

PROJECT_ARCHITECTURE.md

ROADMAP.md

.gitignore

requirements.txt

---

## Criterios de Aceptación

✔ Proyecto publicado.

✔ Documentación creada.

✔ Git funcionando.

✔ Python funcionando.

✔ Godot funcionando.

✔ Arquitectura definida.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

No comenzar el desarrollo del software hasta finalizar completamente este Sprint.

Toda la documentación debe existir antes de escribir código.

---

# 5. Sprint 1 — Arquitectura Base del Backend

## Estado

🟡 Pendiente

---

## Objetivo

Construir la arquitectura principal del backend utilizando Python y la Arquitectura Hexagonal.

Este Sprint establece la estructura sobre la cual se desarrollará toda la lógica del proyecto.

---

## Descripción

Durante este Sprint se crearán únicamente las bases del software.

No se implementará todavía Inteligencia Artificial.

El objetivo consiste en dejar preparada toda la estructura para que los siguientes módulos puedan incorporarse sin modificar la arquitectura.

---

## Carpetas

Crear.

```text
src/

domain/

application/

infrastructure/

presentation/

shared/
```

---

## Archivos Iniciales

Ejemplo.

```text
main.py

config.py

settings.py

logger.py

constants.py
```

---

## Tareas

Crear estructura Hexagonal.

Crear entidades.

Crear interfaces.

Crear casos de uso.

Crear servicios base.

Crear configuración.

Crear sistema de logs.

Crear manejo de excepciones.

---

## Objetivos Técnicos

* Arquitectura limpia.
* Bajo acoplamiento.
* Alta cohesión.
* Preparación para IA.
* Preparación para Godot.

---

## Criterios de Aceptación

✔ Arquitectura creada.

✔ Código organizado.

✔ Proyecto ejecutable.

✔ Logging funcionando.

✔ Configuración funcionando.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

No implementar todavía OpenCV ni YOLO.

Este Sprint únicamente prepara la arquitectura.

---

# 6. Sprint 2 — Configuración Inicial de Godot

## Estado

🟡 Pendiente

---

## Objetivo

Construir la primera versión del cliente gráfico utilizando Godot Engine.

---

## Descripción

Durante este Sprint se desarrollará la estructura visual del proyecto.

No existirá comunicación con Python.

Se prepararán únicamente las escenas principales.

---

## Escenas

Crear.

MainMenu

Login

Lobby

Training

Settings

Profile

CharacterEditor

Dashboard

Credits

---

## Organización

```text
godot/

scenes/

scripts/

themes/

fonts/

textures/

audio/

animations/
```

---

## Tareas

Crear proyecto Godot.

Crear tema principal.

Crear navegación.

Crear escenas.

Crear animaciones básicas.

Crear sistema de cambio entre pantallas.

---

## Objetivos

* Navegación estable.
* UI limpia.
* Preparación para futuras conexiones.

---

## Criterios

✔ Proyecto abre correctamente.

✔ Cambio entre pantallas.

✔ Tema visual funcionando.

✔ Resolución adaptable.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

No conectar todavía con Python.

Todo el trabajo será únicamente visual.

---

# 7. Sprint 3 — Comunicación entre Python y Godot

## Estado

🟡 Pendiente

---

## Objetivo

Permitir que Godot y Python intercambien información de manera estable y desacoplada.

---

## Descripción

Este Sprint implementará el primer puente entre el backend y el cliente gráfico.

Inicialmente se utilizarán archivos JSON como mecanismo de intercambio de datos por su simplicidad y facilidad de depuración.

La arquitectura deberá permitir migrar posteriormente a HTTP o WebSockets sin modificar la lógica del dominio.

---

## Componentes

Backend Python

↓

Exportador JSON

↓

Godot

↓

Dashboard

---

## Tareas

Crear exportador JSON.

Crear lector JSON.

Crear eventos.

Actualizar Dashboard.

Sincronizar configuración.

Validar comunicación.

---

## Datos Compartidos

* Perfil del jugador.
* Configuración.
* Estado del entrenamiento.
* Estadísticas.
* Información de depuración.

---

## Criterios

✔ Python genera JSON.

✔ Godot lee JSON.

✔ Dashboard actualizado.

✔ Comunicación estable.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Diseñar esta capa pensando en reemplazar JSON por WebSockets sin cambiar la arquitectura.

---

# 8. Sprint 4 — Captura de Cámara y Procesamiento Inicial

## Estado

🟡 Pendiente

---

## Objetivo

Implementar el primer módulo funcional del backend encargado de capturar video en tiempo real y preparar los frames para el pipeline de Inteligencia Artificial.

---

## Descripción

Este Sprint marca el inicio del procesamiento de visión por computadora.

El sistema deberá abrir la cámara seleccionada por el usuario, capturar imágenes de forma continua y prepararlas para los módulos de detección que se desarrollarán en los siguientes Sprints.

En esta etapa todavía no se realizará detección de personas ni análisis deportivo.

El objetivo es disponer de un flujo de captura estable, eficiente y desacoplado.

---

## Componentes a Crear

* CameraService
* FrameManager
* FrameBuffer
* CameraConfiguration
* FramePreprocessor

---

## Tareas

* Detectar cámaras disponibles.
* Permitir seleccionar la cámara desde la configuración.
* Capturar video en tiempo real.
* Controlar FPS.
* Redimensionar imágenes.
* Preparar frames para el pipeline.
* Registrar errores de captura.
* Integrar el flujo con la arquitectura existente.

---

## Archivos Previstos

```text
src/infrastructure/camera/

camera_service.py

camera_manager.py

frame_manager.py

frame_buffer.py

camera_config.py

frame_preprocessor.py
```

---

## Criterios de Aceptación

✔ La cámara inicia correctamente.

✔ El flujo de video es estable.

✔ Los FPS se mantienen dentro del objetivo definido.

✔ Los frames llegan preparados para el siguiente Sprint.

✔ El sistema detecta y notifica errores de cámara.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

No implementar todavía modelos de IA.

El objetivo de este Sprint es garantizar un flujo de captura sólido y reutilizable que servirá de base para todos los módulos de visión por computadora posteriores.


# 9. Sprint 5 — Detección de Personas (YOLO)

## Estado

🟡 Pendiente

---

## Objetivo

Integrar el primer modelo de Inteligencia Artificial utilizando YOLO para detectar al jugador dentro del campo de visión de la cámara.

---

## Descripción

Este Sprint implementará el primer módulo de visión por computadora.

El sistema deberá detectar personas en tiempo real utilizando un modelo YOLO optimizado y devolver información estructurada al resto del pipeline.

La detección de personas será la base para todos los módulos posteriores, como el seguimiento del jugador, el análisis de movimientos y la detección de lanzamientos.

---

## Componentes a Crear

* PersonDetector
* DetectionManager
* BoundingBox
* DetectionResult
* PersonRepository

---

## Tareas

* Integrar YOLO.
* Cargar el modelo automáticamente.
* Detectar personas.
* Obtener coordenadas del jugador.
* Dibujar Bounding Boxes (modo depuración).
* Exportar resultados al pipeline.

---

## Archivos Previstos

```text
src/infrastructure/detectors/

person_detector.py
detection_manager.py
detection_result.py
bounding_box.py

models/
yolo_person.pt
```

---

## Criterios de Aceptación

✔ YOLO carga correctamente.

✔ La detección funciona en tiempo real.

✔ Se identifica al jugador correctamente.

✔ El rendimiento es estable.

✔ Los resultados llegan al siguiente módulo.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Mantener el detector desacoplado del resto del sistema para facilitar futuras actualizaciones del modelo.

---

# 10. Sprint 6 — Detección del Balón

## Estado

🟡 Pendiente

---

## Objetivo

Implementar la detección automática del balón de baloncesto.

---

## Descripción

Este Sprint permitirá identificar el balón dentro de cada frame y calcular su posición en tiempo real.

El balón será uno de los elementos principales para determinar la trayectoria del lanzamiento y calcular estadísticas avanzadas.

---

## Componentes a Crear

* BallDetector
* BallTracker
* BallPosition
* BallRepository

---

## Tareas

* Detectar el balón.
* Calcular coordenadas.
* Filtrar falsas detecciones.
* Mantener seguimiento básico.
* Integrar resultados con el pipeline.

---

## Archivos Previstos

```text
src/infrastructure/detectors/

ball_detector.py
ball_tracker.py
ball_position.py

models/
yolo_ball.pt
```

---

## Criterios de Aceptación

✔ El balón es detectado correctamente.

✔ La posición se actualiza en tiempo real.

✔ Se mantiene una tasa baja de falsas detecciones.

✔ El módulo funciona de forma independiente.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Diseñar el módulo pensando en futuras mejoras mediante modelos entrenados específicamente para baloncesto.

---

# 11. Sprint 7 — Detección del Aro

## Estado

🟡 Pendiente

---

## Objetivo

Implementar la detección del aro de baloncesto.

---

## Descripción

El sistema deberá localizar el aro durante toda la sesión de entrenamiento.

Esta referencia será utilizada para determinar si un lanzamiento fue exitoso y calcular la trayectoria del balón.

---

## Componentes a Crear

* RimDetector
* RimPosition
* RimRepository

---

## Tareas

* Detectar el aro.
* Obtener coordenadas.
* Mantener posición estable.
* Validar precisión.
* Integrar resultados con el pipeline.

---

## Archivos Previstos

```text
src/infrastructure/detectors/

rim_detector.py
rim_position.py

models/
yolo_rim.pt
```

---

## Criterios de Aceptación

✔ El aro permanece correctamente identificado.

✔ La posición es estable.

✔ Compatible con distintos fondos.

✔ Integrado con BallDetector.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Permitir sustituir el modelo de detección sin afectar otros módulos.

---

# 12. Sprint 8 — Seguimiento Inteligente de Objetos

## Estado

🟡 Pendiente

---

## Objetivo

Implementar el sistema de seguimiento para mantener la identidad de cada objeto detectado entre distintos frames.

---

## Descripción

Hasta este Sprint únicamente existirán detecciones independientes.

A partir de ahora el sistema deberá comprender que un objeto detectado en un frame corresponde al mismo objeto en los siguientes.

Esto permitirá analizar trayectorias y movimientos.

---

## Componentes a Crear

* ObjectTracker
* TrackManager
* TrackHistory
* MotionPredictor

---

## Tareas

* Asignar ID únicos.
* Mantener seguimiento.
* Recuperar objetos perdidos.
* Calcular velocidad.
* Calcular dirección.
* Integrar BallTracker y PersonTracker.

---

## Archivos Previstos

```text
src/infrastructure/tracking/

object_tracker.py
track_manager.py
track_history.py
motion_predictor.py
```

---

## Criterios de Aceptación

✔ El jugador conserva su ID.

✔ El balón conserva su ID.

✔ El sistema recupera objetos tras pérdidas breves.

✔ Seguimiento estable durante la sesión.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Diseñar el seguimiento de forma modular para poder sustituir el algoritmo sin modificar el resto del sistema.

---

# 13. Sprint 9 — Detección Automática de Lanzamientos

## Estado

🟡 Pendiente

---

## Objetivo

Detectar automáticamente cuándo un jugador realiza un lanzamiento hacia el aro.

---

## Descripción

Este Sprint implementará uno de los módulos más importantes del proyecto.

El sistema deberá identificar el inicio del lanzamiento, seguir la trayectoria del balón y determinar cuándo finaliza la acción.

Esta información será utilizada por el motor de estadísticas.

---

## Componentes a Crear

* ShotDetector
* ShotAnalyzer
* ShotTrajectory
* ShotValidator

---

## Tareas

* Detectar liberación del balón.
* Analizar trayectoria.
* Identificar lanzamiento válido.
* Registrar intentos.
* Enviar eventos al motor de estadísticas.

---

## Archivos Previstos

```text
src/application/shots/

shot_detector.py
shot_analyzer.py
shot_validator.py
trajectory.py
```

---

## Criterios de Aceptación

✔ El sistema identifica lanzamientos correctamente.

✔ La trayectoria se calcula automáticamente.

✔ Se registran todos los intentos.

✔ Compatible con el pipeline existente.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Evitar reglas rígidas. El algoritmo deberá permitir futuras mejoras mediante IA y aprendizaje automático.

---

# 14. Sprint 10 — Motor de Estadísticas

## Estado

🟡 Pendiente

---

## Objetivo

Desarrollar el motor encargado de transformar las detecciones en estadísticas deportivas útiles para el jugador.

---

## Descripción

Este Sprint consolidará toda la información obtenida por el pipeline de visión.

El motor calculará métricas deportivas en tiempo real y almacenará el historial de entrenamiento del usuario.

Será uno de los componentes centrales de VJC Hoops AI.

---

## Componentes a Crear

* StatisticsEngine
* StatisticsCalculator
* SessionAnalyzer
* ReportGenerator
* ExportManager

---

## Tareas

* Contabilizar tiros.
* Calcular aciertos.
* Calcular porcentaje de efectividad.
* Registrar sesiones.
* Generar reportes.
* Exportar resultados.
* Integrar con el Dashboard de Godot.

---

## Archivos Previstos

```text
src/application/statistics/

statistics_engine.py
statistics_calculator.py
session_analyzer.py
report_generator.py
export_manager.py
```

---

## Criterios de Aceptación

✔ Las estadísticas son precisas.

✔ Los resultados se actualizan en tiempo real.

✔ Las sesiones pueden almacenarse y recuperarse.

✔ El Dashboard muestra la información correctamente.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

El motor de estadísticas deberá diseñarse para admitir nuevas métricas en futuras versiones, como mapas de calor, análisis por zonas, tendencias históricas, recomendaciones personalizadas y un asistente de entrenamiento basado en Inteligencia Artificial.

---

## Dependencias de los Sprints 5–10

| Sprint    | Depende de      |
| --------- | --------------- |
| Sprint 5  | Sprint 4        |
| Sprint 6  | Sprint 5        |
| Sprint 7  | Sprint 5        |
| Sprint 8  | Sprint 5, 6 y 7 |
| Sprint 9  | Sprint 6, 7 y 8 |
| Sprint 10 | Sprint 9        |


# 15. Sprint 11 — Dashboard, HUD y Visualización de Estadísticas

## Estado

🟡 Pendiente

---

## Objetivo

Desarrollar un Dashboard moderno e interactivo que permita al jugador visualizar en tiempo real toda la información generada por el motor de Inteligencia Artificial.

---

## Descripción

Este Sprint transformará los datos técnicos del backend en una interfaz visual clara, atractiva y fácil de interpretar.

El Dashboard será uno de los componentes más importantes del proyecto, ya que representará el principal punto de interacción entre el jugador y el sistema durante una sesión de entrenamiento.

---

## Componentes a Crear

* DashboardManager
* HUDManager
* StatisticsPanel
* SessionSummary
* ProgressGraphs
* HeatMapViewer (preparación)

---

## Funcionalidades

* Mostrar tiros intentados.
* Mostrar tiros acertados.
* Mostrar porcentaje de efectividad.
* Mostrar tiempo de entrenamiento.
* Mostrar FPS (modo desarrollador).
* Mostrar estado de la IA.
* Mostrar historial de la sesión.

---

## Archivos Previstos

```text
presentation/godot/ui/

dashboard.tscn
dashboard.gd
hud.gd
statistics_panel.gd
session_summary.gd
graphs.gd
```

---

## Criterios de Aceptación

✔ Dashboard actualizado en tiempo real.

✔ Información sincronizada con Python.

✔ Diseño adaptable a distintas resoluciones.

✔ Navegación fluida.

✔ Interfaz intuitiva.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Diseñar el Dashboard de forma modular para facilitar la incorporación de nuevas métricas sin modificar la estructura principal.

---

# 16. Sprint 12 — Editor de Personajes y Personalización

## Estado

🟡 Pendiente

---

## Objetivo

Crear un sistema completo de personalización del jugador inspirado en videojuegos deportivos modernos.

---

## Descripción

El jugador podrá crear un avatar único modificando su apariencia física, ropa y accesorios.

Este sistema permitirá aumentar la inmersión y servirá como base para futuras funciones multijugador y progresión.

---

## Componentes a Crear

* CharacterEditor
* CharacterManager
* CustomizationSystem
* ClothingManager
* AppearanceManager

---

## Opciones de Personalización

* Nombre.
* Altura.
* Peso.
* Color de piel.
* Cabello.
* Barba.
* Rostro.
* Ojos.
* Uniforme.
* Tenis.
* Muñequeras.
* Rodilleras.
* Accesorios.

---

## Archivos Previstos

```text
presentation/godot/character/

character_editor.tscn
character_editor.gd
character_manager.gd
appearance_manager.gd
clothing_manager.gd
```

---

## Criterios de Aceptación

✔ El jugador puede crear un personaje.

✔ La apariencia se guarda correctamente.

✔ Los cambios persisten entre sesiones.

✔ Interfaz intuitiva.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Diseñar el sistema para permitir agregar nuevos elementos cosméticos sin modificar el editor existente.

---

# 17. Sprint 13 — Sistema de Perfiles, Progresión y Logros

## Estado

🟡 Pendiente

---

## Objetivo

Implementar un sistema de perfiles persistentes que almacene el progreso del jugador y registre sus logros.

---

## Descripción

Cada usuario dispondrá de un perfil propio donde se almacenarán sus estadísticas históricas, configuraciones, personajes y logros obtenidos.

Este sistema permitirá construir una experiencia de largo plazo.

---

## Componentes a Crear

* PlayerProfile
* ProfileManager
* AchievementSystem
* ProgressManager
* SaveManager

---

## Funcionalidades

* Crear perfiles.
* Editar perfiles.
* Guardar progreso.
* Historial de sesiones.
* Logros desbloqueados.
* Estadísticas históricas.
* Exportación de datos.

---

## Archivos Previstos

```text
src/application/profile/

profile_manager.py
achievement_system.py
progress_manager.py
save_manager.py
player_profile.py
```

---

## Criterios de Aceptación

✔ Los perfiles se crean correctamente.

✔ Las estadísticas persisten entre sesiones.

✔ Los logros se registran automáticamente.

✔ Compatible con futuras sincronizaciones en la nube.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Toda la información deberá almacenarse mediante repositorios para facilitar futuras migraciones a bases de datos.

---

# 18. Sprint 14 — Configuración, Accesibilidad y Experiencia de Usuario

## Estado

🟡 Pendiente

---

## Objetivo

Desarrollar un sistema completo de configuración que permita adaptar la aplicación a diferentes dispositivos y necesidades de los usuarios.

---

## Descripción

El objetivo es ofrecer una experiencia flexible y accesible, permitiendo personalizar aspectos visuales, técnicos y funcionales del sistema.

---

## Componentes a Crear

* SettingsManager
* AccessibilityManager
* ThemeManager
* LanguageManager
* CameraSettings

---

## Funcionalidades

* Selección de idioma.
* Cambio de resolución.
* Modo oscuro y claro.
* Configuración de cámara.
* Ajustes de rendimiento.
* Volumen.
* Escalado de interfaz.
* Atajos de teclado.

---

## Archivos Previstos

```text
presentation/godot/settings/

settings_manager.gd
theme_manager.gd
language_manager.gd
accessibility_manager.gd
camera_settings.gd
```

---

## Criterios de Aceptación

✔ Todas las configuraciones se guardan.

✔ La interfaz responde correctamente.

✔ Compatible con futuras plataformas.

✔ Configuración integrada con el backend.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

Toda nueva opción de configuración deberá añadirse mediante módulos independientes.

---

# 19. Sprint 15 — Optimización, Pruebas y Preparación para Beta

## Estado

🟡 Pendiente

---

## Objetivo

Optimizar el rendimiento general del sistema y preparar la primera versión Beta funcional.

---

## Descripción

Este Sprint estará dedicado a estabilizar el proyecto antes de la distribución a usuarios de prueba.

Se corregirán errores, se optimizará el rendimiento y se realizarán pruebas integrales del sistema.

---

## Componentes

* PerformanceAnalyzer
* BenchmarkSystem
* ErrorReporter
* TestingSuite

---

## Tareas

* Optimizar FPS.
* Reducir consumo de memoria.
* Optimizar inferencia de IA.
* Corregir errores.
* Ejecutar pruebas unitarias.
* Ejecutar pruebas de integración.
* Documentar incidencias.
* Preparar versión Beta.

---

## Archivos Previstos

```text
tests/

unit/
integration/
performance/

src/shared/

benchmark.py
performance_monitor.py
error_reporter.py
```

---

## Criterios de Aceptación

✔ El sistema mantiene un rendimiento estable.

✔ Todas las pruebas críticas son satisfactorias.

✔ No existen errores bloqueantes.

✔ La documentación está actualizada.

✔ La versión Beta está lista para distribución.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Antes de iniciar el siguiente Sprint deberán revisarse todos los resultados de las pruebas y actualizar el archivo CHANGELOG.md con las mejoras, correcciones y funcionalidades implementadas.

---

## Dependencias de los Sprints 11–15

| Sprint    | Depende de |
| --------- | ---------- |
| Sprint 11 | Sprint 10  |
| Sprint 12 | Sprint 11  |
| Sprint 13 | Sprint 12  |
| Sprint 14 | Sprint 13  |
| Sprint 15 | Sprint 14  |


# 20. Sprint 16 — Beta Pública y Retroalimentación

## Estado

🔵 Planificado

---

## Objetivo

Publicar la primera versión Beta de VJC Hoops AI para un grupo controlado de usuarios y recopilar información real sobre el funcionamiento del sistema.

---

## Descripción

Este Sprint marca la transición del desarrollo interno hacia las pruebas con usuarios reales.

El objetivo es validar el rendimiento del sistema, la precisión de la Inteligencia Artificial, la experiencia de usuario y detectar oportunidades de mejora antes del lanzamiento oficial.

---

## Objetivos Principales

* Publicar la versión Beta.
* Obtener retroalimentación.
* Detectar errores reales.
* Medir rendimiento en diferentes equipos.
* Analizar estabilidad del sistema.
* Priorizar mejoras.

---

## Funcionalidades

* Sistema de reporte de errores.
* Envío opcional de registros.
* Encuestas de satisfacción.
* Registro de incidencias.
* Actualizaciones Beta.

---

## Criterios de Aceptación

✔ La Beta funciona correctamente.

✔ Existe retroalimentación suficiente.

✔ Los errores críticos están documentados.

✔ Se genera un plan de mejoras.

---

## Tiempo Estimado

2 Sprints

---

## Notas para futuras IA

Toda observación recibida durante la Beta deberá registrarse y priorizarse antes del lanzamiento oficial.

---

# 21. Sprint 17 — Lanzamiento Oficial Versión 1.0

## Estado

🔵 Planificado

---

## Objetivo

Publicar la primera versión estable de VJC Hoops AI.

---

## Descripción

Este Sprint representa la culminación de la primera etapa del proyecto.

El sistema deberá ofrecer una experiencia estable, documentación completa y una arquitectura preparada para futuras ampliaciones.

---

## Funcionalidades Incluidas

* Dashboard completo.
* IA funcional.
* Detección de personas.
* Detección del balón.
* Detección del aro.
* Seguimiento de objetos.
* Detección automática de tiros.
* Estadísticas.
* Editor de personajes.
* Sistema de perfiles.
* Configuración.
* Accesibilidad.

---

## Entregables

* Instalador.
* Manual de usuario.
* Manual técnico.
* Documentación actualizada.
* Código estable.
* Release en GitHub.

---

## Criterios de Aceptación

✔ Todos los módulos funcionan.

✔ No existen errores críticos.

✔ Documentación completa.

✔ Publicación oficial realizada.

---

## Tiempo Estimado

1 Sprint

---

## Notas para futuras IA

La versión 1.0 será el punto de partida para futuras expansiones del proyecto.

---

# 22. Sprint 18 — IA Coach y Análisis Inteligente

## Estado

🟣 Visión Futura

---

## Objetivo

Incorporar un entrenador virtual basado en Inteligencia Artificial capaz de analizar el rendimiento del jugador y ofrecer recomendaciones personalizadas.

---

## Descripción

La IA Coach utilizará las estadísticas históricas para identificar patrones de juego, detectar áreas de mejora y proponer ejercicios específicos adaptados al usuario.

Este módulo convertirá VJC Hoops AI en una plataforma de entrenamiento inteligente.

---

## Funcionalidades

* Recomendaciones automáticas.
* Análisis de progreso.
* Comparación entre sesiones.
* Objetivos personalizados.
* Predicción de rendimiento.
* Generación de rutinas.

---

## Componentes Futuros

* CoachEngine
* RecommendationSystem
* TrainingPlanner
* PerformancePredictor

---

## Criterios de Éxito

✔ Recomendaciones útiles.

✔ Aprendizaje continuo.

✔ Personalización por jugador.

✔ Integración con el motor de estadísticas.

---

## Tiempo Estimado

3 Sprints

---

## Notas para futuras IA

El Coach deberá mantenerse desacoplado del resto del sistema para facilitar la incorporación de nuevos modelos de IA.

---

# 23. Sprint 19 — Sincronización en la Nube y Plataforma Online

## Estado

🟣 Visión Futura

---

## Objetivo

Permitir que los usuarios puedan acceder a sus estadísticas desde cualquier dispositivo mediante sincronización en la nube.

---

## Descripción

Este Sprint transformará VJC Hoops AI en una plataforma conectada.

Los jugadores podrán iniciar sesión, sincronizar su progreso y compartir estadísticas entre diferentes dispositivos.

---

## Funcionalidades

* Cuentas de usuario.
* Inicio de sesión.
* Sincronización automática.
* Copias de seguridad.
* Compartir estadísticas.
* Ranking global.
* Perfiles públicos.

---

## Tecnologías Previstas

* FastAPI.
* PostgreSQL.
* JWT.
* WebSockets.
* Servicios en la nube.

---

## Criterios de Éxito

✔ Sincronización estable.

✔ Datos seguros.

✔ Acceso multiplataforma.

✔ Baja latencia.

---

## Tiempo Estimado

4 Sprints

---

## Notas para futuras IA

Diseñar todos los servicios siguiendo una arquitectura orientada a APIs para facilitar futuras integraciones.

---

# 24. Sprint 20 — Evolución hacia VJC Hoops AI 2.0

## Estado

🟣 Visión Estratégica

---

## Objetivo

Definir la evolución del proyecto más allá de la versión 1.0, ampliando sus capacidades mediante nuevos módulos, tecnologías y disciplinas deportivas.

---

## Descripción

La versión 2.0 no será una simple actualización.

Representará una nueva etapa del proyecto con funcionalidades avanzadas, mayor personalización y un ecosistema preparado para crecer durante muchos años.

---

## Líneas de Evolución

### Inteligencia Artificial

* Modelos personalizados.
* Aprendizaje continuo.
* Predicción de rendimiento.
* Detección avanzada de movimientos.

### Nuevos Deportes

* Fútbol.
* Voleibol.
* Tenis.
* Béisbol.
* Pádel.

### Nuevas Plataformas

* Android.
* iOS.
* Web.
* Linux.
* macOS.

### Funcionalidades Sociales

* Amigos.
* Equipos.
* Retos.
* Torneos.
* Compartir estadísticas.

### Analítica Avanzada

* Mapas de calor.
* Comparación histórica.
* Reportes automáticos.
* Paneles interactivos.

---

## Visión a Largo Plazo

VJC Hoops AI aspira a convertirse en una plataforma modular de análisis deportivo impulsada por Inteligencia Artificial.

Su arquitectura permitirá incorporar nuevos deportes, nuevos algoritmos y nuevas experiencias sin comprometer la estabilidad del sistema.

Cada nueva versión deberá construirse respetando los principios definidos en:

* README.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md

---

# Conclusión

Este ROADMAP constituye la planificación oficial de VJC Hoops AI.

Cada Sprint describe una etapa concreta del desarrollo y proporciona una guía clara para desarrolladores e Inteligencias Artificiales.

El objetivo de esta hoja de ruta no es únicamente organizar tareas, sino establecer una estrategia sostenible que permita construir una plataforma profesional, escalable y preparada para evolucionar durante muchos años.

Toda modificación futura deberá respetar la arquitectura, la documentación y los principios definidos en este repositorio para garantizar la continuidad y la calidad del proyecto.
