# CONTRIBUTING.md

# Guía Oficial de Contribución

Bienvenido a **VJC Hoops AI**.

Este documento define las normas, recomendaciones y procedimientos oficiales para contribuir al proyecto.

Su objetivo es garantizar que todo el código, la documentación y las futuras funcionalidades mantengan un nivel de calidad uniforme, independientemente de si son desarrolladas por personas o por Inteligencias Artificiales.

Toda contribución deberá respetar las reglas descritas en este documento.

---

# Índice

1. Filosofía del proyecto
2. Requisitos del entorno de desarrollo
3. Instalación del proyecto
4. Configuración de las herramientas
5. Primer inicio del proyecto
6. Organización del repositorio
7. Convenciones de nombres
8. Estándares de programación
9. Arquitectura obligatoria
10. Flujo de trabajo con Git
11. Convenciones de commits
12. Uso de ramas
13. Pull Requests
14. Documentación
15. Pruebas
16. Checklist antes de un Commit
17. Checklist antes de un Pull Request
18. Reglas para Inteligencias Artificiales
19. Código de conducta
20. Conclusión

---

# 1. Filosofía del Proyecto

## 1.1 Objetivo

VJC Hoops AI busca convertirse en una plataforma profesional de entrenamiento deportivo basada en Inteligencia Artificial.

El proyecto combina visión por computadora, análisis de datos y una interfaz desarrollada con Godot para ofrecer una herramienta moderna, escalable y fácil de mantener.

Cada decisión técnica deberá favorecer la calidad del software a largo plazo.

---

## 1.2 Principios Fundamentales

Todo el desarrollo deberá seguir los siguientes principios.

* Código claro y legible.
* Arquitectura modular.
* Bajo acoplamiento entre componentes.
* Alta cohesión.
* Documentación actualizada.
* Escalabilidad.
* Reutilización del código.
* Facilidad para realizar pruebas.
* Mantenibilidad.

La prioridad siempre será construir un sistema sólido antes que desarrollar funcionalidades rápidamente.

---

## 1.3 Colaboración

Este proyecto está diseñado para que puedan colaborar tanto desarrolladores como Inteligencias Artificiales.

Por esta razón, toda modificación deberá ser fácil de comprender, documentar y mantener.

No deberán realizarse cambios que dificulten la continuidad del desarrollo.

---

# 2. Requisitos del Entorno de Desarrollo

Antes de comenzar cualquier contribución será necesario disponer del siguiente entorno de trabajo.

---

## Software Requerido

* Python 3.x
* Godot Engine 4.x
* Git
* Visual Studio Code
* GitHub Desktop (opcional)

---

## Conocimientos Recomendados

Es recomendable tener conocimientos básicos sobre.

* Python.
* Programación orientada a objetos.
* Arquitectura Hexagonal.
* Git.
* GDScript.
* Visión por computadora.
* Inteligencia Artificial.

No es obligatorio dominar todas estas tecnologías, ya que la documentación del proyecto servirá como guía.

---

## Documentación Obligatoria

Antes de comenzar cualquier desarrollo deberán leerse los siguientes documentos.

* README.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md

Estos documentos constituyen la referencia oficial del proyecto.

---

# 3. Instalación del Proyecto

## Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/vjc-hoops-ai.git
```

---

## Acceder al Proyecto

```bash
cd vjc-hoops-ai
```

---

## Crear un Entorno Virtual

### Windows

```bash
python -m venv .venv
```

### Linux / macOS

```bash
python3 -m venv .venv
```

---

## Activar el Entorno Virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Instalar Dependencias

Cuando el archivo `requirements.txt` esté disponible.

```bash
pip install -r requirements.txt
```

---

## Verificar la Instalación

Comprobar que Python está correctamente instalado.

```bash
python --version
```

Comprobar que Git está disponible.

```bash
git --version
```

Verificar que Godot Engine puede abrir el proyecto correctamente.

---

# 4. Configuración de las Herramientas

## Visual Studio Code

Se recomienda utilizar Visual Studio Code como entorno principal de desarrollo.

Extensiones sugeridas.

* Python
* Pylance
* GitLens
* Markdown All in One
* Error Lens
* Even Better TOML
* YAML
* EditorConfig

Estas extensiones mejoran la productividad y facilitan el mantenimiento del proyecto.

---

## Python

Todas las dependencias deberán instalarse dentro del entorno virtual del proyecto.

No deberán utilizarse instalaciones globales para el desarrollo diario.

---

## Godot

El proyecto utilizará Godot Engine 4.x como cliente gráfico.

Se recomienda utilizar la misma versión del motor definida por el equipo para evitar incompatibilidades.

---

## Git

Antes de realizar cualquier cambio deberá comprobarse que el repositorio está actualizado.

```bash
git pull
```

De esta forma se reducen conflictos y se mantiene un historial limpio.

---

# 5. Primer Inicio del Proyecto

Una vez configurado el entorno de desarrollo, el primer paso será comprobar que todos los componentes funcionan correctamente.

---

## Verificaciones Iniciales

Antes de comenzar a programar deberá comprobarse que:

* El repositorio se clonó correctamente.
* El entorno virtual está activo.
* Las dependencias están instaladas.
* Git funciona correctamente.
* Godot abre el proyecto sin errores.
* Python reconoce todas las librerías necesarias.

---

## Estructura Esperada

El directorio principal deberá contener una estructura similar a la siguiente.

```text
vjc-hoops-ai/

