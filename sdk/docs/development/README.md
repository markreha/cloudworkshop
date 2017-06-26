**Getting Started Building the IoT Apps**
==================
The Cloud and IoT Workshop SDK contains all the documentation, sample applications (REST Services, Reporting, and Raspberry Pi Sense HAT) required to build a simple, scalable, Cloud based suite of IoT applications. The following assumes you have setup Github, Codenvy, and OpenShift accounts.

Get the SDK and Code
--------------------

To get started building the IoT Template apps please perform the following steps. The Template projects are starter projects contains all the scaffolding Java Spring Maven files and all the scaffolding PHP Laravel files to enable you to start building "working" applications. These starter projects can be used as a baseline when building your IoT set of applications. You will first need to create a Github account if you do not have one already.

 1. [Clone the SDK](https://github.com/markreha/cloudworkshop) to your local file system.
 2. Create two repositories 'cloudservices' and 'cloudapp' in your Github account.
 3. Copy all of the files from the SDK ***/sdk/developer/templates/cloudservices*** folder to your Github 'cloudservices' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 4. Copy all of the files from the SDK ***/sdk/developer/templates/cloudapp*** folder to your Github 'cloudapp' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 5. Create local GIT repositories using the Sourcetree GIT Client using the Github repositories created in the previous steps. Make sure your local GIT repositories are configured properly to manage hidden files (via .gitignore file) so that hidden files are also uploaded.

To get started building the IoT Reference apps please perform the following steps. The Reference apps are fully working IoT applications that you can build and modify as desired.

 1. [Clone the IoT Cloud Services Reference app ](https://github.com/markreha/cloudservices) to your local file system. [Clone the IoT Cloud Reporting Reference app ](https://github.com/markreha/cloudapp) to your local file system.
 2. Create two repositories 'cloudservices' and 'cloudapp' in your Github account.
 3. Copy all of the files from the cloned IoT Cloud Services Reference app to your Github 'cloudservices' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 4. Copy all of the files from the cloned IoT Cloud Reporting Reference app to your Github 'cloudapp' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 5. Create local GIT repositories using the Sourcetree GIT Client using the Github repositories created in the previous steps. Make sure your local GIT repositories are configured properly to manage hidden files (via .gitignore file) so that hidden files are also uploaded.

Other documents located in this directory that you need to review and reference include:

* Codenvy and OpenShift Setup Notes - Cloud Setup Notes.txt
* Codenvy Tomcat / MySQL Stack Recipe - Codeenvy Custom Tomcat MySQL Stack Recipe.txt
* Codenvy PHP Workspace Recipe - Codenvy CloudApp Recipe.txt
* Codenvy Tomcat / MySQL Workspace Recipe - Codenvy CloudServices Recipe.txt
* OpenShift Getting Started Guide - OpenShift_Online-3-Getting_Started-en-US.pdf *

You can now use the steps outlined below for setting up your development environment and building the IoT Template applications or building the IoT Reference applications.

Setup your Development Environment
--------------------
It is recommended to use the Cloud based Codenvy IDE as your development environment. This saves you from all the time and complexity of setting up Eclipse, MySQL, and Tomcat in your local environment. However, if you wish, the Template and Reference apps have been built and validated in both the Codenvy IDE and Eclipse IDE so you are also free to setup a local development environment using Eclipse, MySQL, and Tomcat. You will want to reference [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

Build the IoT Services App
--------
To build in Codenvy:
1. Import the Codeenvy Custom Tomcat MySQL Stack Recipe Stack located in the docs/development directory.
2. Create a new Workspace using the Java-MySQL-Mark runtime (created from step #1).
3. Start your Workspace.
4. Create a new Project by importing your Github 'cloudservices' repository.
5. See the 'Cloud Setup Notes.txt' located in this directory for instructions how to setup the database and command tools in Codeny.

To build in Eclipse Neon:
1. Create a new Workspace.
2. Import the 'cloudservices' template from the SDK (making sure you check the 'copy' checkbox when importing).
3. Add a Tomcat 8.5 server to your Workspace.
4. Create a Maven Run Configuration using the clean package goals and the dev profile.
5. See the IoT.sql DDL script in the SDK to create your Database Schema.
6. Add the Project to your Tomcat Server (making sure you use the /cloudservices path for your web module).

Build the IoT Reporting App
--------
To build in Codenvy:
1. Create a new Workspace using the PHP runtime.
3. Start your Workspace.
4. Create a new Project by importing your Github 'cloudapp'  repository.
5. See the 'Cloud Setup Notes.txt' located in this directory for instructions how to setup the command tools in Codeny.

To build in Eclipse Neon:
1. Create a new Workspace.
2. Import the 'cloudapp' template from the SDK (making sure you check the 'copy' checkbox when importing).
3. Setup an ANT build file to copy files from your Workspace to your MAMP runtime hotdogs directory (see Reference App for example).

Next Steps
--------
After you are able to build template projects then you are ready to start customizing the application functionality as per the requirements in the sample applications. All code should be maintained in the Github cloud based source control system because code deployed to the OpenShift PaaS cloud uses Github as the source repository. See the Cloud Setup Notes file located in the developer folder to get started with OpenShift to deploy your IoT applications to the cloud.
