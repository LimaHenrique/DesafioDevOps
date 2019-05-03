#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                bat '''
                python -m pip install --upgrade pip
                pip install python-jenkins
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
               python -m Pyautomators -f json -o .//test.json
               type test.json
               '''
            }
        }
    }
}
