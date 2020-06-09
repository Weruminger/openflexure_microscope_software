properties([
  parameters([
		choice(name: 'MERGE_UPSTREAM', choices: ['false','true'], description: '' ),
		choice(name: 'DO_BUILD', choices: ['true','false'], description: '' ),
		choice(name: 'DO_INSTALL', choices: ['true','false'], description: '' ),
		choice(name: 'INSTALL_ATLAS', choices: ['false','true'], description: '' ),
		choice(name: 'INSTALL_LAPACK', choices: ['false','true'], description: '' ),
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
    if("${env.INSTALL_ATLAS}" == 'true'){
        stage('Install ATLAS'){
            try{
                sh('mkdir ~/dload; mkdir ~/numeric')
            }catch(e){ println(e.message) }
            try{
                dir('dload'){
                    sh('wget https://sourceforge.net/projects/math-atlas/files/Stable/3.10.3/atlas3.10.3.tar.bz2')
                }
            }catch(e){ println(e.message) }
            try{
                dir('numerics'){
                    sh('bunzip2 -c ../dload/atlas3.10.3.tar.bz2 | tar xfm - ; mv ATLAS ATLAS3.10.3')
                }
            }catch(e){ println(e.message) }
            dir('numerics/ATLAS3.10.3/Linux_ARM6'){
                try{
                    sh('../configure -b 64 -D c --prefix=/home/whaley/lib/atlas --with-netlib-lapack-tarfile=/home/whaley/dload/lapack-3.4.1.tgz')
                }catch(e){ println(e.message) }
                try{
                     sh('make build')
                }catch(e){ println(e.message) }
                try{
                    sh('make check')
                }catch(e){ println(e.message) }
                try{
                    sh('make ptcheck')
                }catch(e){ println(e.message) }
                try{
                    sh('make time')
                }catch(e){ println(e.message) }
                try{
                    sh('sudo make install')
                }catch(e){ println(e.message) }
            }
        }
    }
	stage('Build'){
		if ("${env.DO_BUILD}" == 'true' ){
	    sh('sudo python3 setup.py build')
	    sh('sudo python3 setup.py install')
		}
	}
}
