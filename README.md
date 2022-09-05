Template Osee
==============================

template of how all the files will be organized

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
<h1>data-science-project-template</h1>
<h2>Configuracion del entorno</h2>
<p>1. Descargar e instalar Anaconda del siguiente enlace: <a target="_blank" href="https://www.anaconda.com">https://www.anaconda.com/</a>.</p>
<p>2. Como IDE se recomienda usar el Visual Studio Code el cual se puede descargar del siguiente enlace: <a target="_blank" href="https://code.visualstudio.com/Download">https://code.visualstudio.com/Download/</a>.</p>

<p>3. Clonar el proyecto desde GitHub y localizarlo en el folder de su preferencia.</p>

<p>4. Una vez instalado ambos programas (Anaconda y Visual Studio Code), abrir el editor Visual Studio Code y en la pestaña File hacer click para abrir el folder donde hemos clonado el proyecto (paso 3.).</p>

<p>5. En el visual Studio Code abrimos una nueva terminal y ejecutamos el comando <b>conda env create --file=enviroment.yaml</b>.</p>

<p>6. Con el paso 5° hemos creado un entorno virtual con lo necesario para ejecutar los scripts ahora debe para ejecutar el entorno virtual debemos ejecutar el comando <b>conda activate envOsee</b>.</p>

<p>7. Una activate nuestro entorno virual en el terminal se mostrará lo siguiente: <b>(envOsee) C:\Users\GNC\Desktop\crearCokkie\project_template></b>.</p>

<p>8. Ya podemos ejecutar cada unos de los scripts.</p>



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
