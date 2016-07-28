# Install and Configure Oracle Weblogic Server

Ansible Playbook  to install and configure weblogic server 
All your enviroment variables can be defined in Variables.yml & passwords in password.yml and can be encrypted using ansible-vault. 

Roles includes: 
wls-install -- Installs JDK & Oracle 12c software. 
domain-install -- creates domain 
managedsrv-install -- creates managed server for application. 

Execute below command to create weblogic server.

-- ansible-playbook weblogic-bootstrap.yml --vault-password-file ~/.vault_pass.txt

After playbook is sucessfully completed you can access your weblogic server from http://localhost:7001/console. 
