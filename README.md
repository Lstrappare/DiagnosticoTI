# Herramienta de Diagnóstico de TI

Una aplicación de escritorio desarrollada en Python para evaluar la madurez de los procesos de Tecnologías de la Información (TI) de una organización, utilizando los marcos de referencia COBIT y CMMI.

<img width="1920" height="1440" alt="Proyecto3" src="https://github.com/user-attachments/assets/f280527b-14dd-47d0-b653-02748347e49d" />

## ✨ Características Principales

  * **Autenticación de Usuario:** Permite el registro e inicio de sesión para guardar y personalizar los diagnósticos.
  * **Evaluación COBIT:** Mide la madurez en 5 dimensiones clave de COBIT a través de un sistema de calificación.
  * **Evaluación CMMI:** Evalúa la madurez en 5 áreas de proceso de CMMI con una calificación de 1 a 5.
  * **Visualización de Resultados:** Presenta los resultados de ambas evaluaciones en gráficos de barras intuitivos.
  * **Recomendaciones Personalizadas:** Genera recomendaciones específicas basadas en los niveles de madurez obtenidos.
  * **Exportación de Informes:** Permite exportar los resultados y recomendaciones a archivos **CSV** y **PDF**.
  * **Interfaz Gráfica Moderna:** Utiliza la librería `ttkbootstrap` para una experiencia de usuario atractiva y amigable.

-----

## 🚀 Instalación

Para ejecutar esta aplicación en tu sistema, sigue estos pasos:

1.  **Clona el repositorio** o descarga los archivos en una carpeta local.

2.  **Asegúrate de tener Python 3 instalado.**

3.  **Abre una terminal** en la carpeta del proyecto. Se recomienda crear un entorno virtual para no afectar otras instalaciones de Python:

    ```bash
    # Crear un entorno virtual (ej. en macOS/Linux)
    python3 -m venv entorno

    # Activar el entorno
    source entorno/bin/activate
    ```

4.  **Instala las dependencias necesarias** con pip. [cite: 39] Los módulos requeridos son `matplotlib`, `reportlab`, y `ttkbootstrap`.

    ```bash
    pip install -r requirements.txt
    ```

-----

## 📋 Modo de Uso

1.  Con tu terminal en la carpeta del proyecto y el entorno virtual activado, ejecuta la aplicación:

    ```bash
    python app.py
    ```

2.  **Inicia sesión o regístrate.** Si es tu primera vez, crea una cuenta nueva. Si ya tienes una, ingresa tus credenciales.

3.  **Realiza las evaluaciones.** Navega a las pestañas 'COBIT' y 'CMMI' y selecciona el nivel de madurez (1 a 5) para cada ítem.

4.  **Genera el diagnóstico.** Una vez completadas ambas evaluaciones, haz clic en el botón "Generar Diagnóstico".

5.  **Analiza los resultados.** Serás dirigido a la pestaña de "Resultados", donde verás los gráficos y las recomendaciones personalizadas.

6.  **Exporta los informes.** Si lo deseas, puedes guardar un informe completo en formato CSV o PDF usando los botones de exportación.

-----

## 🧑‍💻 Autores

Este proyecto fue desarrollado por estudiantes de la carrera de **Administración Informática** en la **UPIICSA - IPN**.

  * **CISNEROS VALERO JOSÉ MANUEL**
  * **HERNANDEZ DEL PILAR AZUL MAGALY**
  * **ROMERO PÉREZ MIGUEL ÁNGEL**
    
-----

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
