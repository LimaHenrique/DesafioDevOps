#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                bat '''
                env/Scripts/activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               cd Rodrigo
               python -m Pyautomators -f json -o test.json
               type test.json
               '''
            }
        }
    }
}
