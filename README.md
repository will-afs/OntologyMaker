# <img src="https://github.com/will-afs/AdvancedAcademicProject/blob/main/doc/OntologyMaker.png" width="30"> OntologyMaker

Build an ontology from inferences made onto a set of rules, entities and relations between each

This is a sub-project of the [AdvancedAcademicProject](https://github.com/will-afs/AdvancedAcademicProject/)

⚙️ Configuration
-----------------
The project configuration holds in the project_config.toml file.

🔽 Installing the project on your machine
------------------------------------------
In a terminal, run the following command :

    git clone https://github.com/will-afs/OntologyMaker.git

Then build the Docker image :

    sudo docker build --tag ontologymaker .

▶️ Usage
---------
You can now run the Docker image as a container :

    docker run ontologymaker

🧪 Running tests
-----------------
The tests are placed in the tests folder. They can be ran with pytests, as follows :

    python -m pytest tests
