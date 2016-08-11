# Set AdminServer connection URL
#ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
#connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

# Read Domain 
readDomain('{{ domain_home }}')

# Start editing mode
edit();
startEdit();

# Create and configure a cluster and assign the managedsrv1 and managedsrv2 Managed Servers to that cluster.

print('Creating Cluster - {{ cluster_name }} and adding {{ managed_server_name }}, {{ managed_server_name_2 }}')

cd('/')
create('{{ cluster_name }}', 'Cluster')
assign('Server', '{{ managed_server_name }},{{ managed_server_name_2 }}','Cluster','{{ cluster_name }}')

cd('Cluster/{{ cluster_name }}')
set('ClusterMessagingMode', 'unicast')

# Update the domain 
updateDomain()
exit();
