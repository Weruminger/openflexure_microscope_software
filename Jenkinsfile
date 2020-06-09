properties([
  parameters([
		choice(name: 'MERGE_UPSTREAM', choices: ['false','true'], description: '' ),
		choice(name: 'DO_BUILD', choices: ['true','false'], description: '' ),
		choice(name: 'DO_INSTALL', choices: ['true','false'], description: '' ),
		string(name: 'BRANCH_TO_FETCH', defaultValue: 'master', description: '' )
   ])
])

node{

    stage('init'){
			  
			  echo 'Do Checkout'
        
			  checkout([$class: 'GitSCM', 
									branches: [[name: "${env.BRANCH_TO_FETCH ?: 'master'}"]],
									doGenerateSubmoduleConfigurations: false, 
									extensions: [], 
									submoduleCfg: [], 
									userRemoteConfigs: [[credentialsId: 'GitHubWerumingerI', 
																			 url: 'https://github.com/Weruminger/openflexure_microscope_software.git']]])
    }
	stage('Build'){
		if ("${env.DO_BUILD}" == 'true' ){
	    sh('sudo python3 setup.py build')
	    sh('sudo python3 setup.py install')
		}
	}
}
