# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Start editing mode
edit();
startEdit();

# Declare the machine that hosts the Managed Server
cd('/')
cmo.createMachine('{{ server_hostname_2 }}')

# Configure the nodemanager for that machine
cd('/Machines/' + '{{ server_hostname_2 }}' + '/NodeManager/' + '{{ server_hostname_2 }}')
cmo.setListenAddress('{{ node_manager_listen_address_2 }}')

# Create the Managed Server
cd('/')
cmo.createServer('{{ managed_server_name_2 }}')

# Setup the managed Server configurations
cd('/Servers/' + '{{ managed_server_name_2 }}')
cmo.setListenAddress('{{ server_hostname_2 }}')
cmo.setListenPort({{ managed_server_port_2 }})

# Assign the Managed server to the hosting machine (create a sort of dependencie relation)
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname_2 }}'))

# Save changes
save();
activate(block='true');

# Log out from AdminServer
disconnect();
exit();
