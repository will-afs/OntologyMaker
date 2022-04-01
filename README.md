# <img src="https://github.com/will-afs/AdvancedAcademicProject/blob/main/doc/Icons/OntologyMaker.png" width="30"> OntologyMaker

Build an ontology from scientific articles data (authors, references, relations, etc.)

This is a sub-project of the [AdvancedAcademicProject](https://github.com/will-afs/AdvancedAcademicProject/)

<img src="https://github.com/will-afs/AdvancedAcademicProject/blob/main/doc/Steps/Step%203%20-%20Building%20the%20ontology.JPG" width="700">

⚙️ Configuration
-----------------
The project configuration holds in the [project_config.toml file](https://github.com/will-afs/OntologyMaker/settings/project_config.toml)

🐇 Quickly run the service as a container
------------------------------------------

    sudo docker run -p 9000:8080 williamafonso/ontologymaker:latest

🧪 Developing and running tests
--------------------------------
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

Run the main python file:

    celery -A src.core.ontologymaker worker --loglevel=INFO --concurrency=1

The tests are placed in the tests folder. They can be ran with pytests, as follows:

    python -m pytest tests

 🐋 Containerizing the application 
----------------------------------
To build a Docker image :

    sudo docker build --tag ontologymaker .
    
Or if you want to be able to push it to your DockerHub:

    sudo docker build --tag <your_docker_username>/ontologymaker .

Pushing the Docker image to your registry :

    sudo docker push <your_docker_user_name>/ontologymaker

You can now run the Docker image as a container :

    sudo docker run -d -p 80:80 ontologymaker
