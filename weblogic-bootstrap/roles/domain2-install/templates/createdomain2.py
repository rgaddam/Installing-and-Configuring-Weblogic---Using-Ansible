# Set AdminServer connection URL
ADMIN_SERVER_URL = 't3://' + '10.52.65.3' + ':' + '7001';

# Connect to the AdminServer
connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

#The path on the local machine where the template will be created,
#it should not already exist.
templatePath = '/apps/oracle/myTemplate.jar'

#get the packed template from the Administration Server
writeTemplate(templatePath)

#disconnect from online WLST connection to the Administration Server
disconnect()

#read the template that was downloaded from the Administration Server. In this
#case, the Expanded configuration of the domain is read.
readTemplate(templatePath, 'Expanded')

#specify the domain directory where the domain needs to be created
domainPath = ('/apps/oracle/platform12c_test/config/Domains/test_domain')

#create the domain
writeDomain(domainPath)
exit();
