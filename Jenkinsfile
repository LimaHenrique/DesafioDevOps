#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                powershell label: '', script: 'pip install python-jenkins'
                powershell '''
                script: 'pip install python-jenkins
                python -m pip install --upgrade pip
                pip install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               powershell '''
               cd Rodrigo
               python -m Pyautomators -f json -o .//test.json
               type test.json
               '''
            }
        }
    }
}
