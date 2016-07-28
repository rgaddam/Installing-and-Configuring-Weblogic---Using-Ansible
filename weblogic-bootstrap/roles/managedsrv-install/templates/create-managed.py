# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Start editing mode
edit();
startEdit();

# Declare the machine that hosts the Managed Server
cd('/')
cmo.createMachine('{{ server_hostname }}')

# Configure the nodemanager for that machine
cd('/Machines/' + '{{ server_hostname }}' + '/NodeManager/' + '{{ server_hostname }}')
cmo.setListenAddress('{{ node_manager_listen_address }}')

# Create the Managed Server
cd('/')
cmo.createServer('{{ managed_server_name }}')

# Setup the managed Server configurations
cd('/Servers/' + '{{ managed_server_name }}')
cmo.setListenAddress('{{ server_hostname }}')
cmo.setListenPort({{ managed_server_port }})

# Assign the Managed server to the hosting machine (create a sort of dependencie relation)
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))

# Save changes
save();
activate(block='true');

# Log out from AdminServer
disconnect();
exit();
