pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejpdocker'
            }
        }
        stage ("Test"){
            steps{
               sh 'cd leonardo/Extra'
               sh 'python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
