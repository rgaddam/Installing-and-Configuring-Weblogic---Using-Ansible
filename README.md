# Install and Configure Oracle Weblogic Server & Cluster Configuration -- Using Ansible
Ansible Playbook to install and configure weblogic server & cluster configuration 

All enviroment variables are defined in Variables.yml & passwords in password.yml and can be encrypted using ansible-vault. 

Roles includes: 

wls-install -- Installs JDK & Oracle 12c software. 

domain-install -- creates domain 

managedsrv-install -- creates managed server for application. 

managedsrv2-install -- creates manged server 2 for application 

domain2-install -- Connects to admin server creates a domain template and expands configuration of the domain to 2nd managedserver and 
create the domain on 2nd server. 

cluster-config --  create cluster and add the managed servers to cluster. ( need to run this in offline mode)

** Note Need to restart the Weblogic server to get the cluster setup active. 


Execute below command to create weblogic server.

-- ansible-playbook weblogic-bootstrap.yml --vault-password-file ~/.vault_pass.txt

After playbook is sucessfully completed you can access your weblogic server from http://localhost:7001/console. 
