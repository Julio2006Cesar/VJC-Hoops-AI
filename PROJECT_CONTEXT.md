# 📘 PROJECT_CONTEXT.md

# VJC Hoops AI

**Versión del documento:** 1.0

**Estado:** En desarrollo

**Última actualización:** Junio 2026

---

# 0. Información del Documento

## Propósito

Este documento es la fuente principal de información del proyecto **VJC Hoops AI**.

Su objetivo es documentar la visión, la arquitectura, las decisiones de diseño, la estructura del código, el flujo de trabajo, los componentes existentes y los planes futuros del proyecto.

Está pensado para que cualquier desarrollador o cualquier modelo de Inteligencia Artificial pueda comprender rápidamente cómo funciona el sistema y continuar su desarrollo respetando la arquitectura y las decisiones ya tomadas.

Este documento evoluciona junto con el proyecto. Cada Sprint importante debe reflejarse aquí para mantener la documentación sincronizada con el código.

---

## Alcance

Este documento describe tanto la parte de Inteligencia Artificial como la parte del videojuego.

Incluye:

- Arquitectura del software.
- Arquitectura de la IA.
- Arquitectura del cliente desarrollado con Godot.
- Flujo de procesamiento de datos.
- Organización del repositorio.
- Estado actual del proyecto.
- Objetivos.
- Convenciones de desarrollo.
- Guías para futuras IA.
- Roadmap general.

La documentación detallada de módulos específicos podrá encontrarse en la carpeta `docs/`, pero este documento servirá como punto de entrada principal.

---

## Audiencia

Este documento está dirigido a:

- El creador del proyecto.
- Colaboradores.
- Desarrolladores.
- Modelos de Inteligencia Artificial.
- Futuros mantenedores del proyecto.

---

# 1. Visión General del Proyecto

## ¿Qué es VJC Hoops AI?

VJC Hoops AI es una plataforma de entrenamiento de baloncesto asistida por Inteligencia Artificial cuyo objetivo es ayudar a jugadores de todos los niveles a mejorar su técnica mediante análisis automático de vídeo.

El proyecto combina Visión por Computadora, Aprendizaje Profundo y una interfaz interactiva desarrollada con Godot para ofrecer una experiencia que une análisis técnico y elementos propios de un videojuego.

La plataforma no pretende sustituir a un entrenador, sino proporcionar una herramienta de apoyo que ofrezca información objetiva y fácil de interpretar.

---

## Visión a largo plazo

La visión del proyecto es convertirse en una plataforma modular que permita:

- Analizar entrenamientos individuales.
- Medir la evolución del jugador.
- Detectar patrones de movimiento.
- Evaluar la mecánica del lanzamiento.
- Calcular estadísticas automáticamente.
- Presentar la información mediante una interfaz moderna e intuitiva.
- Incorporar elementos de progresión y motivación inspirados en videojuegos.

En el futuro, la plataforma podrá ampliarse con nuevos módulos sin necesidad de rediseñar toda la arquitectura.

---

## Componentes principales

El proyecto está compuesto por dos grandes sistemas independientes pero conectados.

### Motor de Inteligencia Artificial

Desarrollado en Python.

Responsable de:

- Captura de vídeo.
- Detección de personas.
- Seguimiento de jugadores.
- Detección del balón.
- Estimación de pose.
- Reconocimiento de tiros.
- Cálculo de estadísticas.

### Cliente del juego

Desarrollado con Godot 4.

Responsable de:

- Pantalla de inicio.
- Navegación.
- Dashboard.
- Editor de personajes.
- Perfil del jugador.
- Configuración.
- Visualización de resultados.
- Experiencia de usuario.

La comunicación entre ambos sistemas permitirá mantener separadas las responsabilidades y facilitar futuras ampliaciones.

---

# 2. Filosofía del Proyecto

## 2.1 Introducción

Antes de escribir cualquier línea de código es importante comprender que VJC Hoops AI no es únicamente un proyecto de Visión por Computadora ni únicamente un videojuego.

Es una plataforma completa que combina Inteligencia Artificial, análisis deportivo y una experiencia interactiva desarrollada mediante un motor de videojuegos.

Por este motivo, todas las decisiones técnicas deberán tomarse pensando en la escalabilidad del sistema y no únicamente en resolver un problema inmediato.

La filosofía del proyecto define los principios que deberán mantenerse durante todo el desarrollo.

Estas reglas deberán respetarse independientemente del lenguaje de programación utilizado, de la Inteligencia Artificial que participe en el desarrollo o de las nuevas tecnologías que puedan incorporarse en el futuro.

---

# 2.2 Objetivo Principal

El objetivo principal del proyecto es construir una plataforma inteligente capaz de analizar automáticamente la técnica de lanzamiento de un jugador de baloncesto utilizando Inteligencia Artificial.

El sistema deberá proporcionar información clara, útil y fácil de interpretar para ayudar al jugador a mejorar su rendimiento.

El videojuego no reemplaza al sistema de IA.

La IA no reemplaza al videojuego.

Ambos componentes trabajan juntos formando un único producto.

---

# 2.3 Filosofía de Desarrollo

Todo el desarrollo seguirá los siguientes principios.

## Modularidad

Cada componente deberá tener una única responsabilidad.

No deberán existir clases que realicen múltiples tareas diferentes.

Por ejemplo:

Correcto:

CameraService
↓
PersonDetector
↓
ObjectTracker
↓
ShotDetector
↓
StatisticsEngine

Incorrecto:

Una única clase que abra la cámara, detecte personas, calcule estadísticas, dibuje resultados y almacene información.

Cada módulo debe poder sustituirse sin afectar al resto del sistema.

---

## Escalabilidad

El proyecto está diseñado para crecer durante muchos años.

Por esta razón nunca deberán implementarse soluciones que únicamente funcionen para el estado actual del proyecto.

Cada nuevo módulo deberá permitir futuras ampliaciones.

Ejemplo:

Hoy únicamente existe un detector de personas.

Mañana podrán existir:

- Detector de balón.
- Detector de aro.
- Detector de líneas de la cancha.
- Detector de entrenador.
- Detector de obstáculos.

La arquitectura deberá permitir incorporar estos módulos sin modificar los anteriores.

---

## Independencia Tecnológica

La lógica del negocio nunca dependerá directamente de una tecnología específica.

Ejemplos:

La capa Domain no deberá conocer OpenCV.

La capa Domain no deberá conocer YOLO.

La capa Domain no deberá conocer Godot.

La capa Domain únicamente conocerá conceptos del negocio.

Ejemplo:

Jugador

Tiro

Entrenamiento

Estadística

Sesión

Intento

Resultado

---

## Arquitectura Limpia

El proyecto seguirá los principios de Clean Architecture.

Las dependencias siempre deberán apuntar hacia el dominio.

Nunca al revés.

```text
Presentación

↓

Infraestructura

↓

Aplicación

↓

Dominio
```

El dominio será completamente independiente.

---

## Bajo Acoplamiento

Los módulos deberán comunicarse mediante interfaces claras.

Nunca deberán acceder directamente al estado interno de otros componentes.

Cada módulo únicamente conocerá lo necesario para realizar su trabajo.

---

## Alta Cohesión

Cada archivo deberá resolver un único problema.

Ejemplos:

PersonDetector

Únicamente detecta personas.

ObjectTracker

Únicamente mantiene IDs persistentes.

StatisticsEngine

Únicamente calcula estadísticas.

ShotDetector

Únicamente detecta tiros.

No deberán mezclarse responsabilidades.

---

# 2.4 Filosofía del Motor de IA

El motor de Inteligencia Artificial será un servicio independiente.

No contendrá elementos gráficos.

No mostrará menús.

No administrará interfaces.

Su única responsabilidad será procesar información y devolver resultados.

El motor deberá ser reutilizable incluso si en el futuro se reemplaza Godot por otro motor gráfico.

---

# 2.5 Filosofía del Cliente Godot

Godot será únicamente el cliente visual.

Su responsabilidad será:

- Mostrar información.
- Gestionar menús.
- Dibujar interfaces.
- Mostrar estadísticas.
- Gestionar navegación.
- Administrar configuraciones.
- Reproducir animaciones.
- Gestionar sonidos.
- Mejorar la experiencia del usuario.

Godot nunca implementará algoritmos complejos de Inteligencia Artificial.

Toda la lógica relacionada con Visión por Computadora permanecerá en Python.

---

# 2.6 Separación entre IA y Juego

Uno de los principios más importantes del proyecto es mantener completamente separados ambos sistemas.

Python será responsable del análisis.

Godot será responsable de la experiencia del usuario.

La comunicación entre ambos deberá realizarse mediante una interfaz claramente definida.

Esto permitirá sustituir cualquiera de los dos componentes sin afectar al otro.

---

# 2.7 Calidad del Código

Todo el código nuevo deberá cumplir los siguientes requisitos.

- Ser legible.
- Ser documentado.
- Ser modular.
- Ser reutilizable.
- Ser fácil de probar.
- Evitar duplicación.
- Seguir convenciones consistentes.

Antes de agregar una nueva funcionalidad deberá evaluarse si ya existe un módulo capaz de resolver ese problema.

---

# 2.8 Testing

Toda funcionalidad importante deberá incluir pruebas.

Siempre que sea posible deberán existir:

- Pruebas unitarias.
- Pruebas de integración.

El objetivo es garantizar que futuras modificaciones no rompan funcionalidades existentes.

---

# 2.9 Documentación

La documentación es considerada parte del software.

Cada Sprint importante deberá actualizar al menos uno de los siguientes documentos:

- README.md
- PROJECT_CONTEXT.md
- PROJECT_ARCHITECTURE.md
- ROADMAP.md
- Documentación específica dentro de la carpeta docs/

El código y la documentación deberán evolucionar al mismo tiempo.

---

# 2.10 Filosofía para futuras Inteligencias Artificiales

Este proyecto está diseñado para poder continuar su desarrollo utilizando diferentes asistentes de Inteligencia Artificial.

Por este motivo, cualquier IA que participe deberá:

- Leer primero PROJECT_CONTEXT.md.
- Comprender la arquitectura antes de modificar código.
- Respetar la separación de responsabilidades.
- No romper la modularidad.
- No introducir dependencias innecesarias.
- Mantener la compatibilidad con los módulos existentes.
- Documentar cualquier cambio importante.
- Actualizar el Roadmap cuando se complete un Sprint.

El objetivo es que cualquier IA pueda continuar exactamente donde terminó la anterior sin necesidad de reconstruir el contexto del proyecto.

---

# 3. Estado Actual del Proyecto

## 3.1 Introducción

Esta sección documenta el estado actual del proyecto VJC Hoops AI.

Su propósito es servir como un punto de referencia para desarrolladores y asistentes de Inteligencia Artificial.

Antes de modificar cualquier componente del sistema deberá consultarse esta sección para conocer qué módulos ya existen, cuáles están terminados, cuáles están en desarrollo y cuáles aún forman parte del Roadmap.

Esta información deberá mantenerse actualizada al finalizar cada Sprint importante.

---

# 3.2 Estado General

Actualmente el proyecto se encuentra en una fase temprana de desarrollo.

La arquitectura base ya fue construida y las primeras piezas del pipeline de Visión por Computadora ya funcionan correctamente.

En este momento el sistema es capaz de:

- Capturar video desde una cámara.
- Administrar correctamente los frames.
- Detectar personas mediante YOLO.
- Mantener IDs persistentes utilizando un motor de tracking.
- Dibujar la información sobre la imagen.
- Mostrar FPS en tiempo real.
- Ejecutar pruebas automáticas.

Aunque el sistema todavía no analiza tiros de baloncesto, ya existe una base sólida sobre la cual se construirán los siguientes módulos.

---

# 3.3 Estado de los Sprints

## Sprint 1

Nombre:

Frame Manager

Estado:

Completado.

Objetivo:

Crear la estructura inicial del proyecto y administrar correctamente el procesamiento de imágenes.

Resultado:

Existe una base estable para manipular los frames del sistema.

---

## Sprint 2

Nombre:

Camera Service

Estado:

Completado.

Objetivo:

Crear un servicio independiente encargado de abrir la cámara y obtener imágenes.

Resultado:

La captura de video quedó completamente desacoplada del resto del proyecto.

---

## Sprint 3

Nombre:

Video Preview

Estado:

Completado.

Objetivo:

Mostrar el video capturado utilizando OpenCV.

Resultado:

Existe una ventana de visualización que recibe los frames del sistema.

---

## Sprint 4

Nombre:

Person Detector

Estado:

Completado.

Objetivo:

Integrar YOLO para detectar personas.

Resultado:

El sistema detecta únicamente la clase Person del modelo COCO.

Características implementadas:

- Carga única del modelo.
- Uso de YOLOv8.
- Bounding Boxes.
- Nivel de confianza.
- Integración con CameraService.
- Integración con FrameManager.

---

## Sprint 5

Nombre:

Object Tracker

Estado:

Completado.

Objetivo:

Mantener IDs persistentes entre frames.

Resultado:

Cada jugador conserva el mismo identificador mientras permanezca visible.

Características implementadas:

- Matching por IoU.
- IDs incrementales.
- Tolerancia a desapariciones temporales.
- Independencia respecto al detector.
- Integración completa con el preview.

---

# 3.4 Pipeline Actual

Actualmente el flujo del sistema es el siguiente.

```
Cámara

↓

CameraService

↓

FrameManager

↓

PersonDetector

↓

ObjectTracker

↓

Visualización OpenCV
```

Cada módulo realiza únicamente una responsabilidad.

Ningún módulo conoce detalles internos de los demás.

Esta separación es uno de los principios fundamentales del proyecto.

---

# 3.5 Arquitectura Actual

En este momento existen dos grandes bloques.

## Motor de IA

Desarrollado en Python.

Responsabilidades actuales:

- Captura de video.
- Administración de frames.
- Detección de personas.
- Tracking.
- Visualización.

---

## Cliente del Juego

Actualmente todavía no ha comenzado su desarrollo.

Será construido utilizando Godot 4.

Responsabilidades futuras:

- Pantalla de inicio.
- Login.
- Editor de personajes.
- Dashboard.
- Configuración.
- Estadísticas.
- Perfil.
- Entrenamientos.
- Sistema de progreso.

---

# 3.6 Estado del Repositorio

Actualmente la estructura del proyecto es similar a la siguiente.

```
VJC-Hoops-AI/

docs/

src/

tests/

models/

data/

README.md

README_EN.md

PROJECT_CONTEXT.md

PROJECT_ARCHITECTURE.md

ROADMAP.md

main.py

requirements.txt

pyproject.toml
```

Esta estructura crecerá conforme se implementen nuevos módulos.

---

# 3.7 Estado de la Arquitectura

Actualmente la arquitectura sigue los principios de Clean Architecture.

Las responsabilidades ya se encuentran separadas correctamente.

La lógica del dominio permanece independiente de OpenCV y YOLO.

Las dependencias externas permanecen dentro de Infrastructure.

Esta separación deberá mantenerse durante todo el proyecto.

---

# 3.8 Cobertura de Pruebas

Actualmente existen pruebas para:

- CameraService.
- PersonDetector.
- ObjectTracker.
- Visualización.
- Integración del pipeline.

Cada Sprint deberá aumentar la cobertura de pruebas.

No deberán eliminarse pruebas existentes salvo que exista una justificación técnica.

---

# 3.9 Próximo Objetivo

El siguiente gran paso del proyecto consiste en comenzar el análisis deportivo.

Los próximos módulos previstos son:

- Pose Estimation.
- Ball Detection.
- Court Detection.
- Shot Detection.

Estos módulos transformarán el proyecto desde un simple detector de personas hacia un verdadero asistente inteligente para entrenamiento de baloncesto.

---

# 3.10 Estado General del Proyecto

Actualmente el proyecto posee una base sólida.

Las primeras capas del sistema ya están desacopladas y probadas.

La arquitectura fue diseñada pensando en el crecimiento a largo plazo.

