**Getting Started Building the IoT Apps**
==================
The Cloud and IoT Workshop SDK contains all the documentation, sample applications (REST Services, Reporting, and Raspberry Pi Sense HAT) required to build a simple, scalable, Cloud based suite of IoT applications. The following assumes you have a Github, Codenvy, and OpenShift accounts.

To get started you should first Clone the SDK from Github: https://github.com/markreha/cloudworkshop then create two repositories 'cloudservices' and 'cloud app' in your Github account. Then from the SDK copy all the respective files from each of the developer/teampltes folders to your respective Github repositories. Note, bulk file upload can be done in GitHub using your browser but you must use the Chrome browser. If you use the Sourcetree GIT Client then make sure you configure (via .gitgnore file) your local GIT repository so that hidden files are also uploaded. The template projects are starter projects contains all the scaffolding Java Spring Maven files and all the scaffolding PHP Laravel files to build "working" applications. These starter projects can be used as a baseline when building your IoT set of applications. 

If you want complete working with completely working end to end IoT Reference applications you can clone the following Github repositories:
1) IoT Services App: https://github.com/markreha/cloudservices
2) IoT Reporting App: https://github.com/markreha/cloudapp
You can then use the project import steps as outlined below for the IoT Template applications.

Building the IoT Services Template App
--------
To build in Codenvy:
1. Import the Codeenvy Custom Tomcat MySQL Stack Recipe Stack located in the docs/development directory.
2. Create a new Workspace using the Java-MySQL-Mark runtime (created from step #1).
3. Start your Workspace.
4. Create a new Project by importing your Github 'cloudservices' repository.
5. See the Cloud Setup Notes for instructions how to setup the database and command tools in Codeny.

To build in Eclipse Neon:
1. Create a new Workspace.
2. Import the 'cloudservices' template from the SDK (making sure you check the 'copy' checkbox when importing).
3. Add a Tomcat 8.5 server to your Workspace.
4. Create a Maven Run Configuration using the clean package goals and the dev profile.
5. See the IoT.sql DDL script in the SDK to create your Database Schema.
6. Add the Project to your Tomcat Server (using the /cloudservices path for your web module.

Building the IoT Reporting Template App
--------
To build in Codenvy:
1. Create a new Workspace using the PHP runtime.
3. Start your Workspace.
4. Create a new Project by importing your Github 'cloudapp'  repository.
5. See the Cloud Setup Notes for instructions how to setup the command tools in Codeny.

To build in Eclipse Neon:
1. Create a new Workspace.
2. Import the 'cloudapp' template from the SDK (making sure you check the 'copy' checkbox when importing).
3. Setup an ANT build file to copy files from your Workspace to your MAMP runtime hotdogs directory.

Next Steps
--------
After you are able to build template projects then you are ready to start customizing the application functionality as per the requirements in the sample applications. All code should be maintained in the Github cloud based source control system because code deployed to the OpenShift PaaS cloud uses Github as the source repository. See the Cloud Setup Notes file located in the developer folder to get started with OpenShift to deploy your IoT applications to the cloud.
