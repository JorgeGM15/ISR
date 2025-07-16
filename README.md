# Calculadora Simplificada de ISR para Empleados en Python

Este proyecto es un script en Python que utiliza las librerías `pandas` y `numpy` para simular el cálculo del Impuesto Sobre la Renta (ISR) para un conjunto de 10 empleados ficticios. El objetivo principal es demostrar la manipulación de datos tabulares y la aplicación de cálculos vectorizados.

---

## 📜 Descripción del Proyecto

El script realiza las siguientes operaciones:
1.  **Genera un conjunto de datos**: Crea 10 empleados con salarios mensuales aleatorios para un año completo.
2.  **Aplica una fórmula de ISR**: Utiliza un modelo fiscal simplificado, basado en un único tramo impositivo, para calcular la retención mensual de cada empleado.
3.  **Calcula los totales anuales**: Suma los salarios y las retenciones mensuales para obtener un resumen anual por empleado.
4.  **Presenta los resultados**: Muestra tres tablas (DataFrames) en la consola: salarios mensuales, ISR mensual y el resumen anual.

**Nota Importante**: El cálculo del ISR en este script es una **simplificación** con fines educativos y no representa la complejidad total de la ley fiscal real, que incluye múltiples tramos, subsidios y deducciones.

---

## ✨ Características Principales

* **Uso de `pandas`**: Toda la información se organiza y manipula eficientemente a través de DataFrames, la estructura de datos central de la librería.
* **Uso de `numpy`**: Se utiliza para la generación de datos numéricos aleatorios de manera eficiente y reproducible.
* **Código Vectorizado**: Los cálculos se aplican a columnas enteras de datos a la vez, lo que resulta en un código más limpio y con mejor rendimiento que los bucles tradicionales.
* **Código Reproducible**: Gracias al uso de `np.random.seed()`, los resultados son consistentes en cada ejecución.

---

## 🔧 Requisitos

Necesitarás tener las siguientes librerías de Python instaladas:
* `numpy`
* `pandas`

Puedes instalarlas usando pip:
```bash
pip install numpy pandas
```
## 🚀 Cómo Ejecutar

Simplemente clona el repositorio y ejecuta el script de Python desde tu terminal:
```python ISR_empleados.py```

El script imprimirá en la consola las tres tablas con los resultados de los cálculos.

