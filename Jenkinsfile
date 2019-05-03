#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                bat '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               cd Rodrigo
               python -m Pyautomators -f json -o rodrigo.json
               cd ../Raul
               python -m Pyautomators -f json -o raul.json
               cd ../Gustavo/localExtra
               python -m Pyautomators -f json -o gustavo.json
               cd ../../Leonardo/Extra
               python -m Pyautomators -f json -o leonardo.json
               '''
            }
        }
    }
}