README.md
README_EN.md
PROJECT_CONTEXT.md
PROJECT_ARCHITECTURE.md
ROADMAP.md
CHANGELOG.md
CONTRIBUTING.md

src/
assets/
models/
data/
config/
docs/
tests/
logs/
```

La estructura podrá ampliarse con nuevas carpetas conforme evolucione el proyecto, pero deberá mantenerse organizada y documentada.

---

## Primer Objetivo

Antes de desarrollar nuevas funcionalidades, cualquier colaborador deberá comprender la arquitectura, revisar la documentación existente y verificar que el entorno funciona correctamente.

Solo después de completar estas verificaciones se deberá comenzar a trabajar en nuevas tareas definidas dentro del `ROADMAP.md`.


# 6. Organización del Repositorio

## 6.1 Objetivo

La organización del repositorio tiene como finalidad mantener una estructura clara, escalable y fácil de comprender.

Cada carpeta deberá tener una única responsabilidad.

Nunca deberán mezclarse archivos de distintas capas dentro del mismo directorio.

---

## 6.2 Estructura Principal

La estructura oficial del proyecto será la siguiente.

```text
vjc-hoops-ai/

README.md
README_EN.md
PROJECT_CONTEXT.md
PROJECT_ARCHITECTURE.md
ROADMAP.md
CHANGELOG.md
CONTRIBUTING.md

src/

application/
domain/
infrastructure/
presentation/
shared/

assets/
config/
models/
data/
docs/
logs/
tests/
```

---

## 6.3 Responsabilidad de Cada Carpeta

### src/domain

Contendrá únicamente la lógica de negocio.

Ejemplos.

* Entidades
* Interfaces
* Objetos de Valor
* Reglas del negocio

Nunca deberá depender de OpenCV, Godot o cualquier otra librería externa.

---

### src/application

Contendrá los casos de uso del sistema.

Ejemplos.

* Iniciar entrenamiento.
* Finalizar sesión.
* Calcular estadísticas.
* Crear perfil.

---

### src/infrastructure

Contendrá todas las dependencias externas.

Ejemplos.

* OpenCV
* YOLO
* Cámara
* Archivos JSON
* Bases de datos
* APIs

---

### src/presentation

Contendrá la interfaz gráfica desarrollada con Godot.

---

### src/shared

Contendrá código reutilizable.

Ejemplos.

* Utilidades.
* Configuración.
* Constantes.
* Logger.
* Excepciones.

---

## 6.4 Reglas

No crear carpetas nuevas sin una justificación clara.

No duplicar código.

Mantener responsabilidades separadas.

Toda nueva carpeta deberá documentarse.

---

# 7. Convenciones de Nombres

## 7.1 Objetivo

Mantener una nomenclatura uniforme facilita la lectura del código y reduce errores durante el desarrollo.

Todas las contribuciones deberán respetar estas convenciones.

---

## 7.2 Python

### Archivos

Siempre utilizar.

```text
snake_case.py
```

Ejemplos.

```text
camera_service.py

statistics_engine.py

shot_detector.py
```

---

### Clases

Utilizar.

```text
PascalCase
```

Ejemplos.

```python
CameraService

StatisticsEngine

ShotDetector

PlayerProfile
```

---

### Funciones

Utilizar.

```python
snake_case
```

Ejemplos.

```python
calculate_statistics()

