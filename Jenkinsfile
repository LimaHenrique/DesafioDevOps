#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                bat '''
                start cmd.exe pip install python-jenkins
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
               start cmd.exe cd Rodrigo
               start cmd.exe python -m Pyautomators -f steps -o .//rodrigo.steps
               start cmd.exe type rodrigo.json
               '''
            }
        }
    }
}
