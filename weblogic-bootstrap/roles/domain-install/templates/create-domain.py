domain_application_home = '{{ applications_home }}/{{ domain_name }}'
domain_configuration_home = '{{ domains_home }}/{{ domain_name }}'
domain_name = '{{ domain_name }}'
java_home = '{{ jdk_folder }}/jdk1.8.0_91'
middleware_home = '{{ middleware_home }}'
node_manager_home = '{{ nodemanager_home }}'
weblogic_home = '{{ weblogic_home }}'

weblogic_template=weblogic_home + '/common/templates/wls/wls.jar';
#em_template=middleware_home + '/em/common/templates/wls/oracle.em_wls_template_12.2.1.jar';

readTemplate(weblogic_template);
setOption('DomainName', domain_name);
setOption('OverwriteDomain', 'true');
setOption('JavaHome', java_home);
setOption('ServerStartMode', 'prod');
setOption('NodeManagerType', 'CustomLocationNodeManager');
setOption('NodeManagerHome', node_manager_home);
cd('/Security/base_domain/User/weblogic');
cmo.setName('{{ weblogic_admin }}');
cmo.setUserPassword('{{ weblogic_admin_pass }}');
cd('/');

print "SAVE DOMAIN";
writeDomain(domain_configuration_home);
closeTemplate();

print 'READ DOMAIN';
readDomain(domain_configuration_home);

#print 'ADD TEMPLATES';
#addTemplate(em_template);
#addTemplate(jrf_template);
#addTemplate(coherence_template);
#setOption('AppDir', domain_application_home);

cd("/SecurityConfiguration/" + domain_name);
cmo.setNodeManagerUsername('{{ nodemanager_username }}');
cmo.setNodeManagerPasswordEncrypted('{{ nodemanager_password }}');

cd('/Server/' + '{{ admin_server_name }}');
create('{{ admin_server_name }}','SSL');
cd('SSL/' + '{{ admin_server_name }}');
cmo.setHostnameVerificationIgnored(true);
cmo.setHostnameVerifier(None);
cmo.setTwoWaySSLEnabled(false);
cmo.setClientCertificateEnforced(false);

cd('/SecurityConfiguration/'+ domain_name +'/Realms/myrealm');
cd('AuthenticationProviders/DefaultAuthenticator');
set('ControlFlag', 'SUFFICIENT');
cd('../../');

updateDomain();
closeDomain();
