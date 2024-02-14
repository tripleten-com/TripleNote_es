# triple_note

## Descripción
TripleNote, un cuaderno electrónico para quienes no quieren olvidarse de nada anotándolo todo.

Presta atención a las peculiaridades del proyecto: si el campo slug no se rellena en el formulario al crear una nota, el título transliterado de la nota se establecerá como la dirección de la página; además, el campo slug debe ser único.

Para cargar notas preparadas después de aplicar las migraciones, ejecuta este comando:
```bash
python manage.py loaddata db.json
```
Después de esto, estarán disponibles en el proyecto dos usuarios, `author` y `reader`.
Las contraseñas coinciden con el login.


## Cómo trabajar con un repositorio
Para empezar la tarea, necesitas copiar la URL del repositorio y clonarlo en tu computadora.

  
### Creación de un entorno virtual

1. Inicia el editor de código de Visual Studio y, a través del menú *"Archivo" / "Abrir directorio"*, abre la carpeta *Dev/triple_note/*.
2. Inicia la terminal en VS Code, asegúrate de trabajar desde el directorio `triple_note/` (si estás trabajando en Windows, asegúrate de que Git Bash se esté ejecutando en la terminal, ni PowerShell ni nada más), y ejecuta el comando:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
El entorno virtual se desplegará en el directorio *triple_note/* y aparecerá una carpeta `venv`, que almacenará todas las dependencias del proyecto.


### Activación del entorno virtual
En la terminal, navega hasta el directorio raíz del proyecto *Dev/triple_note/* y ejecuta este comando:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Ahora todos los comandos en la terminal irán precedidos por el string `(venv)`.

💡 Todos los comandos siguientes deben ejecutarse con el entorno virtual de trabajo.

Actualiza pip:

```bash
python -m pip install --upgrade pip
```

### Instalar las dependencias del archivo *requirements.txt*:
Mientras estás en la carpeta *Dev/triple_note/*, ejecuta este comando:

```bash
pip install -r requirements.txt
```

### Aplicación de migraciones

    
En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py migrate
```

### Ejecutar el proyecto en modo dev

    
En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py runserver
```

En respuesta, Django indicará que el servidor está funcionando y que el proyecto está disponible en [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
