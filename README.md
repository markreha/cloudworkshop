
**Getting Started with the Cloud and IoT Workshop SDK**
==================
The Cloud and IoT Workshop SDK contains all the documentation and sample Reference applications (REST Services, Reporting, and Raspberry Pi Sense HAT) required to build a simple, scalable, Cloud based suite of IoT applications.

![IoT Logical Architecture](/sdk/docs/architecture/images/logical.png)

SDK Contents
--------
This SDK is organized into a number of folders. It should be noted that all directories in this markup are indicated in ***bold italic*** text.
 - The '[***developer***](#developer-directory-contents)' folder: contains starter Java Spring and PHP Laravel template projects 
 - The '[***docs***](#docs-directory-contents)' folder: contains Database, JavaDoc, PhpDoc, and Architecture documentation, you should start here 
 - The '[***pi***](#pi-directory-contents)' folder: contains sample Raspberry Pi Sense HAT application and discrete component IoT applications 
 - The '[***tools***](#tools-directory-contents)' folder: contains misc. documentation generation tools

Getting Started
--------
You should start by first reading the Architecture decks and JavaDoc as well as the PhpDoc all located in the [***docs***](/sdk/docs/development/README.md) directory in the SDK. You should also make sure you are comfortable with the following technologies, frameworks, and tools:
1)  Java, Spring Framework (Core, Security, JDBC), Maven, and JAX-RS. These technologies and frameworks will be used to build the IoT Services application.
2) Laravel PHP, LavaCharts, and Guzzle. These technologies and frameworks will be used to build the IoT Reporting application.
3) Github, SourceTree, Eclipse Neon, MySQL Workbench, Apache Tomcat 8.5, and PostMan. These tools will be used to support building all of the IoT applications.

Development Tools Installation
--------
For desktop development you will need to download and install the following tools. If you use the Cloud based Codeenvy IDE than you will not be required to install ANY development tools!
1. Eclipse Neon for Java EE platform: Download [here](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/neon3) and/or use cloud based the Codenvy IDE.
2. Eclipse Neon for PHP platform: Download [here](http://www.eclipse.org/downloads/packages/eclipse-php-developers/neon3) and/or use the cloud based Codenvy IDE.
3. Tomcat 8.5: Download [here](http://www.eclipse.org/downloads/packages/eclipse-php-developers/neon3) and/or use the cloud based Codenvy IDE.
4. SourceTree: Download [here](https://www.sourcetreeapp.com) and/or use the Chrome Browser.
5. MySQL Workbench: Download [here](https://dev.mysql.com/downloads/workbench/) and/or use the MySQL Admin Chrome Plugin, which can be dowloaded from the [Chrome WebStore](https://chrome.google.com/webstore/) (search for MySQL Admin).
6. PostMan: Download [here](www.getpostman.org) and/or use the Postman Chrome Plugin, which can be dowloaded from the [Chrome WebStore](https://chrome.google.com/webstore/) (search for Postman).

Next Steps
--------
After you are become familiar with the architecture, sample applications, and tools you can start building your own IoT applications using the sample Reference applications in the SDK as a guide. As a developer, there are application build instructions for developing in the Cloud based Cloudenvy IDE or desktop Eclipse Neon IDE. All code is maintained in the Github Cloud based source control system and deployed to the Cloud based OpenShift PaaS. It should be noted that there is nothing technically preventing you from deploying these application to other Clouds such as Amazon AWS. See the ['README'](/sdk/docs/development/README.md) file and 'Cloud Setup Notes text' file located in the [***docs/development***](/sdk/docs/development/README.md) folder to get started building your own IoT applications.

----------

----------

Developer Directory Contents
----------
This directory contains the contains starter Java Spring and PHP Laravel template projects. You can import these into your IDE to get the basic scaffolding for a starter IoT Services application and an IoT Reporting application.

 - ***cloudapp***: this folder contains a basic PHP Laravel Project with the "Hello World" page along with the Guzzle and LavaCharts libraries added.
 - ***cloudservices***: this folder contains a basic Java Spring Project with "Test" REST API configured along with basic SLF4J configuration.

[Back to Top](#getting-started-with-the-cloud-and-iot-workshop-sdk)

----------

Docs Directory Contents
----------
This directory contains all of the documentation for the IoT SDK. This is where all developers should start!

 - ***architecture***: this folder contains all of the high level architecture documents.
 - ***database***: this folder contains the database design (ER Diagram) and DDL script that can be used to build the database and tables to support the IoT Reference applications.
 - ***development***: this folder contains the developer documentation that can be referenced when setting up the Development Environment and configuring the Cloud Environments. See the README markup file in this folder for all the details.
 - ***javadoc***: this folder contains the JavaDoc for the Reference IoT Services application.
 - ***phpdoc***: this folder contains the PhpDoc for the Reference IoT Reporting application.
 - ***testing***: this folder contains the Postman Test Scripts that can be used when testing the Reference IoT Services application and its associated REST API's.
 - ***training***: this folder contains the Workshop Training decks.

[Back to Top](#getting-started-with-the-cloud-and-iot-workshop-sdk)

----------

Pi Directory Contents
----------
This directory contains the contains Reference IoT Device application that can be used with any Raspberry Pi 3 and Sense HAT or a Raspberry Pi 3 DHT11 and LED wired to a breadboard. The Reference application can be used as a starting point to monitor Weather IoT data.

 - ***app/hat***: this folder contains the Python 3 code for the Reference IoT Device application using a Sense HAT.
 - ***app/discrete***: this folder contains the Python 3 code for the Reference IoT Device application using the DHT11 and LED discrete components.

[Back to Top](#getting-started-with-the-cloud-and-iot-workshop-sdk)

----------

Tools Directory Contents
----------
This directory contains a few miscellaneous tools to support building the code and documentation for the IoT applications.

 - ***phpdocumentor***: this folder contains the PHP Archive (phar file) that can be used to generate standard HTML documentation for any PHP projects.
 - ***yworks***: this folder contains the documentation and Java Archive (jar file) that creates and embeds UML class diagrams within standard JavaDoc.

[Back to Top](#getting-started-with-the-cloud-and-iot-workshop-sdk)