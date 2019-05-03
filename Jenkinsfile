#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                bat '''
                start cmd.exe env/Scripts/activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               start cmd.exe cd Rodrigo
               start cmd.exe python -m Pyautomators -f json -o test.json
               start cmd.exe type test.json
               '''
            }
        }
    }
}
