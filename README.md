CampusNavigator IA — PA4

Curso: Algoritmo y Estructura de Datos Basados en Inteligencia Artificial
NRC: 30710
Docente(s): WILDER JULIO ESPINOZA BRAVO
Fecha de entrega: 01/07/2026

Integrantes del grupo

1. Diego Ricardo Arcos Espinoza
2. Jerson Herrera Salazar
3. Fabian Marcelo Davila Herrera
4. Juan José Montenegro

Propósito del trabajo

Este repositorio contiene la solución grupal a la evaluación PA4 – Proceso de Aprendizaje 4, correspondiente al caso integrador CampusNavigator IA, un módulo académico pensado para orientar a estudiantes dentro del campus.

La solución cubre tres necesidades planteadas por el caso:

- Ordenamiento recursivo de resultados y recorridos mediante una estrategia de divide y vencerás.
- Modelado del campus como un grafo con ambientes, laboratorios y servicios como nodos.
- Aplicación de algoritmos de búsqueda (DFS, BFS y A*) para recomendar recorridos según el objetivo del usuario.

Estructura del repositorio

.
├── README.md               ← este archivo
├── /docs                   ← documentación del examen
│   └── PA4_Informe.pdf     ← informe completo con el desarrollo de las 4 actividades
├── /src                    ← código fuente y pseudocódigo
│   └──ejercicio02.py
└── /evidencias             ← capturas, evidencia grupal, borradores

Resumen breve de la solución

Actividad 1 — Recursividad. Se diseñó un algoritmo recursivo que calcula el número total de pasos necesarios para revisar una secuencia de puntos de control del campus, con su respectiva traza manual de al menos 5 llamadas y la identificación de caso base y caso recursivo.
Actividad 2 — Ordenamiento recursivo. Se implementó Merge Sort sobre un vector de 8 tiempos estimados de desplazamiento entre puntos del campus [12, 7, 25, 4, 18, 9, 15, 2]. Se eligió Merge Sort por ser el ejemplo más claro del principio divide y vencerás, con eficiencia O(n log n) frente a los O(n²) de alternativas como Bubble Sort. El código está en /src/actividad2_merge_sort.py.
Actividad 3 — Grafos y búsquedas. El campus se modeló como un grafo [dirigido / no dirigido — completar] con [número] nodos y [número] conexiones, sobre el cual se aplicaron los recorridos DFS y BFS desde un nodo origen. Adicionalmente, se propuso un escenario donde A* resulta pertinente, indicando la heurística utilizada.
Actividad 4 — Cierre grupal. Conclusiones del equipo sobre lo aprendido al combinar recursividad y grafos para resolver un problema real, con propuestas de mejora para una segunda versión del módulo.

El desarrollo detallado, diagramas y justificaciones técnicas se encuentran en /docs/EVALUACIÓN PA04 - 5360.pdf.

Video de sustentación

📹 Enlace del video en YouTube: 
