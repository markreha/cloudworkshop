# Active environment
environment = "dev1"

# Sample time in ~seconds (not very accurate in sleep)
sampleTime = 20

# True if print debug statements
debug = True

# Device ID for this PI
deviceID = 0

# Different environment configurations
env_dev1 = {'webApi': 'http://marks-macbookair.local:8080/cloudservices/rest/dht11/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_dev2 = {'webApi': 'http://node5.codenvy.io:37551/cloudservices/rest/dht11/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_qa = {'webApi': 'http://cloud-services-playlaravel.44fs.preview.openshiftapps.com/cloadservices/rest/dht11/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_prod = {'webApi': 'http://cloud-services-playlaravel.44fs.preview.openshiftapps.com/cloadservices/rest/dht11/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