A partir de este punto el desarrollo se enfocará en incorporar nuevas capacidades de Inteligencia Artificial y, de manera paralela, comenzar la construcción del cliente gráfico utilizando Godot.

El objetivo final es integrar ambos componentes en una única plataforma que permita analizar entrenamientos reales mientras ofrece una experiencia moderna, intuitiva y atractiva para el usuario.

---

# 4. Arquitectura General del Sistema

## 4.1 Introducción

La arquitectura de VJC Hoops AI ha sido diseñada para construir una plataforma escalable, modular y fácilmente mantenible.

El proyecto no está pensado como una aplicación pequeña o un prototipo, sino como una plataforma que continuará creciendo durante muchos años.

Por esta razón, desde las primeras etapas del desarrollo se decidió separar completamente cada responsabilidad del sistema.

La arquitectura busca cumplir cinco objetivos principales:

- Escalabilidad.
- Bajo acoplamiento.
- Alta cohesión.
- Facilidad para realizar pruebas.
- Facilidad para incorporar nuevas tecnologías.

Cada nuevo módulo deberá respetar estos principios.

---

# 4.2 Visión General

VJC Hoops AI está formado por dos grandes sistemas completamente independientes.

```
                VJC Hoops AI

        ┌──────────────────────────────┐
        │                              │
        │        GODOT 4               │
        │ (Interfaz del Videojuego)    │
        │                              │
        └──────────────┬───────────────┘
                       │
             Comunicación de Datos
                       │
        ┌──────────────▼───────────────┐
        │                              │
        │         PYTHON               │
        │ Motor de Inteligencia        │
        │ Artificial                   │
        │                              │
        └──────────────────────────────┘
```

Ambos componentes evolucionarán de forma independiente.

Esto permitirá modificar cualquiera de ellos sin afectar al otro.

---

# 4.3 Motor de Inteligencia Artificial

El motor desarrollado en Python constituye el núcleo técnico del proyecto.

Su responsabilidad es transformar imágenes provenientes de la cámara en información útil para el jugador.

El motor no tiene interfaces gráficas complejas.

No administra menús.

No contiene pantallas.

No administra configuraciones visuales.

Su única responsabilidad es analizar información.

Entre sus funciones se encuentran:

- Captura de vídeo.
- Procesamiento de imágenes.
- Detección de personas.
- Tracking.
- Estimación de pose.
- Detección del balón.
- Detección del aro.
- Reconocimiento de tiros.
- Cálculo de estadísticas.
- Exportación de resultados.

Todo el procesamiento deportivo ocurre aquí.

---

# 4.4 Cliente Godot

Godot será el responsable de toda la experiencia visual.

El jugador interactuará únicamente con Godot.

Nunca directamente con Python.

Godot será responsable de:

- Pantalla de inicio.
- Login.
- Navegación.
- Dashboard.
- Perfil.
- Editor de personajes.
- Entrenamientos.
- Tienda.
- Logros.
- Configuración.
- Animaciones.
- Audio.
- Notificaciones.

Godot nunca implementará algoritmos deportivos.

Toda la Inteligencia Artificial continuará viviendo en Python.

---

# 4.5 Comunicación entre Sistemas

Uno de los principios más importantes del proyecto es mantener desacoplados ambos sistemas.

La comunicación deberá realizarse mediante una interfaz claramente definida.

En el futuro podrán utilizarse diferentes tecnologías dependiendo de las necesidades del proyecto.

Algunas opciones contempladas son:

- REST API.
- WebSockets.
- TCP/IP.
- gRPC.
- Archivos JSON.
- Memoria compartida.

La decisión definitiva se tomará cuando el cliente Godot necesite comunicarse en tiempo real con el motor de IA.

Mientras tanto ambos sistemas podrán desarrollarse completamente por separado.

---

# 4.6 Arquitectura Interna del Motor IA

Internamente Python seguirá una arquitectura basada en capas.

```
Presentación

↓

Infraestructura

↓

Aplicación

↓

Dominio
```

Cada capa tendrá responsabilidades completamente independientes.

---

## Dominio

Es la capa más importante.

Representa las reglas del negocio.

Nunca conocerá:

- OpenCV.
- YOLO.
- Godot.
- Interfaces gráficas.
- APIs externas.

Aquí únicamente existirán conceptos deportivos.

Ejemplos:

- Jugador.
- Entrenamiento.
- Tiro.
- Estadística.
- Sesión.
- Intento.

---

## Aplicación

Coordina los casos de uso.

Aquí vivirán los servicios encargados de conectar el dominio con la infraestructura.

Ejemplos:

- Analizar entrenamiento.
- Procesar sesión.
- Generar estadísticas.
- Exportar resultados.

---

## Infraestructura

Contiene toda dependencia externa.

Aquí viven:

- OpenCV.
- YOLO.
- Cámara.
- Archivos.
- Modelos IA.
- Comunicación con Godot.

Todo cambio tecnológico deberá quedar encapsulado aquí.

---

## Presentación

Actualmente está representada por `main.py`.

En el futuro será sustituida por Godot.

Su única responsabilidad será iniciar la aplicación y mostrar resultados.

Nunca deberá contener lógica de negocio.

---

# 4.7 Flujo Completo del Sistema

El flujo esperado del proyecto será el siguiente.

```
Jugador

↓

Cámara

↓

CameraService

↓

FrameManager

↓

PersonDetector

↓

ObjectTracker

↓

Pose Estimation

↓

Ball Detection

↓

Rim Detection

↓

Shot Detection

↓

Statistics Engine

↓

API de Comunicación

↓

Godot

↓

Jugador
```

Este flujo representa la visión completa del proyecto.

Actualmente solamente una parte del pipeline ha sido implementada.

Los siguientes Sprints irán completando el resto.

---

# 4.8 Organización Modular

Todos los módulos deberán ser independientes.

Cada módulo tendrá una única responsabilidad.

Ejemplo:

CameraService

↓

Captura imágenes.

PersonDetector

↓

Detecta personas.

ObjectTracker

↓

Asigna IDs.

PoseEstimator

↓

Calcula articulaciones.

ShotDetector

↓

Detecta lanzamientos.

StatisticsEngine

↓

Calcula estadísticas.

Cada uno podrá modificarse sin afectar a los demás.

---

# 4.9 Escalabilidad

La arquitectura fue diseñada pensando en futuras ampliaciones.

Entre las funcionalidades previstas se encuentran:

- Entrenamientos personalizados.
- Múltiples jugadores.
- Diferentes deportes.
- Modelos IA intercambiables.
- Nuevas cámaras.
- Sensores externos.
- IA en la nube.
- Procesamiento distribuido.
- Aplicación móvil.
- Plataforma web.

El crecimiento del proyecto no deberá requerir reescribir la arquitectura.

---

# 4.10 Principios que Nunca Deben Romperse

Existen principios fundamentales que deberán respetarse durante toda la vida del proyecto.

Estos principios son obligatorios.

- Nunca mezclar lógica de negocio con interfaces gráficas.
- Nunca colocar código de OpenCV dentro del dominio.
- Nunca colocar YOLO fuera de Infrastructure.
- Nunca duplicar responsabilidades.
- Cada clase debe tener una única responsabilidad.
- Cada módulo debe poder probarse de manera independiente.
- Toda nueva funcionalidad deberá documentarse.
- Todo Sprint deberá mantener la arquitectura limpia.
- Antes de escribir código deberá analizarse si existe un módulo capaz de resolver ese problema.

Estos principios representan la base técnica de VJC Hoops AI y garantizan que el proyecto pueda seguir creciendo durante muchos años sin perder calidad.

---

# 5. Pipeline Completo de Inteligencia Artificial

## 5.1 Introducción

El motor de Inteligencia Artificial constituye el núcleo tecnológico de VJC Hoops AI.

Su responsabilidad es transformar un flujo continuo de imágenes provenientes de una cámara en información deportiva útil para el jugador.

Todo el análisis ocurre dentro del motor desarrollado en Python.

Godot nunca procesará visión artificial.

Godot únicamente recibirá resultados.

Esta separación permite mantener un sistema modular, reutilizable y fácilmente escalable.

---

# 5.2 Objetivo del Pipeline

El objetivo del pipeline es convertir un simple video en conocimiento útil.

El usuario únicamente verá estadísticas.

Sin embargo, internamente el sistema realizará una gran cantidad de procesos consecutivos.

Cada módulo del pipeline resolverá una única responsabilidad.

Esto permitirá sustituir cualquier algoritmo sin modificar el resto del sistema.

---

# 5.3 Filosofía del Pipeline

Todos los módulos deberán cumplir las siguientes reglas.

- Una única responsabilidad.
- Independencia del resto del sistema.
- Fácil reemplazo.
- Fácil mantenimiento.
- Fácil prueba.
- Fácil documentación.

El pipeline deberá comportarse como una cadena donde cada módulo recibe información, la transforma y entrega un nuevo resultado al siguiente módulo.

---

# 5.4 Flujo General

El flujo completo previsto para el proyecto será el siguiente.

```
Jugador

↓

Cámara

↓

CameraService

↓

FrameManager

↓

PersonDetector

↓

ObjectTracker

↓

BallDetector

↓

RimDetector

↓

CourtDetector

↓

PoseEstimator

↓

ShotDetector

↓

StatisticsEngine

↓

Exportador de Datos

↓

API

↓

Godot
```

Actualmente únicamente una parte de este flujo ha sido implementada.

El resto será desarrollado progresivamente mediante nuevos Sprints.

---

# 5.5 Captura de Vídeo

La primera etapa consiste en obtener imágenes desde la cámara.

Responsable:

CameraService

Funciones:

- Abrir la cámara.
- Configurar resolución.
- Leer frames.
- Detectar errores.
- Liberar recursos.

La captura debe ser completamente independiente del análisis posterior.

---

# 5.6 Administración de Frames

Una vez capturada la imagen, el FrameManager controla el flujo de procesamiento.

Responsabilidades:

- Recibir frames.
- Validar imágenes.
- Entregar el frame al siguiente módulo.
- Mantener un flujo continuo.

No debe contener lógica deportiva.

---

# 5.7 Detección de Personas

Responsable:

PersonDetector

Modelo actual:

YOLOv8.

Objetivo:

Localizar todas las personas presentes en la imagen.

Salida esperada:

- Bounding Box.
- Confianza.
- Clase detectada.

Actualmente únicamente se procesa la clase `person`.

En el futuro podrán añadirse nuevas clases si son necesarias.

---

# 5.8 Tracking

Responsable:

ObjectTracker

Objetivo:

Mantener una identidad única para cada jugador durante toda la sesión.

Funciones:

- Asignar IDs.
- Mantener IDs entre frames.
- Detectar desapariciones temporales.
- Crear nuevos tracks.

El tracker no depende de YOLO.

Puede trabajar con cualquier detector que produzca cajas delimitadoras.

---

# 5.9 Detección del Balón

Estado:

Pendiente.

Objetivo:

Localizar el balón en cada frame.

Información generada:

- Posición.
- Velocidad.
- Trayectoria.
- Dirección.

Este módulo será fundamental para detectar lanzamientos.

---

# 5.10 Detección del Aro

Estado:

Pendiente.

Objetivo:

Detectar automáticamente la posición del aro.

Información generada:

- Centro.
- Altura.
- Tamaño.
- Región válida.

---

# 5.11 Estimación de Pose

Estado:

Pendiente.

Objetivo:

Calcular la posición de las articulaciones del jugador.

Articulaciones principales:

- Cabeza.
- Cuello.
- Hombros.
- Codos.
- Muñecas.
- Cadera.
- Rodillas.
- Tobillos.

Esta información permitirá analizar la técnica de lanzamiento.

---

# 5.12 Detección del Tiro

Estado:

Pendiente.

Este módulo será uno de los más complejos del proyecto.

Será responsable de determinar:

- Cuándo inicia un tiro.
- Cuándo termina.
- Si fue exitoso.
- Ángulo de salida.
- Tiempo de lanzamiento.
- Trayectoria.

Para ello combinará información proveniente de:

- BallDetector.
- PoseEstimator.
- RimDetector.
- ObjectTracker.

---

# 5.13 Motor de Estadísticas

Estado:

Pendiente.

Será responsable de calcular:

- Tiros intentados.
- Tiros anotados.
- Porcentaje de acierto.
- Tiempo promedio.
- Velocidad del balón.
- Ángulo promedio.
- Consistencia.
- Evolución histórica.

---

# 5.14 Exportación de Resultados

Una vez finalizado el análisis, toda la información deberá transformarse en un formato fácilmente consumible por Godot.

Inicialmente se contempla el uso de JSON.

En el futuro podrán utilizarse otros mecanismos dependiendo de las necesidades del proyecto.

---

# 5.15 Comunicación con Godot

El pipeline finalizará enviando la información procesada al cliente desarrollado en Godot.

Godot mostrará:

- Estadísticas.
- Animaciones.
- Dashboard.
- Progreso.
- Historial.
- Logros.

Godot nunca recalculará datos deportivos.

Toda la información deberá provenir del motor de IA.

---

# 5.16 Estado Actual del Pipeline

Actualmente se encuentran implementados:

✔ CameraService

✔ FrameManager

✔ PersonDetector

✔ ObjectTracker

Los siguientes módulos forman parte del Roadmap:

◻ BallDetector

◻ RimDetector

◻ CourtDetector

◻ PoseEstimator

◻ ShotDetector

◻ StatisticsEngine

◻ Exportador

◻ Comunicación con Godot

---

# 5.17 Objetivo Final

Cuando el pipeline esté completamente desarrollado, el sistema será capaz de analizar automáticamente una sesión completa de entrenamiento.

El usuario únicamente deberá iniciar una práctica frente a la cámara.

Todo el procesamiento restante será realizado por el motor de Inteligencia Artificial de forma automática.

El resultado será una plataforma capaz de proporcionar métricas objetivas sobre el rendimiento del jugador y presentar dicha información mediante una interfaz moderna desarrollada con Godot.

---

# 6. Arquitectura del Videojuego (Godot)

## 6.1 Introducción

El cliente del videojuego será desarrollado utilizando **Godot Engine 4.x**.

Su objetivo principal no será realizar análisis de Inteligencia Artificial, sino proporcionar una experiencia moderna, intuitiva y motivadora para el jugador.

Toda la lógica relacionada con visión por computadora permanecerá en Python.

Godot actuará como la interfaz visual del sistema.

Esta separación permitirá que ambos proyectos evolucionen de manera independiente.

---

# 6.2 ¿Por qué Godot?

Después de analizar diferentes motores de videojuegos, se decidió utilizar Godot por las siguientes razones.

- Es completamente gratuito y de código abierto.
- No requiere pago de licencias.
- Posee una excelente documentación.
- Tiene un excelente rendimiento en aplicaciones 2D.
- Permite crear interfaces modernas con gran facilidad.
- Es altamente personalizable.
- Posee una arquitectura basada en escenas muy modular.
- Es compatible con Windows, Linux, macOS, Android e iOS.
- Puede comunicarse fácilmente con aplicaciones externas.

Godot será utilizado exclusivamente para la experiencia del usuario.

---

# 6.3 Objetivos del Cliente Godot

El cliente tendrá como objetivo proporcionar una experiencia similar a un videojuego moderno.

No será únicamente una aplicación para mostrar estadísticas.

El jugador deberá sentir que está progresando constantemente.

El cliente deberá incluir:

- Pantalla de inicio.
- Login.
- Perfil.
- Editor de personajes.
- Dashboard.
- Entrenamientos.
- Estadísticas.
- Logros.
- Configuración.
- Sistema de progreso.
- Animaciones.
- Sonidos.
- Interfaz moderna.

---

# 6.4 Filosofía del Cliente

Godot nunca deberá contener algoritmos deportivos.

Todo cálculo relacionado con:

- IA
- OpenCV
- YOLO
- Tracking
- Estadísticas

deberá realizarse en Python.

