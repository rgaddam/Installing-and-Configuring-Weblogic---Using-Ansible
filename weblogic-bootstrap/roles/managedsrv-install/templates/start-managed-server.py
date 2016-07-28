# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}')

# Start the Managed Server
start('{{ managed_server_name }}', block='false');

# Disconnect from AdminServer
disconnect();
exit();
