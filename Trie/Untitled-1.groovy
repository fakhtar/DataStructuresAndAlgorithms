pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                checkout(
                    [ 
                        $class: 'GitSCM', 
                        branches: [
                            [name: '*/master']
                        ], 
                        doGenerateSubmoduleConfigurations: false, 
                        extensions: [], 
                        submoduleCfg: [], 
                        userRemoteConfigs: [
                            [
                                credentialsId: 'a4b1845a-c8ea-4d8d-b68f-0f6454632c14', 
                                url: 'https://git-codecommit.us-east-1.amazonaws.com/v1/repos/grants_online_form_docker'
                            ]
                        ]
                    ]
                )
            }
        }
        
        stage('Build image') {
            steps {
                echo "WORKSPACE: ${WORKSPACE}"
                sh "ls"
                // sh "docker build --build-arg APP_NAME=grants_online_form -t 853556455528.dkr.ecr.us-east-1.amazonaws.com/sihamecluster_node_externalmongo:latest -f deploy/Dockerfile ."
                sh "docker build -t sihamecluster_node_externalmongo ."
            }
        }
        
        stage('Tag image') {
            steps {
                sh "docker tag sihamecluster_node_externalmongo:latest 853556455528.dkr.ecr.us-east-1.amazonaws.com/sihamecluster_node_externalmongo:latest"   
            }
        }
        
        stage('Login to AWS') {
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding', 
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                        credentialsId: '0f965e6f-81b1-446d-830a-6744a3f0c00e', 
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                ]) {
                    //sh "aws ecr get-login --region us-east-1"
                    //sh "docker login -u ${env.AWS_ACCESS_KEY_ID} -p ${env.AWS_SECRET_ACCESS_KEY} https://853556455528.dkr.ecr.us-east-1.amazonaws.com"
                    sh "aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 853556455528.dkr.ecr.us-east-1.amazonaws.com"
                }
            }
       }
    
        stage('Push image') {
            steps {
                script {
                    // https://www.jenkins.io/doc/book/pipeline/docker/
                    //docker.withRegistry('https://853556455528.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:sihamecluster_node_externalmongo') {
                        //sh "docker push 853556455528.dkr.ecr.us-east-1.amazonaws.com/sihamecluster_node_externalmongo:latest"
                    //}
                    
                    echo "Make sure to uncomment the next line to allow pushes"
                    sh "docker push 853556455528.dkr.ecr.us-east-1.amazonaws.com/sihamecluster_node_externalmongo:latest"
                }
            }
        }
    }
}