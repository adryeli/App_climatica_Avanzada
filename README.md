# 🌤️ App Climática

Aplicación de gestión y registro del clima.

---

## 📁 Estructura del proyecto

```
App_climatica_Python/
├── .github/
│   └── workflows/
│       └── ci.yml               # Pipeline de CI (tests automáticos)
├── controller/
│   ├── control_alert.py         # Controlador de alertas
│   ├── control_menu.py          # Controlador del menú
│   └── control_time.py          # Controlador de tiempo/fechas
├── data/
│   └── register.json            # Almacenamiento de registros (autogenerado)
├── model/
│   ├── __init__.py
│   ├── manager.py               # Gestor principal de datos (JSON)
│   └── register_weather.py      # Lógica de registros del clima
├── test/
│   ├── __init__.py
│   ├── test_control_alert.py
│   ├── test_control_weather.py
│   ├── test_index.py
│   ├── test_manager.py
│   └── test_register_weather.py
├── view/
│   └── menu.py                  # Vista del menú principal
├── conftest.py                  # Configuración de pytest
├── index.py                     # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
└── README.md
```

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone git@github.com:lermns/App_climatica_Python.git
cd App_climatica_Python
```

### 2. Crear y activar el entorno virtual

```bash
# Crear
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación (en proceso)

```bash
python index.py
```

---

## 🧪 Tests

```bash
# Ejecutar todos los tests
pytest

# Ver detalle de cada test
pytest -v

# Ejecutar solo un archivo de tests
pytest test/test_manager.py -v
```

> ⚠️ Ejecuta siempre los tests desde la raíz del proyecto, no desde dentro de `/test`.

---

## 📝 Guía de Conventional Commits

Usa esta guía para elegir el tipo correcto en cada commit:

```
¿Corregiste un error o bug?
  Sí → fix:
  No ↓

¿Cambiaste funcionalidad existente o afectaste la interfaz de usuario?
  Sí → feat:
  No ↓

¿Añadiste o modificaste tests?
  Sí → test:
  No ↓

¿Cambiaste el estilo o formato del código (sin afectar su comportamiento)?
  Sí → style:
  No ↓

¿Realizaste cambios en la documentación?
  Sí → docs:
  No ↓

¿Modificaste la forma en que se construye el proyecto (paquetes, dependencias, dockerfile, etc.)?
  Sí → build:
  No ↓

¿Cambiaste algo relacionado con DevOps (pipelines de CI/CD, despliegue, etc.)?
  Sí → ops:
  No ↓

¿Completaste una tarea de mantenimiento o no relacionada con el código (ej. .gitignore, commit inicial)?
  Sí → chore:
  No ↓

¿Reescribiste o reestructuraste código específicamente para mejorar el rendimiento?
  Sí → perf:
  No → refactor:
```

### Formato de un commit

```
<tipo>(<ámbito opcional>): <descripción breve>
```

### Ejemplos

| Commit | Cuándo usarlo |
|---|---|
| `fix(alert): corregir umbral de temperatura` | Se corrige un bug en las alertas |
| `feat(menu): añadir opción de exportar datos` | Se añade una nueva funcionalidad |
| `test(manager): añadir tests unitarios` | Se crean o modifican tests |
| `style: aplicar formato PEP8` | Cambios de estilo sin lógica |
| `docs: actualizar README` | Cambios en documentación |
| `build: añadir dependencia requests` | Cambios en dependencias |
| `ops: configurar pipeline de CI` | Cambios en CI/CD |
| `chore: añadir .gitignore` | Tareas de mantenimiento |
| `perf(manager): optimizar lectura de JSON` | Mejora de rendimiento |
| `refactor(controller): simplificar lógica` | Refactorización sin cambio de comportamiento |