load_model()

detect_ball()
```

---

### Variables

```python
snake_case
```

Ejemplos.

```python
ball_position

current_session

total_shots
```

---

### Constantes

```python
UPPER_CASE
```

Ejemplos.

```python
MAX_FPS

DEFAULT_CAMERA

WINDOW_WIDTH
```

---

### Clases Abstractas

Siempre comenzar con la letra I.

Ejemplo.

```python
ICamera

IDetector

IRepository
```

---

## 7.3 GDScript

Seguir exactamente las mismas convenciones que Python.

El objetivo es mantener consistencia entre ambos lenguajes.

---

## 7.4 Archivos Godot

Escenas.

```text
training_scene.tscn

dashboard_scene.tscn
```

Scripts.

```text
training_scene.gd

dashboard_scene.gd
```

---

# 8. Estándares de Programación

## 8.1 Principios

Todo el código deberá priorizar.

* Legibilidad.
* Simplicidad.
* Modularidad.
* Reutilización.
* Facilidad para pruebas.

---

## 8.2 Funciones

Cada función deberá realizar una única responsabilidad.

Evitar funciones excesivamente largas.

Como referencia general:

* Ideal: menos de 30 líneas.
* Máximo recomendado: 60 líneas.

Si una función supera este límite, deberá evaluarse dividirla en funciones más pequeñas.

---

## 8.3 Clases

Cada clase deberá representar una única responsabilidad.

Evitar clases que concentren demasiada lógica.

---

## 8.4 Comentarios

No comentar código evidente.

Comentar únicamente decisiones importantes.

Ejemplo.

Correcto.

```python
# Convertimos las coordenadas al sistema utilizado por Godot.
```

Incorrecto.

```python
# Sumamos uno.
x = x + 1
```

---

## 8.5 Tipado

Siempre que sea posible utilizar type hints.

Ejemplo.

```python
def calculate_score(total_shots: int, successful_shots: int) -> float:
    ...
```

---

## 8.6 Docstrings

Las funciones públicas deberán incluir documentación.

Ejemplo.

```python
def detect_ball(frame):
    """
    Detecta el balón dentro del frame recibido.

    Args:
        frame: Imagen capturada por la cámara.

    Returns:
        Información de la detección.
    """
```

---

# 9. Arquitectura Obligatoria

## 9.1 Arquitectura Oficial

Todo el proyecto seguirá la Arquitectura Hexagonal.

No deberán implementarse accesos directos entre capas.

---

## 9.2 Flujo Permitido

```text
Presentation

↓

Application

↓

Domain

↑

Infrastructure
```

---

## 9.3 Dependencias

La lógica del dominio nunca deberá depender de.

* OpenCV.
* Godot.
* YOLO.
* Bases de datos.
* APIs.
* Sistemas operativos.

Todas esas dependencias deberán permanecer dentro de Infrastructure.

---

## 9.4 Nuevos Módulos

Cada nueva funcionalidad deberá incorporarse mediante nuevos módulos.

Evitar modificar componentes existentes cuando sea posible.

Esto reducirá el riesgo de introducir errores en funcionalidades ya implementadas.

---

## 9.5 Revisión Arquitectónica

Antes de fusionar cambios importantes deberá comprobarse que la Arquitectura Hexagonal continúa respetándose.

---

# 10. Flujo de Trabajo con Git

## 10.1 Objetivo

Mantener un historial de cambios claro, limpio y fácil de seguir.

---

## 10.2 Antes de Comenzar

Siempre actualizar el repositorio.

```bash
git pull
```

---

## 10.3 Durante el Desarrollo

Realizar commits pequeños y frecuentes.

Cada commit deberá representar un único cambio lógico.

Evitar commits excesivamente grandes.

---

## 10.4 Sincronización

Después de completar una tarea.

```bash
git add .

git commit -m "mensaje"

