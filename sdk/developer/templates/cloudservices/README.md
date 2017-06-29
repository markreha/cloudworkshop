**IoT Services Template Application**
==================
This is an Eclipse Project Template that can be imported into Eclipse to get a Spring JAX-RS project up and running quickly. This project could also be imported into Codenvy once you have checked the source code and Maven pom.xml file into your own Github repository. This project has a single REST based Service at the /weather URI with a single Service test method (i.e. onTest() in the code) that takes no parameters, which can be invoked at the /test URI. The test method simply echoes a test JSON message back to the client. The JAX-RS services are setup at the /rest URI. All JAX-RS are secured using HTTP Basic Authentication. This project also configures the SL4J Logging  Framework and a defaul Maven build file.

To build with Maven: 
- Run Maven with the clean package Maven Goals and the dev Maven Profile.

To run locally with Eclipse:
- Add a Tomcat 8.5 Server to your project. Then add the projects Web Module and set the Web Modules path to /cloudservices.

To test locally with Eclipse and Tomcat: 
- Access the following URL: http://localhost:8080/cloudservices/rest/weather/test using CloudWorkshop/dGVzdHRlc3Q= for access credentials