Godot únicamente recibirá resultados y los mostrará al usuario.

---

# 6.5 Arquitectura por Escenas

Godot organiza los proyectos mediante escenas.

Cada pantalla importante será una escena independiente.

Ejemplo:

MainMenu.tscn

↓

Login.tscn

↓

Dashboard.tscn

↓

CharacterEditor.tscn

↓

Training.tscn

↓

Statistics.tscn

↓

Settings.tscn

↓

Profile.tscn

Esto permitirá trabajar de forma modular.

---

# 6.6 Organización del Proyecto Godot

La estructura prevista será similar a la siguiente.

```
godot/

assets/

audio/

fonts/

icons/

images/

animations/

materials/

scenes/

scripts/

themes/

ui/

config/

resources/

addons/

project.godot
```

Cada carpeta tendrá una responsabilidad específica.

---

# 6.7 Organización de Escenas

Las escenas estarán separadas según su función.

Ejemplo:

```
scenes/

main/

login/

dashboard/

training/

character/

profile/

settings/

statistics/

common/
```

Esto facilitará el mantenimiento conforme el proyecto crezca.

---

# 6.8 Organización de Scripts

Los scripts de Godot también estarán organizados por módulos.

Ejemplo:

```
scripts/

main/

dashboard/

training/

profile/

settings/

character/

network/

ui/

utils/
```

Cada script deberá tener una única responsabilidad.

---

# 6.9 Flujo General del Usuario

La navegación prevista será la siguiente.

```
Inicio

↓

Login

↓

Menú Principal

↓

Perfil

↓

Entrenamiento

↓

Resultados

↓

Dashboard

↓

Configuración
```

El usuario podrá regresar al menú principal desde cualquier pantalla.

---

# 6.10 Comunicación con Python

Godot nunca accederá directamente a la cámara.

Nunca ejecutará modelos de IA.

Su responsabilidad será solicitar información al motor desarrollado en Python.

Ejemplo del flujo esperado.

```
Jugador

↓

Godot

↓

Python

↓

Procesamiento IA

↓

Resultados

↓

Godot

↓

Interfaz
```

---

# 6.11 Sistema Visual

El diseño seguirá una estética moderna inspirada en aplicaciones deportivas y videojuegos.

Se utilizarán:

- Tarjetas.
- Paneles.
- Gradientes.
- Sombras suaves.
- Animaciones.
- Iconografía minimalista.
- Colores consistentes.

El objetivo será ofrecer una experiencia profesional.

---

# 6.12 Rendimiento

El cliente deberá mantenerse ligero.

La mayor parte del procesamiento se realizará en Python.

Godot únicamente renderizará:

- Interfaces.
- Animaciones.
- Avatares.
- Resultados.
- Gráficos.

Esto permitirá mantener una alta tasa de FPS incluso en equipos modestos.

---

# 6.13 Personalización

Uno de los objetivos principales del videojuego será permitir que cada usuario tenga una identidad propia.

El sistema deberá permitir personalizar:

- Apariencia del personaje.
- Color de piel.
- Cabello.
- Barba.
- Ojos.
- Ropa.
- Uniformes.
- Calzado.
- Accesorios.
- Balones.
- Animaciones.
- Celebraciones.

Toda esta información será almacenada en el perfil del jugador.

---

# 6.14 Escalabilidad

El cliente deberá diseñarse pensando en futuras expansiones.

Entre las características previstas se encuentran:

- Multijugador.
- Rankings.
- Torneos.
- Eventos.
- Desafíos diarios.
- Tienda.
- Pase de temporada.
- Logros.
- Misiones.
- Nuevos modos de entrenamiento.

La arquitectura deberá permitir añadir estos módulos sin reorganizar completamente el proyecto.

---

# 6.15 Objetivo Final

El objetivo del cliente Godot es convertir un sistema de análisis deportivo en una experiencia interactiva y motivadora.

El jugador no deberá sentir que utiliza una herramienta técnica.

Deberá sentir que está jugando, entrenando y progresando dentro de un videojuego profesional.

Godot será la cara visible de VJC Hoops AI, mientras que Python será el motor inteligente que realizará todo el análisis deportivo.

---

# 7. Comunicación entre Python y Godot

## 7.1 Introducción

Uno de los principios más importantes de VJC Hoops AI es mantener completamente desacoplados el motor de Inteligencia Artificial y el cliente desarrollado en Godot.

Ambos sistemas deberán evolucionar de forma independiente.

Esto permitirá actualizar cualquiera de los dos componentes sin afectar directamente al otro.

Python será responsable del análisis deportivo.

Godot será responsable de la experiencia del usuario.

La comunicación entre ambos deberá realizarse mediante un protocolo claramente definido.

---

# 7.2 Filosofía de Comunicación

La comunicación deberá cumplir los siguientes principios.

- Bajo acoplamiento.
- Fácil mantenimiento.
- Fácil depuración.
- Independencia tecnológica.
- Escalabilidad.
- Compatibilidad con futuras versiones.

Godot nunca deberá acceder directamente a las clases internas del motor de IA.

Python nunca deberá conocer escenas de Godot.

Ambos proyectos únicamente compartirán datos.

---

# 7.3 Responsabilidades

## Python

Será responsable de:

- Capturar vídeo.
- Detectar personas.
- Realizar tracking.
- Detectar el balón.
- Detectar el aro.
- Analizar la pose.
- Detectar tiros.
- Calcular estadísticas.
- Exportar resultados.

Nunca deberá preocuparse por la interfaz.

---

## Godot

Será responsable de:

- Mostrar menús.
- Mostrar resultados.
- Mostrar estadísticas.
- Mostrar animaciones.
- Mostrar gráficos.
- Administrar el perfil del jugador.
- Gestionar configuraciones.
- Gestionar la navegación.

Nunca recalculará datos deportivos.

---

# 7.4 Flujo General

El flujo previsto será el siguiente.

```
Jugador

↓

Godot

↓

Solicitud de entrenamiento

↓

Python

↓

Pipeline IA

↓

Resultados

↓

Archivo JSON

↓

Godot

↓

Dashboard
```

Este flujo representa la primera versión del sistema.

Posteriormente podrá evolucionar hacia comunicación en tiempo real.

---

# 7.5 Primera Implementación

La primera comunicación utilizará archivos JSON.

¿Por qué?

Porque:

- Es simple.
- Es fácil de depurar.
- Es multiplataforma.
- No requiere servidores.
- Es muy estable.

Python generará archivos JSON.

Godot únicamente los leerá.

---

# 7.6 Formato de Intercambio

Toda la información intercambiada entre ambos sistemas deberá almacenarse en estructuras fácilmente serializables.

Ejemplo conceptual.

```json
{
    "player": {},
    "session": {},
    "shots": [],
    "statistics": {},
    "tracking": {}
}
```

El formato definitivo podrá ampliarse con nuevas propiedades.

Nunca deberán eliminarse campos existentes sin mantener compatibilidad.

---

# 7.7 Evolución del Sistema

Conforme el proyecto crezca podrán incorporarse nuevos métodos de comunicación.

Las opciones previstas incluyen:

- JSON.
- REST API.
- WebSockets.
- TCP/IP.
- gRPC.
- Memoria compartida.

La elección dependerá de los requisitos de rendimiento.

---

# 7.8 Comunicación en Tiempo Real

En una fase posterior del proyecto se implementará comunicación bidireccional entre Godot y Python.

Esto permitirá mostrar información mientras el jugador está entrenando.

Ejemplos:

- FPS.
- Persona detectada.
- ID del jugador.
- Posición del balón.
- Trayectoria.
- Ángulo del tiro.
- Velocidad.
- Resultado del lanzamiento.

Godot podrá actualizar la interfaz varias veces por segundo.

---

# 7.9 Estados del Sistema

El motor de IA deberá informar continuamente su estado.

Ejemplos.

Inicializando.

Cámara conectada.

Modelo cargado.

Procesando.

Analizando jugador.

Calculando estadísticas.

Entrenamiento finalizado.

Estos estados permitirán que Godot muestre mensajes adecuados al usuario.

---

# 7.10 Manejo de Errores

Toda comunicación deberá contemplar errores.

Ejemplos.

- Cámara no encontrada.
- Modelo no cargado.
- Archivo inexistente.
- Error de lectura.
- Error de escritura.
- Tiempo de espera excedido.

Godot nunca deberá bloquearse por un error del motor IA.

Python nunca deberá finalizar inesperadamente por un error del cliente.

---

# 7.11 Compatibilidad

La comunicación deberá diseñarse pensando en futuras plataformas.

En el futuro el motor de IA podrá comunicarse con:

- Aplicación móvil.
- Aplicación web.
- Dashboard remoto.
- API pública.
- Aplicación de escritorio.

Godot será únicamente uno de los posibles clientes.

---

# 7.12 Objetivo Final

El objetivo es construir un sistema donde el motor de Inteligencia Artificial funcione como un servicio independiente.

Godot será uno de los clientes capaces de consumir los resultados generados por dicho servicio.

Esta arquitectura permitirá reutilizar el motor de IA en múltiples plataformas sin necesidad de modificar sus algoritmos internos.

---

# 8. Modelo de Datos Compartidos

## 8.1 Introducción

Uno de los principios fundamentales de VJC Hoops AI es mantener completamente desacoplados el motor de Inteligencia Artificial desarrollado en Python y el cliente del videojuego desarrollado en Godot.

Para lograr esta independencia ambos sistemas compartirán únicamente datos.

Ninguno de los dos conocerá las clases internas del otro.

Por esta razón se define un modelo de datos común que servirá como contrato entre ambos componentes.

Toda información intercambiada deberá respetar estas estructuras.

Si en el futuro se agregan nuevos campos, deberá mantenerse la compatibilidad con versiones anteriores siempre que sea posible.

---

# 8.2 Filosofía del Modelo de Datos

El modelo de datos deberá cumplir los siguientes principios.

- Simplicidad.
- Claridad.
- Independencia del lenguaje.
- Fácil serialización.
- Fácil extensión.
- Compatibilidad futura.

Toda estructura deberá poder convertirse fácilmente a:

- JSON
- Base de datos
- API REST
- WebSockets

sin modificar su significado.

---

# 8.3 Entidades Principales

El proyecto estará compuesto por las siguientes entidades.

Player

Representa al usuario que utiliza la aplicación.

Session

Representa una sesión completa de entrenamiento.

Shot

Representa un lanzamiento individual.

Statistics

Contiene los resultados calculados por la IA.

Character

Describe la apariencia visual del jugador.

Settings

Contiene la configuración personalizada.

Achievement

Representa un logro desbloqueado.

Training

Representa un tipo específico de entrenamiento.

Cada entidad tendrá responsabilidades claramente definidas.

---

# 8.4 Player

Representa al jugador.

Información prevista:

- ID único.
- Nombre.
- Nombre de usuario.
- Fecha de creación.
- Nivel.
- Experiencia.
- Avatar.
- Configuración.
- Estadísticas globales.

Ejemplo conceptual:

```json
{
    "id": 1,
    "username": "Julio",
    "level": 5,
    "experience": 3400
}
```

---

# 8.5 Character

Describe únicamente la apariencia del jugador.

No contiene estadísticas deportivas.

Campos previstos.

- Color de piel.
- Tipo de cabello.
- Color de cabello.
- Ojos.
- Barba.
- Uniforme.
- Calzado.
- Accesorios.
- Balón seleccionado.
- Animaciones.

Ejemplo.

```json
{
    "hair": "short",
    "hair_color": "#1F1F1F",
    "skin": "#C58C65",
    "jersey": "blue"
}
```

---

# 8.6 Session

Representa una sesión completa de entrenamiento.

Una sesión agrupa múltiples lanzamientos.

Información prevista.

- ID.
- Fecha.
- Hora de inicio.
- Hora de finalización.
- Duración.
- Tipo de entrenamiento.
- Lista de tiros.
- Estadísticas.

Ejemplo.

```json
{
    "session_id": 20,
    "duration": 18,
    "shots": []
}
```

---

# 8.7 Shot

Representa un único lanzamiento.

Cada tiro almacenará toda la información calculada por la IA.

Datos previstos.

- ID.
- Tiempo.
- Jugador.
- Coordenadas.
- Resultado.
- Ángulo.
- Velocidad.
- Trayectoria.
- Confianza.
- Tiempo de ejecución.

Ejemplo.

```json
{
    "shot_id": 10,
    "made": true,
    "angle": 48.6,
    "speed": 6.9
}
```

---

# 8.8 Statistics

Contendrá todos los cálculos generados por el motor de IA.

Ejemplos.

- Intentos.
- Aciertos.
- Porcentaje.
- Ángulo promedio.
- Velocidad promedio.
- Tiempo promedio.
- Mejor racha.
- Consistencia.

Ejemplo.

```json
{
    "attempts": 50,
    "made": 41,
    "percentage": 82.0
}
```

---

# 8.9 Training

Describe un entrenamiento disponible.

Ejemplos.

- Tiros libres.
- Triple.
- Media distancia.
- Movimiento.
- Desafío diario.
- Personalizado.

Cada entrenamiento podrá tener reglas específicas.

---

# 8.10 Achievement

Representa un logro.

Ejemplos.

Primer tiro.

100 tiros.

500 tiros.

90% de efectividad.

Entrenamiento perfecto.

Todos los logros deberán almacenarse en el perfil del jugador.

---

# 8.11 Settings

Describe la configuración del usuario.

Ejemplos.

- Idioma.
- Resolución.
- Volumen.
- Tema.
- Accesibilidad.
- Calidad gráfica.
- Cámara.

Estas configuraciones serán utilizadas exclusivamente por Godot.

---

# 8.12 Relaciones entre Entidades

El modelo conceptual será el siguiente.

Player

↓

Character

↓

Training

↓

Session

↓

Shot

↓

Statistics

↓

Achievements

Cada entidad tendrá un identificador único.

Las relaciones deberán mantenerse consistentes.

---

# 8.13 Versionado

Conforme el proyecto evolucione será necesario ampliar estas estructuras.

Las nuevas versiones deberán agregar información sin romper la compatibilidad con clientes anteriores cuando sea posible.

Se recomienda mantener un campo de versión en los archivos de intercambio.

---

# 8.14 Objetivo Final

Este modelo de datos servirá como contrato oficial entre todos los componentes de VJC Hoops AI.

Gracias a esta definición será posible desarrollar el motor de IA y el cliente Godot de manera independiente, manteniendo una comunicación clara, estable y fácilmente extensible.

---

# 9. Sistema de Escenas y Navegación (Godot)

## 9.1 Introducción

La experiencia del usuario será uno de los pilares fundamentales de VJC Hoops AI.

Aunque el proyecto incorpora un potente motor de Inteligencia Artificial desarrollado en Python, el usuario interactuará casi exclusivamente con el cliente desarrollado en Godot.

Por esta razón, el diseño de las escenas, la navegación y la organización de la interfaz deberán recibir el mismo nivel de atención que el desarrollo de los algoritmos de IA.

El objetivo no es construir una aplicación técnica para ingenieros, sino una experiencia moderna, intuitiva y motivadora para jugadores de baloncesto.

Cada pantalla deberá tener una responsabilidad claramente definida y una navegación sencilla.

---

# 9.2 Filosofía de Navegación

Toda la navegación del proyecto seguirá los siguientes principios.

- Fácil de aprender.
- Consistente.
- Fluida.
- Moderna.
- Rápida.
- Sin pantallas innecesarias.

El usuario nunca deberá perderse dentro del sistema.

Cada pantalla deberá indicar claramente dónde se encuentra y cómo regresar.

La navegación deberá requerir el menor número posible de clics.

---

# 9.3 Flujo General del Usuario

El recorrido esperado será el siguiente.

```
Pantalla de Inicio

↓

Login / Registro

↓

Menú Principal

↓

Perfil

↓

Entrenamiento

↓

Resultados

↓

Dashboard

↓

Menú Principal
```