git push
```

---

## 10.5 Frecuencia

Se recomienda realizar un commit al finalizar cada funcionalidad importante.

No esperar varios días para guardar cambios.

---

## 10.6 Revisión

Antes de realizar un commit comprobar.

* El proyecto compila.
* No existen errores evidentes.
* La documentación está actualizada.
* CHANGELOG.md refleja los cambios importantes.

---

## 10.7 Objetivo Final

El historial de Git deberá permitir comprender la evolución completa del proyecto sin necesidad de consultar conversaciones, notas externas o información adicional.

Cada commit deberá representar un avance claro, verificable y bien documentado.


# 11. Convenciones de Commits

## 11.1 Objetivo

Los mensajes de commit deberán ser claros, consistentes y descriptivos.

El historial de Git debe permitir comprender rápidamente qué cambios se realizaron sin necesidad de inspeccionar el código.

---

## 11.2 Formato Oficial

Todos los commits deberán seguir la siguiente estructura.

```text
tipo: descripción breve
```

Ejemplos.

```text
feat: agregar detector de balón

fix: corregir cálculo del porcentaje de aciertos

docs: actualizar ROADMAP

refactor: reorganizar StatisticsEngine

style: mejorar formato del código

test: agregar pruebas para ShotDetector

perf: optimizar procesamiento de frames

chore: actualizar dependencias
```

---

## 11.3 Tipos Permitidos

| Tipo     | Descripción                                |
| -------- | ------------------------------------------ |
| feat     | Nueva funcionalidad                        |
| fix      | Corrección de errores                      |
| docs     | Documentación                              |
| refactor | Reestructuración del código                |
| style    | Cambios de formato sin modificar la lógica |
| test     | Nuevas pruebas o actualización de pruebas  |
| perf     | Mejoras de rendimiento                     |
| chore    | Tareas de mantenimiento                    |

---

## 11.4 Reglas

* Utilizar mensajes cortos y descriptivos.
* Escribir en infinitivo.
* No utilizar mensajes genéricos como "Cambios", "Update" o "Correcciones".
* Un commit debe representar un único cambio lógico.

---

## 11.5 Ejemplos Incorrectos

```text
update

cambios

hola

arreglos

nuevo
```

---

## 11.6 Ejemplos Correctos

```text
feat: implementar Dashboard inicial

fix: corregir error al abrir la cámara

docs: ampliar PROJECT_ARCHITECTURE

perf: reducir consumo de memoria del tracker
```

---

# 12. Uso de Ramas

## 12.1 Objetivo

El desarrollo deberá realizarse mediante ramas para mantener la estabilidad de la rama principal.

La rama `main` deberá contener únicamente versiones funcionales y estables.

---

## 12.2 Rama Principal

```text
main
```

Esta rama representará siempre la versión oficial del proyecto.

No deberá utilizarse para desarrollar funcionalidades nuevas.

---

## 12.3 Ramas de Desarrollo

Utilizar la siguiente nomenclatura.

```text
feature/nombre-funcionalidad

bugfix/nombre-error

hotfix/nombre-problema

docs/nombre-documento

refactor/nombre-modulo

test/nombre-prueba
```

---

## 12.4 Ejemplos

```text
feature/person-detector

feature/dashboard-ui

feature/character-editor

bugfix/camera-crash

docs/project-context

refactor/statistics-engine

test/person-detector
```

---

## 12.5 Flujo Recomendado

```text
main

↓

feature/dashboard

↓

Commits

↓

Pruebas

↓

Merge

↓

