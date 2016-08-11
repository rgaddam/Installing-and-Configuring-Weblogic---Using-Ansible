# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL)

# Start the Managed Server_2
start('{{ managed_server_name_2 }}', block='false');

# Disconnect from AdminServer
disconnect();
exit();
