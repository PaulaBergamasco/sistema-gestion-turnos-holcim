# Sistema de Gestión de Turnos – Holcim

Proyecto desarrollado en el marco del Módulo Programador de la Tecnicatura Superior en Desarrollo de Software.

El sistema tiene como objetivo optimizar la gestión de turnos de carga en la playa de operaciones de Holcim – Planta Malagueño, Córdoba, permitiendo registrar y administrar turnos, vehículos y choferes, consultar la disponibilidad horaria y controlar el estado de cada turno.

La solución busca evitar superposiciones de horarios, reducir tiempos de espera y mejorar la organización de los arribos de transporte mediante una aplicación de escritorio integrada con una base de datos relacional.

## Ejecutar el proyecto (Windows)

1. Instalar MySQL Server 8 y MySQL Workbench.
2. Ejecutar `sql/schema.sql`, después `sql/datos_prueba.sql` y finalmente `sql/roles.sql` en MySQL Workbench. Los datos de prueba se cargan una sola vez.
3. Crear un archivo `.env` en la raíz del proyecto, tomando `.env.example` como referencia y completando `DB_PASSWORD` con la contraseña local de MySQL. No subir `.env` a Git.
4. Instalar las dependencias: `py -m pip install -r requirements.txt`.
5. Ejecutar: `py main.py`.

Las pantallas usan las funciones de `datos/` y la conexión compartida de `conexion.py`.