Desde el menú principal el usuario podrá acceder a cualquier módulo.

---

# 9.4 Mapa Completo de Escenas

La organización inicial de las escenas será la siguiente.

```
MainMenu

├── Login

├── Dashboard

├── Character Editor

├── Training

├── Statistics

├── Profile

├── Settings

├── Achievements

├── Store

└── Credits
```

Cada escena será completamente independiente.

---

# 9.5 Escena Splash

Será la primera pantalla mostrada al iniciar el juego.

Mostrará:

- Logo de VJC.
- Animación de bienvenida.
- Verificación de archivos.
- Inicialización del sistema.
- Carga de recursos.

Duración aproximada.

2 a 3 segundos.

---

# 9.6 Pantalla de Inicio

Será la pantalla principal del proyecto.

Mostrará.

- Fondo animado.
- Personaje principal.
- Botón Jugar.
- Configuración.
- Créditos.
- Salir.

El objetivo será transmitir una sensación profesional desde el primer momento.

---

# 9.7 Login

Permitirá iniciar sesión.

Opciones previstas.

- Usuario y contraseña.
- Inicio rápido.
- Crear cuenta.
- Recuperar contraseña.

En futuras versiones podrán añadirse servicios externos de autenticación.

---

# 9.8 Menú Principal

El menú principal será el centro de navegación del proyecto.

Desde aquí será posible acceder a:

- Entrenamientos.
- Dashboard.
- Perfil.
- Editor de personajes.
- Configuración.
- Logros.
- Tienda.
- Créditos.

El diseño deberá ser limpio y fácil de entender.

---

# 9.9 Flujo de Entrenamiento

Cuando el jugador seleccione un entrenamiento, el sistema seguirá el siguiente flujo.

```
Seleccionar entrenamiento

↓

Configurar sesión

↓

Iniciar cámara

↓

Python analiza

↓

Godot recibe resultados

↓

Resumen

↓

Guardar sesión

↓

Regresar al Dashboard
```

Todo este proceso deberá ser automático.

---

# 9.10 Navegación Permanente

Durante cualquier pantalla deberán existir accesos rápidos para regresar a:

- Menú Principal.
- Perfil.
- Dashboard.
- Configuración.

El usuario nunca deberá sentirse atrapado en una pantalla.

---

# 9.11 Gestión de Escenas

Cada pantalla será una escena independiente de Godot.

Esto permitirá:

- Reutilización.
- Mejor organización.
- Menor consumo de memoria.
- Mayor facilidad para trabajar en equipo.

Las escenas nunca deberán depender directamente unas de otras.

La comunicación deberá realizarse mediante controladores y señales.

---

# 9.12 Transiciones

Todas las transiciones deberán ser suaves.

Ejemplos.

- Fade In.
- Fade Out.
- Desplazamientos.
- Escalado.
- Difuminado.

Nunca deberán existir cambios bruscos de pantalla.

---

# 9.13 Estados Globales

Durante la navegación existirán estados compartidos.

Ejemplos.

- Usuario autenticado.
- Entrenamiento activo.
- IA procesando.
- Guardando resultados.
- Error de conexión.
- Actualización disponible.

Estos estados podrán ser consultados por cualquier escena sin duplicar información.

---

# 9.14 Diseño Responsive

Aunque inicialmente el proyecto será para PC, toda la interfaz deberá diseñarse pensando en futuras adaptaciones.

La navegación deberá ser compatible con:

- Monitores Full HD.
- Pantallas 2K.
- Pantallas 4K.
- Tablets.
- Dispositivos móviles.

La estructura de la interfaz deberá adaptarse automáticamente al tamaño disponible.

---

# 9.15 Objetivo Final

El sistema de escenas deberá ofrecer una navegación clara, intuitiva y agradable.

Cada pantalla deberá tener una única responsabilidad y conectarse con el resto del sistema mediante una arquitectura modular.

El objetivo es que el usuario perciba VJC Hoops AI como un videojuego profesional, donde el acceso a entrenamientos, estadísticas y herramientas sea rápido, consistente y visualmente atractivo.

---

# 10. Sistema de Personajes y Editor de Personalización

## 10.1 Introducción

Uno de los principales objetivos de VJC Hoops AI es ofrecer una experiencia cercana a la de un videojuego moderno.

El usuario no solamente utilizará una herramienta para analizar sus entrenamientos, sino que también construirá una identidad propia dentro de la plataforma.

Por esta razón se implementará un completo sistema de personalización de personajes.

Cada jugador podrá crear un avatar único que lo representará durante toda su experiencia dentro del juego.

Este sistema deberá ser intuitivo, flexible y fácilmente ampliable.

---

# 10.2 Objetivos

El editor de personajes tiene como propósito:

- Crear una identidad visual para cada jugador.
- Incrementar el nivel de personalización.
- Mejorar la inmersión.
- Motivar al usuario a continuar entrenando.
- Servir como base para futuros sistemas de progresión y recompensas.

La personalización será completamente independiente del análisis realizado por la IA.

---

# 10.3 Filosofía del Sistema

El personaje representa al usuario, pero no influye en el análisis deportivo.

Modificar la apariencia nunca cambiará las estadísticas, la dificultad ni los resultados del entrenamiento.

Toda la personalización será exclusivamente visual.

Esto garantiza una experiencia justa y centrada en el progreso real del jugador.

---

# 10.4 Arquitectura General

El sistema estará dividido en cuatro componentes principales:

- Character Manager
- Character Editor
- Character Renderer
- Character Storage

Cada componente tendrá responsabilidades claramente definidas.

---

## Character Manager

Será el encargado de administrar toda la información del personaje.

Responsabilidades:

- Crear personajes.
- Cargar personajes.
- Guardar cambios.
- Aplicar personalizaciones.
- Gestionar identificadores.

---

## Character Editor

Será la interfaz utilizada por el jugador.

Permitirá modificar la apariencia en tiempo real.

Toda modificación deberá visualizarse inmediatamente.

---

## Character Renderer

Será responsable de dibujar el personaje.

No almacenará información.

Únicamente interpretará los datos enviados por Character Manager.

---

## Character Storage

Será el encargado de almacenar toda la configuración del personaje.

Inicialmente utilizará archivos JSON.

En futuras versiones podrá utilizar bases de datos.

---

# 10.5 Personalización Física

El jugador podrá modificar diferentes características visuales.

Inicialmente estarán disponibles las siguientes categorías.

## Cabello

Opciones previstas:

- Corto.
- Largo.
- Rizado.
- Afro.
- Trenzas.
- Rapado.
- Coleta.
- Mohicano.

Cada peinado tendrá múltiples colores disponibles.

---

## Barba

Opciones:

- Sin barba.
- Barba corta.
- Barba completa.
- Bigote.
- Candado.

---

## Cejas

El jugador podrá modificar:

- Forma.
- Grosor.
- Color.

---

## Ojos

Opciones previstas:

- Color.
- Tamaño.
- Forma.

---

## Nariz

Opciones futuras:

- Tamaño.
- Anchura.
- Longitud.

---

## Boca

Opciones futuras:

- Tamaño.
- Forma.

---

## Piel

El sistema permitirá seleccionar diferentes tonos de piel.

No existirán restricciones.

---

# 10.6 Uniformes

El jugador podrá seleccionar diferentes prendas deportivas.

Inicialmente se contemplan.

- Playera.
- Jersey.
- Shorts.
- Calcetas.
- Tenis.

Cada elemento podrá personalizarse mediante colores.

---

# 10.7 Balones

Cada usuario podrá seleccionar el balón utilizado durante la representación visual.

Ejemplos.

- Balón clásico.
- Balón callejero.
- Balón profesional.
- Balón dorado.
- Balón futurista.

La IA siempre analizará el balón real capturado por la cámara.

La personalización únicamente afectará la interfaz.

---

# 10.8 Accesorios

El sistema permitirá incorporar accesorios cosméticos.

Ejemplos.

- Muñequeras.
- Rodilleras.
- Cintas para la cabeza.
- Mangas deportivas.
- Lentes.
- Collares.

Todos serán completamente opcionales.

---

# 10.9 Animaciones

El personaje contará con animaciones para diferentes acciones.

Ejemplos.

- Idle.
- Caminar.
- Correr.
- Lanzar.
- Celebrar.
- Aplaudir.
- Saludar.
- Derrota.

Las animaciones mejorarán la experiencia del usuario sin afectar la lógica del entrenamiento.

---

# 10.10 Expresiones

El personaje podrá mostrar diferentes expresiones faciales.

Ejemplos.

- Feliz.
- Concentrado.
- Sorprendido.
- Motivado.
- Cansado.
- Triste.

Estas expresiones podrán utilizarse en distintas pantallas del juego.

---

# 10.11 Guardado del Personaje

Toda la información del personaje deberá almacenarse de forma persistente.

Inicialmente se utilizará un archivo JSON con una estructura similar a la siguiente.

```json
{
    "character_id": 1,
    "hair": "short",
    "hair_color": "#1E1E1E",
    "skin": "#D8A46D",
    "eyes": "brown",
    "jersey": "blue",
    "shorts": "white",
    "shoes": "black"
}
```

En futuras versiones esta información podrá almacenarse en una base de datos.

---

# 10.12 Futuras Expansiones

El sistema ha sido diseñado pensando en futuras mejoras.

Entre las funcionalidades previstas se encuentran:

- Más peinados.
- Más uniformes.
- Objetos desbloqueables.
- Tienda de cosméticos.
- Pase de temporada.
- Equipamiento especial.
- Celebraciones personalizadas.
- Animaciones premium.
- Mascotas.
- Fondos de perfil.

Todas estas características deberán poder incorporarse sin modificar la arquitectura base.

---

# 10.13 Relación con el Perfil del Jugador

Cada personaje estará asociado a un único perfil.

Un perfil podrá contener:

- Información personal.
- Configuración.
- Estadísticas.
- Historial de entrenamientos.
- Logros.
- Avatar personalizado.

El editor de personajes será únicamente uno de los módulos que compondrán el perfil completo del usuario.

---

# 10.14 Experiencia del Usuario

El editor deberá ser intuitivo y agradable de utilizar.

Todas las modificaciones deberán mostrarse en tiempo real.

El jugador deberá poder:

- Rotar el personaje.
- Acercar o alejar la cámara.
- Cambiar rápidamente entre categorías.
- Deshacer cambios antes de guardar.
- Restaurar la apariencia predeterminada.

La navegación deberá requerir el menor número posible de clics.

---

# 10.15 Objetivo Final

El sistema de personalización deberá convertirse en uno de los elementos distintivos de VJC Hoops AI.

Aunque la función principal del proyecto es el análisis deportivo mediante Inteligencia Artificial, la posibilidad de crear un avatar propio fortalecerá el vínculo del jugador con la plataforma y aumentará la motivación para continuar entrenando.

El diseño del sistema deberá permitir crecer durante años sin necesidad de rediseñar su arquitectura, incorporando nuevos elementos cosméticos, animaciones y opciones de personalización de forma modular.

---

# 11. Sistema de Entrenamientos

## 11.1 Introducción

El sistema de entrenamientos constituye el núcleo de la experiencia de VJC Hoops AI.

Su propósito es transformar una sesión tradicional de práctica de baloncesto en una experiencia interactiva, motivadora y basada en datos objetivos obtenidos mediante Inteligencia Artificial.

Cada entrenamiento deberá registrar información detallada sobre el rendimiento del jugador y convertirla en métricas fáciles de comprender.

El sistema deberá ser flexible para permitir la incorporación de nuevos modos de entrenamiento sin modificar la arquitectura existente.

---

# 11.2 Objetivos del Sistema

El sistema de entrenamientos deberá cumplir los siguientes objetivos.

- Guiar al jugador durante sus sesiones.
- Registrar automáticamente todos los lanzamientos.
- Analizar la técnica mediante IA.
- Proporcionar retroalimentación inmediata.
- Guardar el historial completo de cada sesión.
- Motivar la mejora continua mediante retos y objetivos.

---

# 11.3 Filosofía del Entrenamiento

Cada entrenamiento deberá enfocarse en el aprendizaje y la mejora del jugador.

El sistema nunca deberá penalizar al usuario por fallar.

La información mostrada deberá utilizarse para identificar oportunidades de mejora y no únicamente para indicar errores.

El objetivo es convertir la práctica en un proceso de aprendizaje continuo.

---

# 11.4 Flujo General

El flujo esperado será el siguiente.

```
Seleccionar entrenamiento

↓

Configurar sesión

↓

Inicializar cámara

↓

Cargar modelos IA

↓

Detectar jugador

↓

Esperar inicio

↓

Analizar cada lanzamiento

↓

Calcular estadísticas

↓

Mostrar resultados

↓

Guardar sesión

↓

Actualizar progreso
```

Todo este proceso deberá ejecutarse de forma automática.

---

# 11.5 Tipos de Entrenamiento

El sistema deberá soportar diferentes modalidades.

Inicialmente se contemplan las siguientes.

### Tiros Libres

Entrenamiento centrado en la precisión desde la línea de tiros libres.

---

### Media Distancia

Entrenamiento desde diferentes posiciones dentro de la línea de tres puntos.

---

### Triple

Entrenamiento especializado en lanzamientos de larga distancia.

---

### Entrenamiento Libre

El jugador podrá lanzar desde cualquier posición sin restricciones.

---

### Desafío Diario

Cada día el sistema propondrá un objetivo diferente.

Ejemplos.

- Anotar 20 tiros consecutivos.
- Alcanzar un 80% de efectividad.
- Completar una sesión en menos de cierto tiempo.

---

### Entrenamiento Personalizado

El jugador podrá definir:

- Número de tiros.
- Tiempo límite.
- Zona de lanzamiento.
- Objetivos personales.

---

# 11.6 Configuración de una Sesión

Antes de iniciar un entrenamiento el usuario podrá configurar.

- Tipo de entrenamiento.
- Número objetivo de lanzamientos.
- Tiempo máximo.
- Cámara utilizada.
- Resolución.
- Nivel de dificultad (si aplica).
- Opciones de asistencia.

Toda esta información quedará registrada junto con la sesión.

---

# 11.7 Desarrollo de la Sesión

Una vez iniciada la práctica, el sistema deberá:

- Detectar al jugador.
- Asignar un ID mediante ObjectTracker.
- Detectar el balón.
- Detectar el aro.
- Analizar la pose del jugador.
- Detectar cada lanzamiento.
- Registrar el resultado.

Todo deberá ejecutarse en tiempo real.

---

# 11.8 Retroalimentación en Tiempo Real

Mientras el entrenamiento está activo, el jugador recibirá información como:

- Lanzamientos realizados.
- Lanzamientos anotados.
- Porcentaje de acierto.
- Tiempo transcurrido.
- Estado de la IA.
- FPS del sistema.
- Indicadores visuales de seguimiento.

En versiones futuras podrán añadirse recomendaciones técnicas en tiempo real.

---

# 11.9 Finalización de la Sesión

Al terminar el entrenamiento el sistema generará un resumen completo.

Este incluirá:

- Total de intentos.
- Total de aciertos.
- Porcentaje de efectividad.
- Tiempo total.
- Estadísticas avanzadas.
- Evolución durante la sesión.
- Recomendaciones de mejora.

Toda esta información quedará almacenada para futuras consultas.

---

# 11.10 Integración con el Sistema de Progresión

Cada entrenamiento contribuirá al progreso del jugador.

Ejemplos.

- Experiencia.
- Nivel.
- Logros.
- Desbloqueo de elementos cosméticos.
- Historial de rendimiento.

El entrenamiento será el principal mecanismo para avanzar dentro del juego.

---

# 11.11 Integración con la Inteligencia Artificial

Durante una sesión se utilizarán múltiples módulos del motor de IA.

- CameraService.
- FrameManager.
- PersonDetector.
- ObjectTracker.
- BallDetector.
- RimDetector.
- PoseEstimator.
- ShotDetector.
- StatisticsEngine.

