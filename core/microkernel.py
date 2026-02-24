import importlib
import pkgutil
import inspect


class Microkernel:
    def __init__(self, plugins_package="plugins"):
        self.operators = {}
        self.plugins_package = plugins_package

    def register_operator(self, operator_interface):
        name = operator_interface.get_name()
        self.operators[name] = operator_interface

    def load_plugins(self):
        """
        Carga dinámicamente todos los módulos dentro del paquete self.plugins_package
        (ej. carpeta plugins/ con __init__.py).
        """
        package = importlib.import_module(self.plugins_package)

        for _, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            if is_pkg:
                continue  # Ignora subpaquetes por simplicidad
            full_module_name = f"{self.plugins_package}.{module_name}"
            module = importlib.import_module(full_module_name)
            self._register_from_module(module)

    def _register_from_module(self, module):
        """
        Registra automáticamente clases del módulo que parezcan ser operaciones.
        Regla simple: clase con métodos get_name y execute.
        """
        for _, obj in inspect.getmembers(module, inspect.isclass):
            # Evita clases importadas desde otros módulos
            if obj.__module__ != module.__name__:
                continue

            if callable(getattr(obj, "get_name", None)) and callable(
                getattr(obj, "execute", None)
            ):
                self.register_operator(obj())
                # Si quieres solo 1 operación por archivo, descomenta:
                # break

    def execute_operation(self, operator_name, a, b):
        op = self.operators.get(operator_name)
        if not op:
            raise ValueError(f"Operator '{operator_name}' not found.")
        return op.execute(a, b)
