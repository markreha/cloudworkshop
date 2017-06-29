This is an Eclipse Project Template that can be imported into Eclipse to get a Spring JAX-RS project up and running quickly. This project has a single REST based Service at the /weather URI with a single Service test method (i.e. onTest() in the code) that takes no parameters, which can be invoked at the /test URI. The test method simply echoes a test JSON message back to the client. The JAX-RS services are setup at the /rest URI. All JAX-RS are secured using HTTP Basic Authentication. This project also configures the SL4J Logging  Framework and a defaul Maven build file. The web module path should be set to /cloudservices.

To build: Run Maven with the clean package goals and the dev profile.

To test locally: http://localhost:8080/cloudservices/weather/rest/test using CloudWorkshop/dGVzdHRlc3Q= for access credentials