Cada módulo tendrá una responsabilidad específica dentro del pipeline.

---

# 11.12 Escalabilidad

El sistema ha sido diseñado para crecer con nuevas modalidades.

Ejemplos futuros.

- Entrenamientos por equipos.
- Competiciones online.
- Retos semanales.
- Eventos especiales.
- Simulaciones de partido.
- Entrenamientos con entrenador virtual.
- Modos cooperativos.

La incorporación de nuevas modalidades no deberá requerir cambios importantes en la arquitectura.

---

# 11.13 Experiencia del Usuario

El sistema deberá ser sencillo de utilizar incluso para jugadores sin conocimientos técnicos.

Toda la información relevante deberá presentarse de forma clara y visual.

Las configuraciones avanzadas estarán disponibles para usuarios que deseen personalizar sus entrenamientos.

---

# 11.14 Objetivo Final

El sistema de entrenamientos deberá convertirse en el elemento central de VJC Hoops AI.

Cada sesión permitirá al jugador mejorar sus habilidades mientras el motor de Inteligencia Artificial recopila información objetiva sobre su rendimiento.

La combinación de análisis técnico, estadísticas y una experiencia propia de un videojuego hará que entrenar resulte más entretenido, motivador y eficaz.

---

# 12. Dashboard y Centro de Estadísticas

## 12.1 Introducción

El Dashboard será el centro de información de VJC Hoops AI.

Su propósito será transformar todos los datos obtenidos durante los entrenamientos en información clara, visual y fácil de interpretar.

El Dashboard no solo mostrará estadísticas, sino que también permitirá al jugador comprender su evolución, identificar fortalezas, detectar áreas de mejora y mantenerse motivado mediante objetivos y logros.

Toda la información presentada será generada por el motor de Inteligencia Artificial desarrollado en Python y posteriormente visualizada por el cliente desarrollado en Godot.

---

# 12.2 Objetivos del Dashboard

El Dashboard deberá cumplir los siguientes objetivos.

- Mostrar el progreso del jugador.
- Visualizar estadísticas de forma intuitiva.
- Comparar sesiones de entrenamiento.
- Mostrar tendencias a lo largo del tiempo.
- Motivar al jugador mediante objetivos y logros.
- Facilitar la toma de decisiones durante el entrenamiento.

La interfaz deberá ser moderna, rápida y completamente interactiva.

---

# 12.3 Filosofía de Diseño

El Dashboard deberá priorizar la claridad visual.

No se mostrarán grandes cantidades de números sin contexto.

Cada métrica deberá estar acompañada de elementos gráficos que faciliten su interpretación.

El usuario deberá comprender su rendimiento en pocos segundos.

La navegación entre las distintas secciones será sencilla y consistente.

---

# 12.4 Resumen General

Al acceder al Dashboard el jugador visualizará un resumen de su actividad reciente.

Entre los indicadores principales se incluirán.

- Total de entrenamientos.
- Total de lanzamientos.
- Total de aciertos.
- Porcentaje global de efectividad.
- Tiempo total entrenado.
- Nivel actual.
- Experiencia acumulada.
- Último entrenamiento realizado.
- Objetivos pendientes.

Este resumen actuará como una vista rápida del estado general del jugador.

---

# 12.5 Indicadores Principales (KPIs)

El Dashboard mostrará indicadores destacados mediante tarjetas informativas.

Ejemplos.

- Porcentaje de acierto.
- Mejor racha.
- Tiempo promedio por sesión.
- Promedio de tiros anotados.
- Promedio de intentos.
- Total de horas entrenadas.
- Entrenamientos completados esta semana.
- Progreso hacia el siguiente nivel.

Cada tarjeta incluirá iconografía, colores y animaciones suaves para mejorar la experiencia visual.

---

# 12.6 Estadísticas Avanzadas

El sistema ofrecerá estadísticas más detalladas para usuarios que deseen profundizar en su rendimiento.

Ejemplos.

- Ángulo promedio de lanzamiento.
- Velocidad estimada del balón.
- Tiempo de preparación antes del tiro.
- Tiempo entre lanzamientos.
- Consistencia durante la sesión.
- Desviación estándar de la efectividad.
- Evolución del rendimiento durante el entrenamiento.

Estas métricas permitirán analizar la técnica del jugador con mayor precisión.

---

# 12.7 Historial de Entrenamientos

El Dashboard almacenará un historial completo de todas las sesiones realizadas.

Cada registro incluirá.

- Fecha.
- Hora.
- Duración.
- Tipo de entrenamiento.
- Intentos.
- Aciertos.
- Porcentaje.
- Estadísticas avanzadas.
- Recomendaciones de la IA.

El usuario podrá acceder a cualquier sesión anterior para revisar su desempeño.

---

# 12.8 Comparación de Sesiones

El sistema permitirá comparar dos o más entrenamientos.

La comparación podrá realizarse utilizando diferentes métricas.

Ejemplos.

- Efectividad.
- Tiempo.
- Número de tiros.
- Ángulo promedio.
- Velocidad promedio.
- Evolución del rendimiento.

Esta funcionalidad facilitará el seguimiento de la mejora del jugador.

---

# 12.9 Gráficas

El Dashboard incluirá diferentes tipos de gráficas.

Entre ellas.

- Evolución semanal.
- Evolución mensual.
- Evolución anual.
- Porcentaje de aciertos.
- Tiempo de entrenamiento.
- Progreso de experiencia.
- Rendimiento por sesión.

Todas las gráficas deberán ser interactivas y permitir filtrar información.

---

# 12.10 Mapa de Calor

En futuras versiones se incorporará un mapa de calor de la cancha.

Este permitirá visualizar.

- Zonas con mayor porcentaje de acierto.
- Zonas con menor efectividad.
- Frecuencia de lanzamientos.
- Áreas más utilizadas durante los entrenamientos.

Esta información ayudará al jugador a identificar fortalezas y debilidades.

---

# 12.11 Logros y Progreso

El Dashboard mostrará los logros obtenidos por el jugador.

Ejemplos.

- Primer entrenamiento.
- Primer tiro anotado.
- 100 lanzamientos realizados.
- 500 lanzamientos realizados.
- 90% de efectividad.
- 10 entrenamientos consecutivos.

También mostrará el progreso hacia los próximos logros disponibles.

---

# 12.12 Recomendaciones Inteligentes

El sistema incluirá recomendaciones generadas por la Inteligencia Artificial.

Ejemplos.

- Incrementar la práctica desde la línea de tres puntos.
- Mejorar el ángulo de lanzamiento.
- Aumentar la consistencia entre intentos.
- Practicar sesiones más largas.
- Repetir entrenamientos con mejores resultados.

Estas recomendaciones deberán presentarse de forma clara y comprensible.

---

# 12.13 Integración con el Perfil del Jugador

Toda la información mostrada en el Dashboard estará vinculada al perfil del usuario.

El Dashboard obtendrá datos de.

- Historial de entrenamientos.
- Estadísticas globales.
- Logros.
- Nivel.
- Experiencia.
- Configuración.
- Personalización del personaje.

De esta forma cada jugador tendrá un centro de información completamente personalizado.

---

# 12.14 Escalabilidad

El Dashboard ha sido diseñado para admitir futuras ampliaciones.

Entre las funcionalidades previstas se encuentran.

- Rankings globales.
- Comparación con amigos.
- Estadísticas por temporada.
- Estadísticas por posición.
- Torneos.
- Eventos especiales.
- Desafíos comunitarios.
- Integración con dispositivos externos.
- Exportación de informes en PDF.
- Sincronización con la nube.

Todas estas funciones podrán añadirse sin modificar la arquitectura principal.

---

# 12.15 Objetivo Final

El Dashboard deberá convertirse en el principal centro de análisis deportivo de VJC Hoops AI.

Más que una pantalla de estadísticas, será una herramienta inteligente que permitirá al jugador comprender su evolución, mantenerse motivado y tomar decisiones para mejorar su rendimiento.

La combinación de visualizaciones modernas, métricas avanzadas e inteligencia artificial convertirá el Dashboard en uno de los elementos más importantes y diferenciadores del proyecto.


---

# 13. Perfil del Jugador y Sistema de Progresión

## 13.1 Introducción

El perfil del jugador representa el centro de identidad dentro de VJC Hoops AI.

Su propósito es almacenar toda la información relacionada con el usuario, su progreso, sus logros, estadísticas históricas y elementos personalizados.

El perfil será persistente y acompañará al jugador durante toda su experiencia dentro de la plataforma.

No será únicamente una ficha de información personal, sino un sistema completo de progresión que recompensará la constancia y el esfuerzo realizado durante los entrenamientos.

---

# 13.2 Objetivos del Perfil

El perfil deberá cumplir los siguientes objetivos.

- Identificar al jugador.
- Almacenar el progreso.
- Registrar el historial de entrenamientos.
- Mostrar estadísticas globales.
- Gestionar niveles y experiencia.
- Administrar logros.
- Mantener la configuración personalizada.
- Almacenar la apariencia del personaje.

El perfil será el punto central desde donde se accederá a toda la información del usuario.

---

# 13.3 Información del Jugador

Cada perfil contendrá información básica.

Campos previstos.

- ID único.
- Nombre.
- Nombre de usuario.
- Fecha de creación.
- País.
- Idioma.
- Fotografía o avatar.
- Personaje seleccionado.
- Última conexión.

Toda esta información deberá almacenarse de forma persistente.

---

# 13.4 Sistema de Experiencia (XP)

El progreso del jugador estará basado en puntos de experiencia.

La experiencia se obtendrá mediante acciones como.

- Completar entrenamientos.
- Alcanzar objetivos.
- Desbloquear logros.
- Mantener rachas.
- Participar en eventos.
- Completar desafíos diarios.

Cada acción otorgará una cantidad determinada de experiencia.

La fórmula podrá ajustarse conforme evolucione el proyecto.

---

# 13.5 Sistema de Niveles

El jugador aumentará de nivel conforme acumule experiencia.

Cada nivel representará el tiempo y la dedicación invertidos en el entrenamiento.

Los niveles no modificarán el rendimiento de la IA.

Su función será motivar al jugador y desbloquear contenido visual.

Ejemplo.

Nivel 1

↓

Nivel 2

↓

Nivel 3

↓

...

↓

Nivel 100

En futuras versiones podrán añadirse niveles ilimitados.

---

# 13.6 Sistema de Logros

Los logros reconocerán hitos importantes alcanzados por el jugador.

Ejemplos.

- Primer entrenamiento.
- Primer tiro anotado.
- 100 tiros realizados.
- 1,000 tiros realizados.
- 90% de efectividad.
- 30 días consecutivos entrenando.
- Primer entrenamiento perfecto.

Cada logro incluirá.

- Nombre.
- Descripción.
- Fecha de desbloqueo.
- Icono.
- Recompensa asociada.

---

# 13.7 Rachas de Entrenamiento

El sistema registrará la constancia del jugador.

Ejemplos.

- Días consecutivos entrenando.
- Semanas activas.
- Meses consecutivos.
- Mejor racha histórica.

Las rachas servirán para incentivar el hábito de entrenamiento.

---

# 13.8 Objetivos Diarios y Semanales

El sistema propondrá objetivos periódicos.

Ejemplos diarios.

- Completar una sesión.
- Realizar 50 lanzamientos.
- Alcanzar un 75% de efectividad.

Ejemplos semanales.

- Entrenar cinco días.
- Superar 500 lanzamientos.
- Mejorar el porcentaje de acierto.

El cumplimiento de estos objetivos otorgará experiencia y recompensas.

---

# 13.9 Recompensas

El progreso permitirá desbloquear contenido visual.

Ejemplos.

- Uniformes.
- Balones.
- Animaciones.
- Fondos.
- Insignias.
- Marcos para el perfil.
- Títulos.
- Accesorios.

Todas las recompensas serán cosméticas.

Nunca modificarán el rendimiento del análisis deportivo.

---

# 13.10 Estadísticas Globales

El perfil mostrará un resumen histórico del jugador.

Ejemplos.

- Total de entrenamientos.
- Total de lanzamientos.
- Total de aciertos.
- Porcentaje histórico.
- Tiempo total entrenado.
- Mejor sesión.
- Mayor racha.
- Último entrenamiento.

Estas estadísticas estarán siempre disponibles desde el perfil.

---

# 13.11 Historial

El jugador podrá consultar todas sus sesiones anteriores.

Cada entrenamiento almacenará.

- Fecha.
- Duración.
- Tipo.
- Resultados.
- Estadísticas.
- Recomendaciones.

Esto permitirá revisar la evolución a lo largo del tiempo.

---

# 13.12 Integración con el Dashboard

Toda la información del perfil estará conectada con el Dashboard.

El Dashboard utilizará el perfil para mostrar.

- Progreso.
- Niveles.
- Logros.
- Estadísticas.
- Objetivos.
- Rachas.

Ambos sistemas compartirán la misma fuente de datos.

---

# 13.13 Sincronización Futura

En versiones posteriores el perfil podrá sincronizarse con servicios en la nube.

Esto permitirá.

- Recuperar información desde distintos dispositivos.
- Respaldar automáticamente los datos.
- Compartir estadísticas.
- Participar en rankings globales.
- Competir con otros jugadores.

La arquitectura deberá permitir esta expansión sin modificar los módulos actuales.

---

# 13.14 Seguridad

Toda la información del jugador deberá almacenarse de forma segura.

Se evitará la pérdida de datos mediante copias de seguridad y mecanismos de recuperación.

Las futuras implementaciones con servicios en línea deberán proteger la privacidad del usuario y utilizar conexiones seguras.

---

# 13.15 Objetivo Final

El perfil del jugador deberá convertirse en el centro de toda la experiencia de VJC Hoops AI.

No será únicamente una pantalla con información, sino un sistema que refleje el esfuerzo, la evolución y los logros obtenidos por el usuario a lo largo del tiempo.

El objetivo es motivar al jugador a regresar constantemente, seguir entrenando y observar cómo mejora gracias a la combinación de práctica e Inteligencia Artificial.


---

# 14. Sistema de Configuración y Accesibilidad

## 14.1 Introducción

El sistema de configuración será el encargado de adaptar VJC Hoops AI a las preferencias, necesidades y características del dispositivo de cada usuario.

Su objetivo no será únicamente modificar opciones visuales, sino proporcionar una experiencia completamente personalizable, accesible y preparada para futuras expansiones.

Toda configuración deberá almacenarse de forma persistente y aplicarse automáticamente cada vez que el usuario inicie sesión.

---

# 14.2 Objetivos

El sistema deberá cumplir los siguientes objetivos.

- Permitir personalizar la experiencia del usuario.
- Mejorar la accesibilidad.
- Adaptarse a distintos equipos.
- Configurar la Inteligencia Artificial.
- Configurar la cámara.
- Configurar la interfaz.
- Configurar audio.
- Configurar idioma.
- Facilitar futuras ampliaciones.

---

# 14.3 Filosofía del Sistema

La configuración nunca deberá modificar el funcionamiento interno de la Inteligencia Artificial.

Su responsabilidad será modificar únicamente la experiencia del usuario.

Todas las opciones deberán ser fáciles de entender.

Nunca se mostrarán configuraciones técnicas innecesarias para usuarios principiantes.

Las opciones avanzadas estarán agrupadas en una sección específica.

---

# 14.4 Organización General

La pantalla de configuración estará dividida en módulos independientes.

Configuración

├── General

├── Perfil

├── Video

├── Audio

├── Cámara

├── Inteligencia Artificial

├── Interfaz

├── Accesibilidad

├── Notificaciones

├── Idioma

├── Datos

└── Acerca de

Cada módulo podrá evolucionar sin afectar al resto.

---

# 14.5 Configuración General

Permitirá modificar aspectos básicos del sistema.

Opciones previstas.

- Nombre del jugador.
- Idioma.
- Región.
- Formato de fecha.
- Formato de hora.
- Inicio automático.
- Confirmaciones.

---

# 14.6 Configuración de Video

