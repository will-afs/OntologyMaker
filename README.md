# <img src="https://github.com/will-afs/AdvancedAcademicProject/blob/main/doc/Icons/OntologyMaker.png" width="30"> OntologyMaker

Build an ontology from scientific articles data (authors, references, relations, etc.)

This is a sub-project of the [AdvancedAcademicProject](https://github.com/will-afs/AdvancedAcademicProject/)

<img src="https://github.com/will-afs/AdvancedAcademicProject/blob/main/doc/Steps/Step%203%20-%20Building%20the%20ontology.JPG" width="700">

*Note: For now, the input data are retrieved from a macrostructure.json file instead of a Redis task queue.*

🐇 Quickly run the notebook
----------------------------
In a terminal, run the following command:

    git clone https://github.com/will-afs/OntologyMaker.git

For the following, the working directory will be the root of this folder:

    cd OntologyMaker/
    
Add the working directory to the Python PATH environment variable:

    export PYTHONPATH=$(pwd)
    
Create a virtual environment:

    python3 -m venv .venv

Activate the virtual environment:
    
    source .venv/bin/activate
    
Install the dependencies:
    
    pip install -r requirements.txt

Run the main notebook (ontology_maker.ipynb)
