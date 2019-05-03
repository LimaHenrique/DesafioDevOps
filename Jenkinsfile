#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                bat '''
                start cmd.exe /c env/Scripts/activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               start cmd.exe /c cd Rodrigo
               start cmd.exe /c python -m Pyautomators -f json -o test.json
               start cmd.exe /c type test.json
               '''
            }
        }
    }
}
