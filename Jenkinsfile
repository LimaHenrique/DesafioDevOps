#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                sh '''
                pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env/Scripts/activate
                '''
            }
        }
        stage ("Test"){
            steps{
               sh '''
               cd Rodrigo
               python -m Pyautomators -f json -o rodrigo.json
               type rodrigo.json
               '''
            }
        }
    }
}