Permitirá adaptar la aplicación al hardware del usuario.

Opciones previstas.

- Resolución.
- Pantalla completa.
- Modo ventana.
- FPS máximo.
- Escalado.
- Calidad gráfica.
- Sincronización vertical.
- Renderizado.

Estas opciones serán gestionadas por Godot.

---

# 14.7 Configuración de Audio

El jugador podrá controlar todos los sonidos del juego.

Opciones.

- Volumen general.
- Música.
- Efectos.
- Voz.
- Notificaciones.
- Ambiente.

Cada categoría tendrá su propio control independiente.

---

# 14.8 Configuración de Cámara

La cámara será uno de los elementos más importantes del proyecto.

El sistema permitirá configurar.

- Cámara utilizada.
- Resolución.
- FPS.
- Brillo.
- Contraste.
- Exposición.
- Espejo horizontal.
- Rotación.
- Recorte.

También se mostrará una vista previa en tiempo real para facilitar la configuración.

---

# 14.9 Configuración de Inteligencia Artificial

El usuario podrá ajustar algunos parámetros del motor de IA sin modificar el código.

Opciones previstas.

- Nivel de confianza del detector.
- Resolución del modelo.
- Mostrar bounding boxes.
- Mostrar IDs.
- Mostrar FPS.
- Mostrar información de depuración.
- Activar modo desarrollador.

Las opciones avanzadas estarán ocultas por defecto.

---

# 14.10 Configuración de la Interfaz

Permitirá personalizar el aspecto visual del cliente.

Opciones previstas.

- Tema claro.
- Tema oscuro.
- Tema automático.
- Escala de la interfaz.
- Tamaño del texto.
- Animaciones.
- Transparencias.
- Colores de acento.

Estas opciones modificarán únicamente el cliente desarrollado en Godot.

---

# 14.11 Accesibilidad

La accesibilidad será una prioridad del proyecto.

Opciones previstas.

- Texto grande.
- Alto contraste.
- Modo para daltónicos.
- Navegación mediante teclado.
- Navegación mediante control.
- Subtítulos.
- Indicadores visuales.
- Reducción de animaciones.

El objetivo es permitir que la aplicación pueda ser utilizada por la mayor cantidad posible de personas.

---

# 14.12 Idiomas

El sistema será completamente internacionalizable.

Idiomas previstos.

- Español.
- Inglés.

En futuras versiones podrán añadirse nuevos idiomas sin modificar el código existente.

Todo el texto visible deberá obtenerse desde archivos de traducción.

Nunca deberán existir textos fijos escritos directamente dentro del código.

---

# 14.13 Notificaciones

El usuario podrá configurar recordatorios relacionados con sus entrenamientos.

Ejemplos.

- Recordatorio diario.
- Objetivos semanales.
- Logros desbloqueados.
- Nuevas actualizaciones.
- Eventos especiales.

Todas las notificaciones podrán activarse o desactivarse individualmente.

---

# 14.14 Gestión de Datos

El sistema permitirá administrar la información almacenada.

Opciones previstas.

- Exportar datos.
- Importar datos.
- Crear respaldo.
- Restaurar respaldo.
- Restablecer configuración.
- Eliminar perfil.

Estas funciones facilitarán la migración entre dispositivos y la recuperación ante errores.

---

# 14.15 Acerca de

Esta sección mostrará información técnica del proyecto.

Contenido previsto.

- Nombre del proyecto.
- Versión.
- Versión del motor IA.
- Versión de Godot.
- Licencia.
- Autores.
- Créditos.
- Enlaces oficiales.
- Repositorio GitHub.

También incluirá un botón para comprobar nuevas actualizaciones.

---

# 14.16 Persistencia

Toda configuración deberá almacenarse automáticamente.

Inicialmente se utilizarán archivos JSON.

En futuras versiones podrá emplearse una base de datos o sincronización con la nube.

El usuario nunca deberá perder su configuración al actualizar la aplicación.

---

# 14.17 Objetivo Final

El sistema de configuración deberá ofrecer una experiencia completamente personalizable y accesible.

Cada jugador podrá adaptar VJC Hoops AI a sus preferencias sin afectar el funcionamiento del motor de Inteligencia Artificial.

La arquitectura modular permitirá incorporar nuevas opciones de configuración durante los próximos años sin necesidad de rediseñar el sistema.

---

# 15. Persistencia de Datos y Gestión de Archivos

## 15.1 Introducción

Uno de los pilares fundamentales de VJC Hoops AI será la correcta organización y persistencia de toda la información generada por el sistema.

Cada entrenamiento, estadística, configuración, personaje, logro y archivo generado deberá almacenarse de forma estructurada, consistente y preparada para futuras expansiones.

La gestión de datos no dependerá del motor gráfico ni del motor de Inteligencia Artificial.

Python será responsable de generar información.

Godot será responsable de consumirla y mostrarla al usuario.

Ambos sistemas compartirán una estructura común de almacenamiento.

---

# 15.2 Objetivos

El sistema de persistencia deberá cumplir los siguientes objetivos.

- Evitar pérdida de información.
- Facilitar respaldos.
- Permitir sincronización futura.
- Mantener una organización clara.
- Separar datos del código fuente.
- Facilitar mantenimiento.
- Facilitar migraciones.
- Facilitar depuración.

Toda la información deberá poder localizarse rápidamente.

---

# 15.3 Filosofía

El proyecto nunca deberá almacenar información importante mezclada con el código.

Todos los datos generados por el usuario deberán encontrarse fuera de los módulos de programación.

El código deberá ser independiente de la información producida durante el uso del sistema.

Esta separación permitirá actualizar la aplicación sin afectar el historial del jugador.

---

# 15.4 Organización General

La estructura propuesta será la siguiente.

```
VJC-Hoops-AI/

docs/
src/
tests/
assets/
models/
config/
data/
logs/
exports/
temp/
```

Cada carpeta tendrá una única responsabilidad.

---

# 15.5 Carpeta docs

Contendrá toda la documentación del proyecto.

Ejemplos.

- README.md
- README_EN.md
- PROJECT_CONTEXT.md
- PROJECT_ARCHITECTURE.md
- ROADMAP.md
- Documentación técnica.
- Manuales.
- Diagramas.
- Guías para desarrolladores.

Nunca contendrá datos del usuario.

---

# 15.6 Carpeta src

Contendrá exclusivamente el código fuente.

Ejemplos.

- Motor IA.
- Servicios.
- Casos de uso.
- Infraestructura.
- Dominio.
- Interfaces.

No deberá almacenar configuraciones personales ni archivos temporales.

---

# 15.7 Carpeta assets

Almacenará recursos utilizados por Godot.

Ejemplos.

- Sprites.
- Íconos.
- Botones.
- Fuentes.
- Música.
- Sonidos.
- Animaciones.
- Fondos.
- Personajes.
- Uniformes.

Esta carpeta será utilizada únicamente por el cliente gráfico.

---

# 15.8 Carpeta models

Contendrá todos los modelos de Inteligencia Artificial.

Ejemplos.

- yolov8n.pt
- BallDetector.pt
- RimDetector.pt
- PoseEstimator.pt

Los modelos nunca deberán almacenarse dentro de src.

Además, los modelos grandes deberán excluirse del repositorio mediante `.gitignore` y documentarse para su descarga.

---

# 15.9 Carpeta config

Almacenará la configuración del sistema.

Ejemplos.

- config.json
- camera.json
- ui.json
- ai.json
- language.json

Todas las configuraciones deberán cargarse automáticamente al iniciar la aplicación.

---

# 15.10 Carpeta data

Será la carpeta más importante del sistema.

Aquí se almacenará toda la información generada por el usuario.

Ejemplo.

```
data/

players/
sessions/
statistics/
characters/
achievements/
settings/
backups/
```

Cada módulo utilizará su propio directorio.

---

# 15.11 Carpeta players

Cada jugador tendrá un identificador único.

Ejemplo.

```
players/

000001/

profile.json
character.json
settings.json
```

Esto permitirá soportar múltiples perfiles en el futuro.

---

# 15.12 Carpeta sessions

Cada entrenamiento será almacenado individualmente.

Ejemplo.

```
sessions/

2026/

06/

session_0001.json
session_0002.json
```

Organizar las sesiones por año y mes facilitará búsquedas y respaldos.

---

# 15.13 Carpeta statistics

Contendrá estadísticas consolidadas.

Ejemplos.

- global.json
- weekly.json
- monthly.json
- yearly.json

Estas estadísticas podrán regenerarse si fuera necesario a partir de las sesiones.

---

# 15.14 Carpeta logs

Todos los eventos importantes deberán registrarse.

Ejemplos.

- Inicio del sistema.
- Errores.
- Advertencias.
- Información de depuración.
- Rendimiento.

Los archivos de log facilitarán la resolución de problemas.

---

# 15.15 Carpeta exports

Permitirá generar archivos para compartir.

Ejemplos.

- PDF.
- CSV.
- Excel.
- Imágenes.
- Reportes.

Los usuarios podrán exportar sus resultados para analizarlos o compartirlos.

---

# 15.16 Carpeta temp

Contendrá archivos temporales.

Ejemplos.

- Frames.
- Caché.
- Videos temporales.
- Archivos de procesamiento.

Su contenido podrá eliminarse automáticamente sin afectar la información del usuario.

---

# 15.17 Formato de Archivos

Siempre que sea posible se utilizarán formatos estándar.

Ejemplos.

- JSON.
- PNG.
- JPG.
- MP4.
- CSV.
- PDF.

Se evitarán formatos propietarios que dificulten la interoperabilidad.

---

# 15.18 Copias de Seguridad

El sistema deberá permitir generar respaldos completos.

Cada respaldo incluirá.

- Perfil.
- Personaje.
- Configuración.
- Estadísticas.
- Historial de entrenamientos.
- Logros.

Los respaldos deberán poder restaurarse en cualquier momento.

---

# 15.19 Sincronización Futura

La arquitectura deberá prepararse para integrar almacenamiento en la nube.

Servicios posibles.

- Google Drive.
- OneDrive.
- Dropbox.
- GitHub Releases (para recursos públicos).
- Servidor propio.
- Bases de datos remotas.

La sincronización deberá ser opcional.

---

# 15.20 Compatibilidad

Toda la estructura de archivos deberá funcionar correctamente en.

- Windows.
- Linux.
- macOS.

En futuras versiones también deberá ser adaptable a dispositivos móviles.

Nunca deberán utilizarse rutas absolutas dentro del código.

Siempre se emplearán rutas relativas o mecanismos proporcionados por Godot y Python.

---

# 15.21 Versionado de Datos

Los archivos importantes deberán incluir un número de versión.

Ejemplo.

```json
{
    "version": "1.0.0"
}
```

Esto permitirá realizar migraciones cuando cambie la estructura de los datos.

---

# 15.22 Objetivo Final

El sistema de persistencia deberá garantizar que toda la información generada por VJC Hoops AI permanezca organizada, segura y preparada para crecer durante muchos años.

La correcta separación entre código, recursos, modelos y datos permitirá mantener una arquitectura limpia, escalable y fácilmente comprensible para cualquier desarrollador o Inteligencia Artificial que participe en el proyecto.

---

# 16. Arquitectura de Desarrollo, Convenciones y Reglas para IA

## 16.1 Introducción

El presente capítulo define las reglas oficiales para el desarrollo de VJC Hoops AI.

Su objetivo es garantizar que cualquier desarrollador o Inteligencia Artificial pueda colaborar en el proyecto manteniendo la misma calidad, organización y filosofía de diseño.

Estas reglas deberán considerarse obligatorias para cualquier modificación realizada en el repositorio.

No importa quién escriba el código.

Todo el proyecto deberá parecer desarrollado por un único equipo siguiendo un mismo estándar.

---

# 16.2 Filosofía General

VJC Hoops AI no es un proyecto experimental.

Su objetivo es convertirse en una plataforma profesional de entrenamiento deportivo basada en Inteligencia Artificial.

Por esta razón todas las decisiones deberán priorizar:

- Claridad.
- Escalabilidad.
- Mantenibilidad.
- Modularidad.
- Bajo acoplamiento.
- Alta cohesión.
- Código limpio.
- Documentación.

Nunca deberá priorizarse escribir código rápido sobre escribir código mantenible.

---

# 16.3 Arquitectura Oficial

Toda la aplicación utilizará Arquitectura Hexagonal (Ports and Adapters).

Las capas principales serán.

```
Domain

↓

Application

↓

Infrastructure

↓

Presentation
```

Cada capa tendrá responsabilidades claramente definidas.

Nunca deberán mezclarse responsabilidades entre capas.

---

# 16.4 Responsabilidad de Cada Capa

### Domain

Contendrá únicamente reglas de negocio.

No conocerá:

- OpenCV.
- YOLO.
- Godot.
- JSON.
- Archivos.
- Interfaces gráficas.

Será completamente independiente de cualquier tecnología.

---

### Application

Coordinará los casos de uso.

Ejemplos.

- Iniciar entrenamiento.
- Analizar sesión.
- Guardar estadísticas.
- Exportar resultados.

No contendrá lógica de infraestructura.

---

### Infrastructure

Implementará los adaptadores externos.

Ejemplos.

- Cámara.
- OpenCV.
- YOLO.
- Archivos.
- Base de datos.
- API.
- WebSockets.

Toda dependencia externa deberá vivir aquí.

---

### Presentation

Representará la interfaz.

Inicialmente será:

Godot.

En el futuro podrán existir otros clientes.

- Web.
- Android.
- iOS.
- Consolas.

---

# 16.5 Organización de Carpetas

Toda nueva funcionalidad deberá respetar la estructura oficial.

Ejemplo.

```
src/

domain/

application/

infrastructure/

presentation/
```

Nunca deberán crearse carpetas arbitrarias.

---

# 16.6 Convenciones de Nombres

Archivos Python.

snake_case

Ejemplo.

```
person_detector.py
```

Clases.

PascalCase

Ejemplo.

```
PersonDetector
```

Funciones.

snake_case

Variables.

snake_case

Constantes.

UPPER_CASE

---

# 16.7 Principios SOLID

Todo desarrollo deberá respetar los principios SOLID.

Especialmente.

- Single Responsibility.
- Open / Closed.
- Dependency Inversion.

Cada clase deberá tener una única responsabilidad.

---

# 16.8 Dependencias

Toda nueva dependencia deberá justificarse.

Antes de instalar una librería deberá responderse.

¿Existe una alternativa utilizando las dependencias actuales?

Si la respuesta es sí, deberá evitarse instalar nuevas librerías.

---

# 16.9 Calidad del Código

Todo código deberá ser.

- Legible.
- Reutilizable.
- Documentado.
- Probado.
- Fácil de extender.

Nunca deberán escribirse funciones extremadamente largas.

Como referencia.

Más de 50 líneas normalmente indica que una función debe dividirse.

---

# 16.10 Testing

Toda funcionalidad nueva deberá incluir pruebas.

Tipos previstos.

- Unit Tests.
- Integration Tests.
- Future End-to-End Tests.

Nunca deberá aceptarse una funcionalidad sin pruebas cuando sea razonablemente posible implementarlas.

---

# 16.11 Documentación

Cada módulo importante deberá contar con documentación.

Ejemplos.

- CameraService.
- PersonDetector.
- ObjectTracker.
- BallDetector.
- StatisticsEngine.

La documentación deberá actualizarse cuando cambie el comportamiento del código.

---

# 16.12 Reglas para Inteligencias Artificiales

Cualquier IA que participe en el proyecto deberá seguir estas reglas.

Antes de modificar código deberá comprender la arquitectura existente.

Nunca deberá romper la Arquitectura Hexagonal.

Nunca deberá duplicar código existente.

Siempre deberá reutilizar componentes.

Siempre deberá consultar PROJECT_CONTEXT.md antes de realizar cambios importantes.

Toda nueva funcionalidad deberá integrarse respetando la arquitectura existente.

