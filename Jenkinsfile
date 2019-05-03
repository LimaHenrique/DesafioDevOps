#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                bat '''
                start cmd pip install python-jenkins
                start cmd python -m pip install --upgrade pip
                start cmd pip install virtualenv
                start cmd virtualenv env
                start cmd env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               start cmd.exe cd Rodrigo
               start cmd.exe python -m Pyautomators -f json -o .//rodrigo.json
               start cmd.exe type rodrigo.json
               '''
            }
        }
    }
}
