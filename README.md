# Herramienta de Diagnóstico de TI

[cite\_start]Una aplicación de escritorio desarrollada en Python para evaluar la madurez de los procesos de Tecnologías de la Información (TI) de una organización, utilizando los marcos de referencia COBIT y CMMI. [cite: 15]

## ✨ Características Principales

  * [cite\_start]**Autenticación de Usuario:** Permite el registro e inicio de sesión para guardar y personalizar los diagnósticos. [cite: 18]
  * [cite\_start]**Evaluación COBIT:** Mide la madurez en 5 dimensiones clave de COBIT a través de un sistema de calificación. [cite: 19, 20]
  * [cite\_start]**Evaluación CMMI:** Evalúa la madurez en 5 áreas de proceso de CMMI con una calificación de 1 a 5. [cite: 21]
  * [cite\_start]**Visualización de Resultados:** Presenta los resultados de ambas evaluaciones en gráficos de barras intuitivos. [cite: 22]
  * [cite\_start]**Recomendaciones Personalizadas:** Genera recomendaciones específicas basadas en los niveles de madurez obtenidos. [cite: 23, 24]
  * [cite\_start]**Exportación de Informes:** Permite exportar los resultados y recomendaciones a archivos **CSV** y **PDF**. [cite: 25]
  * [cite\_start]**Interfaz Gráfica Moderna:** Utiliza la librería `ttkbootstrap` para una experiencia de usuario atractiva y amigable. [cite: 26]

-----

## 🚀 Instalación

Para ejecutar esta aplicación en tu sistema, sigue estos pasos:

1.  **Clona el repositorio** o descarga los archivos en una carpeta local.

2.  [cite\_start]**Asegúrate de tener Python 3 instalado.** [cite: 29]

3.  **Abre una terminal** en la carpeta del proyecto. Se recomienda crear un entorno virtual para no afectar otras instalaciones de Python:

    ```bash
    # Crear un entorno virtual (ej. en macOS/Linux)
    python3 -m venv entorno

    # Activar el entorno
    source entorno/bin/activate
    ```

4.  [cite\_start]**Instala las dependencias necesarias** con pip. [cite: 39] [cite\_start]Los módulos requeridos son `matplotlib`, `reportlab`, y `ttkbootstrap`. [cite: 35, 36, 37]

    ```bash
    pip install -r requirements.txt
    ```

-----

## 📋 Modo de Uso

1.  [cite\_start]Con tu terminal en la carpeta del proyecto y el entorno virtual activado, ejecuta la aplicación: [cite: 133]

    ```bash
    python app.py
    ```

2.  **Inicia sesión o regístrate.** Si es tu primera vez, crea una cuenta nueva. [cite\_start]Si ya tienes una, ingresa tus credenciales. [cite: 136]

3.  [cite\_start]**Realiza las evaluaciones.** Navega a las pestañas 'COBIT' y 'CMMI' y selecciona el nivel de madurez (1 a 5) para cada ítem. [cite: 147, 151, 152]

4.  [cite\_start]**Genera el diagnóstico.** Una vez completadas ambas evaluaciones, haz clic en el botón "Generar Diagnóstico". [cite: 158, 159]

5.  [cite\_start]**Analiza los resultados.** Serás dirigido a la pestaña de "Resultados", donde verás los gráficos y las recomendaciones personalizadas. [cite: 164, 165]

6.  [cite\_start]**Exporta los informes.** Si lo deseas, puedes guardar un informe completo en formato CSV o PDF usando los botones de exportación. [cite: 168]

-----

## 🧑‍💻 Autores

[cite\_start]Este proyecto fue desarrollado por estudiantes de la carrera de **Administración Informática** en la **UPIICSA - IPN**. [cite: 3, 4, 6]

  * [cite\_start]**CISNEROS VALERO JOSÉ MANUEL** [cite: 8]
  * [cite\_start]**HERNANDEZ DEL PILAR AZUL MAGALY** [cite: 8]
  * [cite\_start]**ROMERO PÉREZ MIGUEL ÁNGEL** [cite: 8]

[cite\_start]**Profesor:** JUAN CARLOS CRUZ ROMERO [cite: 10]

-----

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.