La IA nunca deberá reemplazar módulos completos cuando únicamente sea necesario ampliarlos.

---

# 16.13 Reglas para Commits

Cada commit deberá representar una unidad lógica de trabajo.

Ejemplos.

Correcto.

Sprint 6: Ball Detector

Sprint 7: Rim Detection

Incorrecto.

Cambios varios

Update

Fix

Los mensajes deberán describir claramente el objetivo del commit.

---

# 16.14 Estrategia de Git

Se utilizará Git como sistema oficial de control de versiones.

Las ramas previstas serán.

```
main

develop

feature/*

hotfix/*
```

La rama main siempre deberá permanecer estable.

Las nuevas funcionalidades deberán desarrollarse en ramas feature.

---

# 16.15 Convenciones de Documentación

Todo documento importante deberá escribirse utilizando Markdown.

Los documentos principales serán.

README.md

README_EN.md

PROJECT_CONTEXT.md

PROJECT_ARCHITECTURE.md

ROADMAP.md

CHANGELOG.md

Cada documento tendrá una responsabilidad específica.

---

# 16.16 Manejo de Errores

Toda excepción deberá gestionarse adecuadamente.

Nunca deberán ocultarse errores importantes.

Siempre deberán registrarse en los archivos de log.

Cuando sea posible se mostrarán mensajes comprensibles para el usuario.

---

# 16.17 Optimización

La optimización deberá realizarse únicamente cuando sea necesaria.

Primero deberá existir un sistema funcional.

Después se optimizará.

Nunca deberá sacrificarse la legibilidad por microoptimizaciones innecesarias.

---

# 16.18 Compatibilidad

Todo desarrollo deberá considerar.

- Windows.
- Linux.
- macOS.

El código deberá ser portable.

Nunca deberán utilizarse rutas absolutas.

---

# 16.19 Escalabilidad

Cada módulo deberá diseñarse pensando en futuras ampliaciones.

Ejemplos.

Hoy.

PersonDetector

Mañana.

PersonDetector

BallDetector

RimDetector

PoseEstimator

StatisticsEngine

La arquitectura deberá permitir añadir nuevos módulos sin modificar los existentes.

---

# 16.20 Principio Más Importante del Proyecto

Toda decisión técnica deberá responder primero a esta pregunta.

"¿Esta solución permitirá que el proyecto siga creciendo durante los próximos cinco años?"

Si la respuesta es no, deberá buscarse una alternativa mejor.

El objetivo no es terminar el proyecto rápidamente.

El objetivo es construir una plataforma profesional, mantenible y preparada para evolucionar durante muchos años.

---

---

# 17. Manual Oficial para Inteligencias Artificiales (AI Development Guide)

## 17.1 Introducción

VJC Hoops AI ha sido diseñado para ser desarrollado de forma colaborativa entre desarrolladores humanos e Inteligencias Artificiales.

Este documento establece las reglas oficiales que deberá seguir cualquier IA que participe en el desarrollo del proyecto.

El objetivo es garantizar la continuidad del desarrollo, mantener una arquitectura consistente y evitar modificaciones que comprometan la estabilidad del sistema.

Toda IA deberá considerar este documento como una guía obligatoria antes de realizar cualquier cambio.

---

# 17.2 Objetivos

El propósito de este manual es garantizar que cualquier IA pueda:

- Comprender rápidamente el proyecto.
- Identificar la arquitectura existente.
- Respetar las decisiones de diseño.
- Continuar el desarrollo sin perder contexto.
- Mantener la calidad del código.
- Evitar duplicación de funcionalidades.
- Facilitar la colaboración con otros desarrolladores.

---

# 17.3 Documentos que deben leerse primero

Antes de modificar cualquier archivo, la IA deberá revisar los siguientes documentos en este orden.

1. README.md
2. PROJECT_CONTEXT.md
3. PROJECT_ARCHITECTURE.md
4. ROADMAP.md
5. CHANGELOG.md (cuando exista)

Estos documentos contienen el contexto general del proyecto.

Nunca deberán ignorarse.

---

# 17.4 Comprender antes de modificar

La IA nunca deberá comenzar a escribir código inmediatamente.

Antes deberá:

- Analizar la estructura del proyecto.
- Identificar la capa correspondiente.
- Revisar módulos similares.
- Comprender el flujo existente.
- Confirmar que no existe una implementación previa.

Solo después podrá comenzar a desarrollar.

---

# 17.5 Principio de No Duplicación

Antes de crear una nueva clase o función la IA deberá comprobar si ya existe una implementación equivalente.

Nunca deberán duplicarse funcionalidades.

Si un componente ya realiza una tarea determinada deberá ampliarse o reutilizarse en lugar de crear uno nuevo.

---

# 17.6 Arquitectura Obligatoria

Toda modificación deberá respetar la Arquitectura Hexagonal definida para el proyecto.

Las responsabilidades estarán separadas en:

Domain

↓

Application

↓

Infrastructure

↓

Presentation

La IA nunca deberá mezclar responsabilidades entre capas.

---

# 17.7 Principios de Desarrollo

Todo código generado deberá cumplir los siguientes principios.

- Modularidad.
- Escalabilidad.
- Bajo acoplamiento.
- Alta cohesión.
- Código limpio.
- Reutilización.
- Legibilidad.
- Simplicidad.

Las soluciones complejas solo deberán utilizarse cuando aporten un beneficio claro.

---

# 17.8 Reglas para Nuevos Módulos

Cuando se incorpore una nueva funcionalidad, la IA deberá:

- Crear la estructura correspondiente.
- Añadir documentación.
- Escribir pruebas.
- Integrar el módulo sin romper el sistema existente.
- Actualizar el README cuando sea necesario.
- Actualizar PROJECT_CONTEXT.md si cambia la arquitectura.

Toda funcionalidad nueva deberá quedar documentada.

---

# 17.9 Validación Antes de Finalizar

Antes de considerar terminado un cambio, la IA deberá verificar:

- El proyecto compila correctamente.
- Las pruebas existentes continúan funcionando.
- Las nuevas pruebas pasan correctamente.
- No existen imports innecesarios.
- No existen archivos temporales.
- No existen modelos grandes añadidos accidentalmente al repositorio.
- La documentación está actualizada.

---

# 17.10 Uso Responsable de Dependencias

Antes de instalar una nueva biblioteca deberá responderse la siguiente pregunta.

¿Puede resolverse el problema utilizando las dependencias existentes?

Si la respuesta es sí, deberá evitarse añadir nuevas librerías.

Cada nueva dependencia incrementa el coste de mantenimiento del proyecto.

---

# 17.11 Comunicación con el Usuario

Cuando una IA proponga cambios importantes deberá explicar:

- Qué se modificará.
- Por qué es necesario.
- Qué archivos serán afectados.
- Qué impacto tendrá sobre el resto del sistema.
- Cómo se validará el resultado.

El usuario siempre deberá comprender el motivo de las modificaciones importantes.

---

# 17.12 Protección del Proyecto

La IA nunca deberá realizar acciones potencialmente destructivas sin autorización explícita del usuario.

Ejemplos.

- Eliminar carpetas completas.
- Reemplazar módulos funcionales.
- Reescribir grandes cantidades de código.
- Borrar historial.
- Eliminar documentación.
- Modificar configuraciones críticas.

Cuando exista duda, la IA deberá solicitar confirmación.

---

# 17.13 Gestión del Contexto

Si la conversación se reinicia o cambia de modelo, la IA deberá reconstruir el contexto utilizando la documentación oficial del proyecto.

No deberá asumir información que no esté documentada.

La documentación será siempre la fuente de verdad.

---

# 17.14 Preparación para el Futuro

El proyecto está diseñado para evolucionar durante varios años.

Por este motivo, la IA deberá diseñar soluciones pensando en futuras ampliaciones.

Cada nuevo módulo deberá poder extenderse sin modificar significativamente los componentes existentes.

---

# 17.15 Filosofía de Colaboración

Las Inteligencias Artificiales no sustituyen a los desarrolladores humanos.

Su función es acelerar el desarrollo, reducir tareas repetitivas y proponer soluciones técnicas.

Las decisiones finales siempre corresponderán al propietario del proyecto.

La IA deberá actuar como una herramienta de apoyo y respetar las preferencias y objetivos definidos para VJC Hoops AI.

---

# 17.16 Objetivo Final

El propósito de este manual es garantizar que cualquier Inteligencia Artificial pueda incorporarse al desarrollo de VJC Hoops AI en cualquier momento, comprendiendo rápidamente la arquitectura, las reglas del proyecto y la visión a largo plazo.

Gracias a este documento, el proyecto podrá mantenerse consistente incluso cuando cambien las herramientas, los modelos de IA o los desarrolladores involucrados.

---

---

# 18. Estrategia de Calidad, Testing y Seguridad

## 18.1 Introducción

La calidad del software será uno de los pilares fundamentales de VJC Hoops AI.

El objetivo no es únicamente desarrollar nuevas funcionalidades, sino garantizar que cada módulo funcione correctamente, sea estable, esté correctamente documentado y pueda mantenerse durante muchos años.

Todo cambio incorporado al proyecto deberá ser verificable, reproducible y compatible con la arquitectura definida en este documento.

La calidad será responsabilidad de todo el equipo de desarrollo, incluyendo desarrolladores humanos e Inteligencias Artificiales.

---

# 18.2 Objetivos

La estrategia de calidad deberá garantizar los siguientes objetivos.

- Evitar regresiones.
- Detectar errores tempranamente.
- Mantener una arquitectura estable.
- Validar el comportamiento de cada módulo.
- Garantizar la compatibilidad entre Python y Godot.
- Facilitar el mantenimiento.
- Permitir futuras ampliaciones sin romper el sistema.

---

# 18.3 Filosofía de Calidad

La calidad no deberá depender únicamente de las pruebas automáticas.

Antes de incorporar cualquier cambio deberá verificarse.

- El diseño.
- La arquitectura.
- El código.
- La documentación.
- El rendimiento.
- La experiencia del usuario.

Un módulo técnicamente correcto pero difícil de mantener también será considerado un problema de calidad.

---

# 18.4 Estrategia General de Testing

El proyecto utilizará varios niveles de pruebas.

```
Unit Tests

↓

Integration Tests

↓

System Tests

↓

Manual Tests

↓

Acceptance Tests
```

Cada nivel verificará un aspecto distinto del sistema.

---

# 18.5 Unit Tests

Los Unit Tests comprobarán el comportamiento individual de cada clase.

Ejemplos.

- CameraService.
- PersonDetector.
- ObjectTracker.
- BallDetector.
- RimDetector.
- PoseEstimator.
- StatisticsEngine.

Cada clase deberá probarse de forma aislada.

No deberán depender de recursos externos siempre que sea posible.

---

# 18.6 Integration Tests

Las pruebas de integración verificarán la comunicación entre módulos.

Ejemplos.

CameraService

↓

FrameManager

↓

PersonDetector

↓

ObjectTracker

↓

StatisticsEngine

El objetivo será comprobar que el pipeline completo funciona correctamente.

---

# 18.7 System Tests

Los System Tests comprobarán el funcionamiento de la aplicación completa.

Ejemplos.

- Inicio del sistema.
- Carga de modelos.
- Apertura de cámara.
- Ejecución de una sesión.
- Guardado de resultados.
- Cierre correcto.

Estas pruebas validarán el comportamiento global del proyecto.

---

# 18.8 Pruebas Manuales

Algunas funcionalidades requerirán validación manual.

Ejemplos.

- Calidad de la interfaz.
- Fluidez de animaciones.
- Experiencia del usuario.
- Diseño visual.
- Navegación.
- Configuración.
- Accesibilidad.

Estas pruebas serán especialmente importantes durante el desarrollo del cliente en Godot.

---

# 18.9 Validación de la Inteligencia Artificial

Cada modelo de IA deberá evaluarse utilizando métricas objetivas.

Ejemplos.

- Precisión.
- Recall.
- F1 Score.
- Tiempo de inferencia.
- FPS promedio.
- Uso de memoria.
- Consumo de CPU.
- Consumo de GPU.

Los resultados deberán documentarse para facilitar comparaciones entre versiones.

---

# 18.10 Rendimiento

El sistema deberá mantener un rendimiento adecuado para el análisis en tiempo real.

Objetivos iniciales.

- Procesamiento estable.
- Baja latencia.
- Uso eficiente de memoria.
- Consumo moderado de CPU.
- Aprovechamiento de GPU cuando esté disponible.

Las optimizaciones deberán realizarse únicamente después de disponer de un sistema funcional.

---

# 18.11 Seguridad

La seguridad deberá considerarse desde las primeras etapas del desarrollo.

Principios generales.

- No almacenar contraseñas en texto plano.
- No exponer claves de API.
- No incluir archivos sensibles en Git.
- Utilizar `.gitignore` correctamente.
- Validar toda información recibida del usuario.
- Evitar rutas absolutas.

En futuras versiones se añadirán mecanismos de autenticación y cifrado cuando exista sincronización en la nube.

---

# 18.12 Gestión de Errores

Todos los errores deberán gestionarse adecuadamente.

Nunca deberán ignorarse excepciones importantes.

Cada error deberá.

- Registrarse.
- Mostrar un mensaje comprensible cuando corresponda.
- Permitir el diagnóstico del problema.

El objetivo será facilitar el mantenimiento y la resolución de incidencias.

---

# 18.13 Revisión de Código

Antes de aceptar un cambio importante deberá verificarse.

- Claridad del código.
- Arquitectura.
- Nombres de variables.
- Comentarios innecesarios.
- Documentación.
- Cobertura de pruebas.
- Compatibilidad con el resto del proyecto.

Cuando participe una IA, el propietario del proyecto deberá revisar las modificaciones antes de integrarlas definitivamente.

---

# 18.14 Checklist de Finalización de un Sprint

Un Sprint solo podrá considerarse finalizado cuando se cumplan todos los siguientes puntos.

- Funcionalidad implementada.
- Código limpio.
- Arquitectura respetada.
- Pruebas completadas.
- Documentación actualizada.
- README actualizado si corresponde.
- PROJECT_CONTEXT.md actualizado si cambia la arquitectura.
- ROADMAP actualizado.
- Sin archivos temporales.
- Sin modelos grandes añadidos accidentalmente.
- Commit correctamente documentado.

---

# 18.15 Métricas de Calidad

A medida que el proyecto evolucione se monitorizarán indicadores como.

- Número de pruebas.
- Cobertura aproximada.
- Tiempo medio de ejecución.
- Tiempo medio de inferencia.
- FPS promedio.
- Uso de memoria.
- Tiempo de carga.
- Número de incidencias corregidas.

Estas métricas permitirán medir la evolución del proyecto.

---

# 18.16 Calidad de la Documentación

La documentación tendrá el mismo nivel de importancia que el código.

Toda nueva funcionalidad deberá incluir.

- Explicación técnica.
- Ejemplos de uso.
- Cambios en la arquitectura.
- Actualización del Roadmap cuando corresponda.

La documentación deberá mantenerse sincronizada con el estado real del proyecto.

---

# 18.17 Compatibilidad

Antes de publicar una versión importante deberán verificarse.

- Compatibilidad con Windows.
- Compatibilidad con Linux.
- Compatibilidad con macOS.

En futuras versiones también se evaluará la compatibilidad con dispositivos móviles.

---

# 18.18 Preparación para Producción

Antes de una versión estable se realizarán pruebas completas.

Entre ellas.

- Pruebas prolongadas de entrenamiento.
- Validación de precisión de la IA.
- Validación del guardado de datos.
- Validación del rendimiento.
- Validación de la interfaz.
- Validación de recuperación ante errores.

Solo después de superar estas verificaciones se considerará que una versión está lista para producción.

---

# 18.19 Objetivo Final

La estrategia de calidad tiene como propósito garantizar que VJC Hoops AI evolucione como una plataforma profesional, estable y mantenible.

Cada nueva funcionalidad deberá aportar valor sin comprometer el rendimiento, la arquitectura o la experiencia del usuario.

