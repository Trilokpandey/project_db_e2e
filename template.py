from fileinput import filename
import os
from pathlib import Path
import logging

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] :  %(message)s",
    level=logging.INFO
)



list_of_files=[
    ".github/workflows/.gitkeep",
    f"lib/authantication_template/__init__.py",
    f"lib/pipelinetemplate/__init__.py",
    f"datatransactions/__init__.py",
    f"datawrangling/__init__.py",
    f"predictor/__init__.py",
    f"predictor/api/__init__.py",
    f"predictor/api/endpoints/__init__.py",
    f"predictor/util/__init__.py",
    f"services/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "setup.py",
    "microservice_flask.py",
    "prefetch_model.py",
    "start_server.sh",
    "wsgi.py",
    "requirements.txt",
    "jenkinsfike",
    "Dockerfile",
    "setup.py",
    "setup.cfg",
    "init_setup.sh",
    "pyproject.toml",
    "tox.ini"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"file directory: {filedir} created for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file ois already present at : {filepath}")



