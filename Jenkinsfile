/* Utility function to fetch from the folder properties the name of the cloud enviroment that student<nn>
 * is allowed to use. The value is "k8s-devops<nn>"
*/
def get_kubernetes_student_cloud() {
  def cloudName;
  withFolderProperties {
    cloudName = env.CLOUD_ENV
  }
  return cloudName
}

pipeline {
    // definition of the agent that will run the pipeline
    agent {
      kubernetes {
        cloud get_kubernetes_student_cloud()
        yamlFile 'jenkins-agents.yaml'
      }
    }
    environment {
        GIT_AUTH = credentials('jenkins-bot20')
    }
    stages {
        stage('Build and Deploy application') {
                steps {
                    withCredentials([file(credentialsId: 'aws-credentials', variable: 'FILE')]) {
                        sh 'cp $FILE .aws/credentials'
                        container(name: 'aws-cdk'){
                            sh 'mkdir ~/.aws'
                            sh 'cp .aws/* ~/.aws'

                            sh 'cdk synth && cdk deploy'
                        }
                    }
                }
            }
        }
    }
