# Proyecto de Análisis de Sentimientos de Playlists de Spotify

Este proyecto es una aplicación web que permite a los usuarios analizar los sentimientos de las playlists de Spotify utilizando la API de Spotify y un modelo de análisis de sentimientos de Hugging Face.

## Requisitos

- Python 3.7 o superior
- Flask
- Spotipy
- Transformers
- Requests

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/jesusruiztoledo/MoodTrack
    cd MoodTrack
    ```

2. Crea un entorno virtual:
    ```sh
    python -m venv myenv
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source myenv/bin/activate
        ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto y añade tus credenciales de Spotify:
    ```env
    SPOTIFY_CLIENT_ID=tu_cliente_id
    SPOTIFY_CLIENT_SECRET=tu_cliente_secreto
    ```

## Uso

1. Inicia la aplicación:
    ```sh
    python app.py
    ```

2. Abre tu navegador y ve a `http://127.0.0.1:5000`.

3. Ingresa el ID de usuario de Spotify para analizar las playlists.

## Estructura del Proyecto

- [app.py](http://_vscodecontentref_/1): Archivo principal de la aplicación Flask.
- [config.py](http://_vscodecontentref_/2): Archivo de configuración (si es necesario).
- [static](http://_vscodecontentref_/3): Archivos estáticos (CSS, fuentes, etc.).
- [templates](http://_vscodecontentref_/4): Plantillas HTML.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.