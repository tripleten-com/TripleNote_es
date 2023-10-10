# triple_note

## Description
TripleNote, an electronic notebook for those who don't want to forget anything by writing everything down.

Pay attention to the peculiarities of the project. If the slug field is not filled out in the form when creating a note, then the transliterated title of the note will be set as the page address; in addition, the slug field should be unique.

To load prepared news after applying migrations, execute this command:
```bash
python manage.py loaddata db.json
```
After this, two users will be available in the project: `author` and `reader`.
The passwords match the login.


## How to work with a repository
To start the task, you need to copy the repository URL and clone it to your computer.  

  
### Create a virtual environment

1. Launch the Visual Studio Code editor and through the "*File"  / "Open Directory"* menu, open the *Dev/triple_note/* folder.
2. Launch the terminal in VS Code, make sure you are working from the directory *triple_note/* (if you are working on Windows, make sure that Git Bash is running in the terminal, not PowerShell or anything else), and execute the command:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
The virtual environment will be deployed in the *triple_note/* directory and a `venv` folder will appear, which will store all project dependencies.


### Activation of the virtual environment
In the terminal, navigate to the root directory of the project *Dev/triple_note/* and execute this command:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Now all commands in the terminal will be preceded by the string `(venv)`.

💡 All the following console commands must be run with the working virtual environment.

Refresh pip:

```bash
python -m pip install --upgrade pip
```

### Installing dependencies from the *requirements.txt*:
While in the *Dev/triple_note/* folder, execute this command:

```bash
pip install -r requirements.txt
```

### Application of migrations

    
In the directory with the manage.py file, run this command: 

```bash
python manage.py migrate
```

### Launching the project in dev mode

    
In the directory with the manage.py file, run this command:

```bash
python manage.py runserver
```

In response, Django will report that the server is running and the project is available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
