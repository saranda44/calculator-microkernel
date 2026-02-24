# calculator-microkernel

Calculadora modular basada en arquitectura **microkernel**.
El núcleo (`core`) se encarga de gestionar y cargar dinámicamente los plugins que implementan operaciones.

---

## 🧩 Arquitectura

* **Core**: Maneja el registro, carga y ejecución de operaciones.
* **Plugins**: Implementan operaciones matemáticas siguiendo una interfaz común.

---

## 📁 Estructura del proyecto

```
calculator-microkernel/
│
├── main.py                # Punto de entrada
├── core/                  # Núcleo del sistema
│   ├── interface.py       # Interfaz de operadores
│   └── microkernel.py     # Lógica del microkernel
│
├── plugins/               # Operaciones (plugins)
│   ├── add.py
│   ├── subtract.py
│   ├── multiply.py
│   ├── divide.py
│   ├── power.py
│   └── root.py
```

---

## ▶️ Uso

Ejecuta el programa:

```bash
python3 main.py
```

El microkernel:

1. Detecta automáticamente los módulos dentro de `plugins/`
2. Registra las clases que implementan `get_name()` y `execute()`
3. Permite ejecutar operaciones dinámicamente

---

## ➕ Crear un nuevo plugin

1. Crea un archivo en `plugins/`
2. Implementa la interfaz:

```python
from core.interface import OperatorInterface

class Modulo(OperatorInterface):
    def __init__(self):
        super().__init__('mod')

    def get_name(self):
        return self.operator

    def execute(self, a, b):
        return a % b
```

3. El microkernel lo cargará automáticamente al iniciar

---

## ⚙️ Concepto clave

El sistema separa:

* **Core** → lógica del sistema (estable)
* **Plugins** → funcionalidades extensibles

Esto permite agregar nuevas operaciones **sin modificar el núcleo**.