main
```

---

## 12.6 Reglas

* No trabajar directamente sobre `main`.
* Mantener las ramas pequeñas.
* Eliminar ramas cuando ya no sean necesarias.
* Mantener sincronizada la rama principal.

---

# 13. Pull Requests

## 13.1 Objetivo

Todo cambio importante deberá revisarse antes de integrarse en la rama principal.

Aunque inicialmente el proyecto sea desarrollado por una sola persona, este procedimiento facilitará futuras colaboraciones.

---

## 13.2 Contenido del Pull Request

Cada Pull Request deberá incluir.

* Objetivo del cambio.
* Descripción de la implementación.
* Archivos modificados.
* Riesgos conocidos.
* Capturas de pantalla cuando existan cambios visuales.
* Relación con el Sprint correspondiente.

---

## 13.3 Revisión

Antes de aprobar un Pull Request deberá comprobarse que.

* El código compila.
* No existen errores evidentes.
* Se respetan las convenciones del proyecto.
* La documentación fue actualizada.
* CHANGELOG.md refleja los cambios importantes.

---

## 13.4 Integración

Una vez aprobado.

* Fusionar la rama.
* Eliminar la rama de trabajo.
* Actualizar ROADMAP si corresponde.

---

# 14. Documentación

## 14.1 Importancia

La documentación forma parte del proyecto y deberá mantenerse al mismo nivel de calidad que el código fuente.

Un módulo sin documentación se considerará incompleto.

---

## 14.2 Documentos Oficiales

Toda modificación importante podrá requerir actualizar uno o varios de los siguientes archivos.

* README.md
* README_EN.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md
* CONTRIBUTING.md

---

## 14.3 Cuándo Actualizar

Actualizar la documentación cuando.

* Se agregue una funcionalidad importante.
* Cambie la arquitectura.
* Se modifique el flujo del sistema.
* Se incorporen nuevas dependencias.
* Se publiquen nuevas versiones.

---

## 14.4 Calidad

La documentación deberá ser.

* Clara.
* Precisa.
* Actualizada.
* Fácil de comprender.
* Coherente con el código.

---

## 14.5 Objetivo

Toda persona o Inteligencia Artificial deberá poder comprender el estado del proyecto únicamente leyendo la documentación oficial.

---

# 15. Pruebas

## 15.1 Objetivo

Todo componente importante deberá ser probado antes de integrarse al proyecto.

Las pruebas permitirán garantizar la estabilidad del sistema y reducir la aparición de errores.

---

## 15.2 Tipos de Pruebas

El proyecto utilizará varios niveles de pruebas.

### Pruebas Unitarias

Validan funciones o clases individuales.

Ejemplos.

* StatisticsEngine
* ShotDetector
* CameraService

---

### Pruebas de Integración

Verifican la comunicación entre distintos módulos.

Ejemplos.

* Python ↔ Godot.
* YOLO ↔ Tracker.
* Tracker ↔ StatisticsEngine.

---

### Pruebas Funcionales

Comprueban que una funcionalidad completa opera correctamente.

Ejemplos.

* Entrenamiento completo.
* Registro de estadísticas.
* Creación de perfiles.

---

### Pruebas de Rendimiento

Evalúan.

* FPS.
* Uso de CPU.
* Uso de GPU.
* Memoria.
* Tiempo de inferencia.

---

## 15.3 Automatización

Siempre que sea posible las pruebas deberán ejecutarse automáticamente antes de publicar nuevas versiones.

---

## 15.4 Cobertura

Como objetivo inicial, los módulos principales deberán alcanzar una cobertura mínima del 80%.

Las funcionalidades críticas deberán acercarse al 100%.

---

## 15.5 Criterios de Aceptación

Antes de considerar finalizada una tarea deberá comprobarse que.

* Las pruebas unitarias son satisfactorias.
* Las pruebas de integración no presentan errores.
* No existen regresiones conocidas.
* El rendimiento se mantiene dentro de los objetivos establecidos.
* La documentación refleja el comportamiento actual del sistema.


# 16. Checklist Antes de Realizar un Commit

Antes de realizar cualquier commit, el desarrollador o la Inteligencia Artificial deberá verificar que el proyecto se encuentra en un estado consistente.

---

## Lista de Verificación

Antes de ejecutar `git commit`, comprobar lo siguiente.

### Código

* El código compila correctamente.
* No existen errores de sintaxis.
* No existen advertencias críticas.
* No hay código comentado innecesario.
* No existen archivos temporales.
* No existen dependencias innecesarias.

---

### Arquitectura

* Se respeta la Arquitectura Hexagonal.
* No se rompieron dependencias entre capas.
* Cada módulo mantiene una única responsabilidad.
* No existe código duplicado.

---

### Calidad

* El código es legible.
* Se utilizaron nombres descriptivos.
* Las funciones son pequeñas y reutilizables.
* Se añadieron comentarios únicamente cuando son necesarios.

---

### Documentación

Comprobar si es necesario actualizar alguno de los siguientes archivos.

* README.md
* README_EN.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md
* CONTRIBUTING.md

---

### Pruebas

* Las pruebas unitarias son satisfactorias.
* No existen errores conocidos relacionados con el cambio.
* El rendimiento no se ha degradado.

---

# 17. Checklist Antes de Crear un Pull Request

Antes de solicitar la integración de una rama deberán realizarse las siguientes verificaciones.

---

## Código

* Todos los commits son claros y descriptivos.
* No existen archivos innecesarios.
* No existen conflictos pendientes.
* El proyecto continúa funcionando correctamente.

---

## Documentación

* La documentación refleja el estado actual del proyecto.
* CHANGELOG.md fue actualizado cuando corresponde.
* El Sprint relacionado se encuentra correctamente documentado.

---

## Calidad

* Se respetan todas las convenciones del proyecto.
* No existen cambios experimentales sin justificar.
* La implementación mantiene la arquitectura establecida.

---

## Revisión

Antes de aprobar un Pull Request deberá comprobarse.

* El código fue revisado.
* La funcionalidad fue probada.
* No existen regresiones.
* El objetivo del cambio se cumplió completamente.

---

# 18. Reglas para Inteligencias Artificiales

## Objetivo

Este proyecto ha sido diseñado para que pueda desarrollarse con la colaboración de diferentes modelos de Inteligencia Artificial.

Con el fin de mantener la coherencia del proyecto, toda IA deberá respetar las siguientes normas.

---

## Continuidad

Antes de generar código, la IA deberá revisar la documentación oficial del proyecto.

En especial.

* README.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md
* CONTRIBUTING.md

Ninguna implementación deberá contradecir estos documentos.

---

## Arquitectura

La IA no deberá modificar la arquitectura principal salvo que exista una justificación técnica sólida y dicha modificación quede documentada.

---

## Calidad

Toda generación de código deberá priorizar.

* Claridad.
* Modularidad.
* Escalabilidad.
* Reutilización.
* Bajo acoplamiento.
* Alta cohesión.

---

## Documentación

Siempre que una IA implemente una funcionalidad importante deberá indicar si es necesario actualizar la documentación oficial del proyecto.

---

## Cambios Importantes

Si una IA detecta una mejora arquitectónica significativa deberá proponerla antes de modificar el diseño existente.

---

## Filosofía

Las Inteligencias Artificiales no deberán limitarse a escribir código.

También deberán contribuir proponiendo mejoras de arquitectura, optimizaciones, estrategias de pruebas y recomendaciones técnicas cuando aporten valor al proyecto.

---

# 19. Código de Conducta Técnico

## Respeto por la Arquitectura

Toda decisión técnica deberá respetar la arquitectura oficial del proyecto.

Las soluciones rápidas que comprometan la mantenibilidad deberán evitarse.

---

## Calidad sobre Velocidad

La prioridad será desarrollar software de calidad.

Nunca deberá sacrificarse la estabilidad del sistema por implementar una funcionalidad más rápido.

---

## Simplicidad

Cuando existan varias soluciones válidas, se preferirá aquella que sea más sencilla de comprender y mantener.

---

## Escalabilidad

Todo nuevo componente deberá diseñarse pensando en el crecimiento futuro del proyecto.

---

## Colaboración

Las decisiones deberán favorecer la colaboración entre desarrolladores humanos e Inteligencias Artificiales.

---

## Aprendizaje Continuo

El proyecto deberá evolucionar incorporando buenas prácticas, nuevas tecnologías y mejoras arquitectónicas siempre que aporten beneficios reales.

---

# 20. Conclusión

Este documento establece las normas oficiales para contribuir a **VJC Hoops AI**.

Su propósito es garantizar que el proyecto conserve una arquitectura consistente, un estilo de programación uniforme y una documentación actualizada, independientemente del número de colaboradores o de las herramientas utilizadas durante su desarrollo.

Toda contribución deberá respetar los principios definidos en este documento, así como en el resto de la documentación oficial del proyecto.

El éxito de VJC Hoops AI dependerá no solo de la calidad del código, sino también de la disciplina con la que se mantengan sus estándares de desarrollo.

---

# Documentación Oficial del Proyecto

La documentación oficial está compuesta por los siguientes archivos.

* README.md
* README_EN.md
* PROJECT_CONTEXT.md
* PROJECT_ARCHITECTURE.md
* ROADMAP.md
* CHANGELOG.md
* CONTRIBUTING.md

Estos documentos constituyen la referencia principal para comprender, desarrollar y mantener el proyecto.

Cualquier modificación relevante deberá reflejarse en ellos cuando corresponda.

---

# Declaración Final

VJC Hoops AI aspira a convertirse en una plataforma profesional de entrenamiento deportivo impulsada por Inteligencia Artificial.

Este objetivo solo podrá alcanzarse manteniendo una arquitectura sólida, una documentación de alta calidad y un proceso de desarrollo disciplinado.

Cada línea de código, cada documento y cada decisión técnica deberán contribuir a construir un proyecto escalable, mantenible y preparado para evolucionar durante muchos años.
