#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/DesafioDevOps'
                bat '''
                pip3 install python-jenkins
                python3 -m pip3 install --upgrade pip3
                pip3 install virtualenv
                virtualenv env
                env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               cd Rodrigo
               python3 -m Pyautomators -f json -o .//test.json
               type test.json
               '''
            }
        }
    }
}