La combinación de pruebas automáticas, revisiones de código, documentación y validación continua permitirá construir un proyecto preparado para crecer durante muchos años.

---

---

# 19. Roadmap Técnico Oficial

## 19.1 Introducción

El presente Roadmap define el orden oficial de desarrollo de VJC Hoops AI.

Cada Sprint representa una unidad funcional del proyecto y deberá completarse antes de avanzar al siguiente, salvo que existan dependencias que justifiquen un cambio en la planificación.

El objetivo del Roadmap es proporcionar una visión clara del estado actual del proyecto, facilitar la coordinación entre desarrolladores humanos e Inteligencias Artificiales y mantener un crecimiento ordenado de la plataforma.

Cada Sprint deberá finalizar con:

- Código funcional.
- Pruebas.
- Documentación.
- Commit correspondiente.
- Actualización del CHANGELOG.
- Revisión de arquitectura cuando sea necesaria.

---

# 19.2 Estado Actual del Proyecto

Al momento de redactar este documento, el proyecto cuenta con los siguientes componentes implementados.

## Sprint 1

- Configuración inicial del proyecto.
- Arquitectura base.
- Organización de carpetas.
- Configuración de Git.
- Documentación inicial.

Estado:

COMPLETADO.

---

## Sprint 2

Implementación del Camera Service.

Funciones.

- Captura de video.
- Manejo de cámara.
- Lectura de frames.
- Validaciones básicas.

Estado.

COMPLETADO.

---

## Sprint 3

Implementación del Person Detector.

Funciones.

- Integración con YOLO.
- Detección de personas.
- Bounding Boxes.
- Gestión de inferencia.

Estado.

COMPLETADO.

---

## Sprint 4

Pipeline de visualización.

Funciones.

- Visualización de resultados.
- Integración entre cámara y detector.
- Pruebas de funcionamiento.

Estado.

COMPLETADO.

---

## Sprint 5

Object Tracker.

Funciones.

- Seguimiento de personas.
- IDs persistentes.
- Asociación entre frames.
- Pruebas unitarias.
- Documentación.

Estado.

COMPLETADO.

---

# 19.3 Roadmap Futuro

A partir de este punto comienza el desarrollo principal de VJC Hoops AI.

---

# Sprint 6 — Ball Detector

Objetivo.

Implementar la detección del balón.

Responsabilidades.

- Integrar detector específico.
- Identificar el balón.
- Obtener coordenadas.
- Calcular trayectoria.
- Dibujar bounding box.
- Integrar con Object Tracker.

Entregables.

- BallDetector.
- Tests.
- Documentación.

Estado.

Pendiente.

---

# Sprint 7 — Rim Detector

Objetivo.

Detectar el aro de baloncesto.

Responsabilidades.

- Detectar el aro.
- Obtener coordenadas.
- Mantener referencia fija.
- Validar precisión.

Entregables.

- RimDetector.
- Tests.
- Documentación.

Estado.

Pendiente.

---

# Sprint 8 — Pose Estimation

Objetivo.

Analizar la postura corporal.

Responsabilidades.

- Detectar articulaciones.
- Identificar brazo dominante.
- Detectar posición de piernas.
- Detectar posición de hombros.
- Detectar muñeca.
- Detectar codo.

Entregables.

- PoseEstimator.
- Tests.
- Documentación.

Estado.

Pendiente.

---

# Sprint 9 — Shot Detection Engine

Objetivo.

Detectar automáticamente un lanzamiento.

Responsabilidades.

- Detectar inicio del tiro.
- Detectar liberación del balón.
- Detectar trayectoria.
- Detectar entrada al aro.
- Determinar acierto o fallo.

Entregables.

- ShotDetector.
- Tests.
- Documentación.

Estado.

Pendiente.

---

# Sprint 10 — Statistics Engine

Objetivo.

Generar estadísticas deportivas.

Responsabilidades.

- Contabilizar tiros.
- Calcular porcentaje.
- Calcular precisión.
- Calcular promedios.
- Generar historial.

Entregables.

- StatisticsEngine.
- Tests.
- Documentación.

Estado.

Pendiente.

---

# Sprint 11 — Comunicación Python ↔ Godot

Objetivo.

Conectar el motor de IA con el videojuego.

Responsabilidades.

- Definir protocolo de comunicación.
- Enviar estadísticas.
- Recibir comandos.
- Sincronizar sesiones.

Tecnologías previstas.

- JSON.
- WebSockets.
- HTTP Local.

Estado.

Pendiente.

---

# Sprint 12 — Cliente Godot

Objetivo.

Construir la primera versión funcional del cliente gráfico.

Funciones.

- Pantalla de inicio.
- Navegación.
- Menús.
- Sistema de escenas.
- Integración inicial.

Estado.

Pendiente.

---

# Sprint 13 — Sistema de Personajes

Objetivo.

Implementar el editor de personajes.

Funciones.

- Personalización.
- Guardado.
- Accesorios.
- Colores.
- Uniformes.
- Animaciones.

Estado.

Pendiente.

---

# Sprint 14 — Dashboard Deportivo

Objetivo.

Construir el centro de estadísticas.

Funciones.

- Gráficas.
- Historial.
- Comparaciones.
- Logros.
- Objetivos.
- Recomendaciones IA.

Estado.

Pendiente.

---

# Sprint 15 — Perfil del Jugador

Objetivo.

Implementar progresión.

Funciones.

- Experiencia.
- Niveles.
- Logros.
- Rachas.
- Perfil.

Estado.

Pendiente.

---

# Sprint 16 — Persistencia Completa

Objetivo.

Implementar almacenamiento definitivo.

Funciones.

- JSON.
- Respaldos.
- Configuración.
- Historial.
- Exportación.

Estado.

Pendiente.

---

# Sprint 17 — Optimización

Objetivo.

Mejorar rendimiento.

Funciones.

- Optimizar inferencia.
- Reducir latencia.
- Mejorar FPS.
- Optimizar memoria.

Estado.

Pendiente.

---

# Sprint 18 — Beta Cerrada

Objetivo.

Primera versión para pruebas reales.

Actividades.

- Corrección de errores.
- Ajustes visuales.
- Validación IA.
- Feedback.

Estado.

Pendiente.

---

# Sprint 19 — Release Candidate

Objetivo.

Preparar la versión candidata.

Actividades.

- Optimización final.
- Limpieza.
- Revisión completa.
- Documentación final.

Estado.

Pendiente.

---

# Sprint 20 — Versión 1.0

Objetivo.

Publicar la primera versión estable.

La versión 1.0 deberá incluir.

- IA funcional.
- Detección completa.
- Dashboard.
- Personajes.
- Estadísticas.
- Perfil.
- Entrenamientos.
- Interfaz Godot.
- Documentación completa.
- Arquitectura estable.

Estado.

Pendiente.

---

# 19.4 Roadmap Posterior a la Versión 1.0

Una vez publicada la versión 1.0, el proyecto continuará evolucionando.

Entre las funcionalidades previstas se encuentran.

- Multijugador.
- Rankings.
- Torneos.
- Eventos.
- Entrenador virtual basado en IA.
- Sincronización en la nube.
- Aplicación móvil.
- Integración con relojes inteligentes.
- Integración con sensores deportivos.
- Exportación avanzada.
- API pública.
- Modo entrenador.
- Plataforma web.

Estas funcionalidades se documentarán con mayor detalle en futuras versiones del Roadmap.

---

# 19.5 Gestión del Roadmap

El Roadmap deberá mantenerse actualizado durante todo el ciclo de vida del proyecto.

Cada Sprint completado deberá marcarse como finalizado.

Cuando cambie el alcance del proyecto, el Roadmap también deberá actualizarse.

El Roadmap representa la planificación oficial de desarrollo y servirá como referencia para desarrolladores humanos e Inteligencias Artificiales.

---

# 19.6 Objetivo Final

El Roadmap Técnico tiene como finalidad proporcionar una planificación clara, organizada y escalable para el desarrollo de VJC Hoops AI.

Gracias a esta planificación, cualquier miembro del equipo podrá conocer el estado del proyecto, identificar las siguientes tareas y continuar el desarrollo siguiendo una estrategia común.

El Roadmap no es un documento estático, sino una guía viva que evolucionará junto con el proyecto hasta alcanzar la versión 1.0 y las futuras versiones de la plataforma.

---

---

# 20. Visión Estratégica y Futuro de VJC Hoops AI

## 20.1 Introducción

VJC Hoops AI nace con el propósito de combinar el entrenamiento deportivo con las tecnologías modernas de Inteligencia Artificial.

El objetivo inicial del proyecto consiste en analizar automáticamente los lanzamientos de baloncesto utilizando visión por computadora y proporcionar estadísticas objetivas que ayuden al jugador a mejorar su rendimiento.

Sin embargo, esta es únicamente la primera etapa de una visión mucho más amplia.

Desde su concepción, VJC Hoops AI ha sido diseñado para convertirse en una plataforma tecnológica capaz de evolucionar durante muchos años, incorporando nuevas funciones, nuevas disciplinas deportivas y nuevos servicios basados en Inteligencia Artificial.

Este documento representa la visión oficial del proyecto y servirá como referencia para todas las decisiones futuras.

---

# 20.2 Misión

La misión de VJC Hoops AI es democratizar el acceso a herramientas avanzadas de análisis deportivo mediante Inteligencia Artificial.

Se busca que cualquier persona, independientemente de su nivel de experiencia o recursos económicos, pueda entrenar con métricas objetivas, recibir retroalimentación inmediata y mejorar su desempeño deportivo utilizando únicamente una cámara y un dispositivo compatible.

El proyecto pretende acercar tecnologías que tradicionalmente solo estaban disponibles para equipos profesionales o centros de alto rendimiento.

---

# 20.3 Visión

La visión de VJC Hoops AI es convertirse en una de las plataformas de entrenamiento deportivo basadas en Inteligencia Artificial más completas y accesibles del mercado.

El proyecto aspira a integrar análisis técnico, estadísticas, personalización, gamificación y herramientas educativas en una única plataforma capaz de acompañar al jugador durante todo su proceso de aprendizaje.

La plataforma deberá evolucionar constantemente incorporando nuevas tecnologías sin perder la simplicidad de uso ni la calidad de la experiencia del usuario.

---

# 20.4 Principios Fundamentales

Todas las decisiones del proyecto deberán respetar los siguientes principios.

- Arquitectura limpia.
- Escalabilidad.
- Código mantenible.
- Documentación completa.
- Transparencia.
- Calidad antes que velocidad.
- Diseño modular.
- Accesibilidad.
- Innovación responsable.

Estos principios servirán como guía permanente para el desarrollo técnico y funcional.

---

# 20.5 Objetivos a Corto Plazo

Durante las primeras versiones el proyecto se enfocará en completar el análisis automático de lanzamientos de baloncesto.

Entre los principales objetivos se encuentran.

- Detección de personas.
- Detección del balón.
- Detección del aro.
- Seguimiento de objetos.
- Detección automática del lanzamiento.
- Cálculo de estadísticas.
- Interfaz desarrollada en Godot.
- Sistema de perfiles.
- Dashboard deportivo.
- Persistencia de datos.

La prioridad será construir una base sólida antes de añadir funcionalidades avanzadas.

---

# 20.6 Objetivos a Mediano Plazo

Una vez publicada la versión 1.0, el proyecto continuará creciendo mediante nuevas características.

Entre ellas.

- Entrenamientos personalizados.
- Recomendaciones automáticas mediante IA.
- Comparación entre sesiones.
- Objetivos semanales.
- Eventos especiales.
- Exportación avanzada de reportes.
- Sincronización en la nube.
- Aplicación móvil.
- Cliente web.
- API pública.

Estas funciones ampliarán las posibilidades de uso sin modificar la arquitectura principal.

---

# 20.7 Objetivos a Largo Plazo

La visión a largo plazo contempla convertir VJC Hoops AI en un ecosistema completo de entrenamiento deportivo.

Las futuras líneas de desarrollo incluyen.

- Integración con dispositivos inteligentes.
- Compatibilidad con relojes deportivos.
- Integración con sensores de movimiento.
- Análisis biomecánico avanzado.
- Asistente virtual basado en IA.
- Entrenamientos completamente personalizados.
- Plataformas educativas.
- Comunidad global de jugadores.
- Rankings internacionales.
- Torneos virtuales.

La arquitectura actual deberá facilitar estas expansiones.

---

# 20.8 Expansión a Otros Deportes

Aunque la primera versión está centrada en el baloncesto, el diseño del proyecto permitirá incorporar otros deportes en el futuro.

Ejemplos.

- Fútbol.
- Voleibol.
- Tenis.
- Béisbol.
- Atletismo.
- Pádel.

Cada disciplina podrá implementar sus propios módulos de análisis reutilizando la arquitectura existente.

---

# 20.9 Inteligencia Artificial como Núcleo del Proyecto

La Inteligencia Artificial será el componente principal de VJC Hoops AI.

Su función no será únicamente detectar objetos.

También participará en.

- Interpretación de movimientos.
- Análisis técnico.
- Predicción de rendimiento.
- Recomendaciones personalizadas.
- Detección de errores.
- Seguimiento del progreso.
- Generación automática de informes.

La IA deberá evolucionar constantemente incorporando nuevos modelos y técnicas cuando aporten beneficios reales.

---

# 20.10 Comunidad

El proyecto buscará construir una comunidad activa alrededor de la plataforma.

En futuras versiones podrán incorporarse.

- Rankings.
- Compartir estadísticas.
- Retos entre jugadores.
- Equipos.
- Clubes.
- Torneos.
- Eventos especiales.

La comunidad será un elemento importante para mantener la motivación de los usuarios.

---

# 20.11 Filosofía de Desarrollo

VJC Hoops AI deberá desarrollarse pensando siempre en el largo plazo.

Las decisiones técnicas no se tomarán únicamente por rapidez de implementación.

Cada cambio deberá responder a la siguiente pregunta.

"¿Esta decisión facilitará el crecimiento del proyecto dentro de cinco años?"

Si la respuesta es negativa, deberá evaluarse una alternativa más adecuada.

---

# 20.12 Colaboración entre Humanos e Inteligencias Artificiales

El proyecto ha sido concebido para desarrollarse mediante una colaboración continua entre personas e Inteligencias Artificiales.

La documentación deberá proporcionar suficiente contexto para que cualquier IA pueda incorporarse al proyecto sin depender del historial de conversaciones.

Esto permitirá mantener la continuidad del desarrollo independientemente de la herramienta utilizada.

---

# 20.13 Compromiso con la Calidad

La calidad será siempre prioritaria sobre la velocidad.

Cada nueva funcionalidad deberá estar correctamente diseñada, implementada, documentada y validada antes de considerarse finalizada.

La documentación oficial deberá mantenerse sincronizada con el estado real del proyecto.

---

# 20.14 Evolución Continua

VJC Hoops AI no debe considerarse un proyecto con un punto final definido.

Se trata de una plataforma en evolución constante.

Cada nueva versión representará una mejora sobre la anterior, manteniendo siempre la compatibilidad, la estabilidad y la claridad arquitectónica.

La capacidad de adaptación será uno de los principales objetivos del proyecto.

---

# 20.15 Declaración Final

VJC Hoops AI representa la visión de construir una plataforma profesional de entrenamiento deportivo impulsada por Inteligencia Artificial, diseñada para crecer durante muchos años y mantenerse accesible para cualquier persona interesada en mejorar su rendimiento.

Este proyecto combina desarrollo de software, visión por computadora, aprendizaje automático, diseño de videojuegos y experiencia de usuario con el propósito de ofrecer una herramienta moderna, escalable y de alta calidad.

Toda decisión técnica deberá respetar la misión, la visión y los principios definidos en este documento.

PROJECT_CONTEXT.md constituye la fuente principal de conocimiento del proyecto y deberá mantenerse actualizado conforme evolucione la plataforma.

---

