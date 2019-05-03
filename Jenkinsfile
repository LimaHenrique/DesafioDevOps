#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                bat '''
                bat start cmd.exe pip install python-jenkins
                start cmd.exe python -m pip install --upgrade pip
                start cmd.exe pip install virtualenv
                start cmd.exe virtualenv env
                start cmd.exe env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               cd Gustavo/localExtra/
               python -m Pyautomators -f json -o gustavo.json
               cd ../../Leonardo/Extra/
               python -m Pyautomators -f json -o leonardo.json
               '''
            }
        }
    }
}
