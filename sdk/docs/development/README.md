**Getting Started Building the IoT Apps**
==================
The Cloud Workshop SDK contains all the documentation, tools, and sample template applicationsrequired to build a simple, scalable, Cloud based suite of IoT applications. The following assumes you have setup Github, Codenvy, and OpenShift, Azure, Google Cloud, Heroku, or Amazon AWS accounts.

![IoT Logical Architecture](../architecture/images/logical.png)

----------

Follow These Easy Steps
-----------------------

Step 1: [Get the SDK and read the Documentation](#get-the-sDK-and-code)

Step 2: [Setup IoT Services Application Local and Codenvy Development Environment](#setup-your-java-mysql-development-environment)

Step 3: [Setup the IoT Reporting Application Local and Codenvy Development Environment](#setup-your-php-development-environment)

Step 4: [Build and configure the IoT Services Application Localy and on Codenvy](#build-the-iot-services-app)

Step 5: [Deploy the IoT Services Application to the OpenShift Cloud](#deploy-the-iot-services-app-to-openshift) or [the Azure Cloud](#deploy-the-iot-services-app-to-azure) or [the Google Cloud Platform](#deploy-the-iot-services-app-to-google-cloud-platform) or [the Heroku Cloud](#deploy-the-iot-services-app-to-heroku-cloud) or [the Amazon Cloud](#deploy-the-iot-services-app-to-amazon-cloud)

Step 6: [Build and configure the IoT Reporting Application](#build-the-iot-reporting-app)

Step 7: [Deploy the IoT Reporting Application to the OpenShift Cloud](#deploy-the-iot-reporting-app-to-openshift) or [the Azure Cloud](#deploy-the-iot-reporting-app-to-azure) or [the Google Cloud Platform](#deploy-the-iot-reporting-app-to-google-cloud-platform) or [the Heroku Cloud](#deploy-the-iot-reporting-app-to-heroku-cloud) or [the Amazon Cloud](#deploy-the-iot-reporting-app-to-amazon-cloud)

After you are able to build and configure the Template applications or the Reference applications you are then ready to start customizing the applications functionality as per your own IoT requirements or per the functionality implemented in the Reference applications. 

Remember, all code should be maintained in the Github Cloud based source control system because code deployed to the Codenvy Cloud IDE and all PaaS Clouds both uses Github as the source repository.

----------


Get the SDK and Code
--------------------

To get started first clone the SDK to your local file system and then create your remote repositories in Github for the two IoT applications required to support an end to end working IoT application. You will first need to create a Github account if you do not have one already. Moving forward all application code should be maintained in your own local and remote Github repositories because any code imported or managed by the Codenvy Cloud IDE and build/deployed to the OpenShift PaaS or Azure Cloud will use Github as the source repository.
 1. [Clone the SDK](https://github.com/markreha/cloudworkshop) to your local file system or local GIT repository. 
 2. Create two repositories 'cloudservices' and 'cloudapp' in your Github account.

To get started building the IoT Template apps OR the IoT Reference apps please perform the following steps.

If you plan on using the IoT Template apps to start your development then please perform the following steps. The Template projects are starter projects containing all the scaffolding Java Spring Maven files and all the scaffolding PHP Laravel files to enable you to start building "working" applications. These starter projects can be used as a baseline when building your IoT set of applications.
 1. Copy all of the files from the SDK ***/sdk/developer/templates/cloudservices*** folder to your remote Github 'cloudservices' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 2. Copy all of the files from the SDK ***/sdk/developer/templates/cloudapp*** folder to your remote Github 'cloudapp' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser.
 3. Create local GIT repositories using the Sourcetree GIT Client by cloning the Github repositories created in the previous steps. Make sure your local GIT repositories are configured properly to manage hidden files (via .gitignore file) so that hidden files are also uploaded.

If you plan on using the IoT Reference apps to start your development then please perform the following steps. The Reference apps are fully working IoT applications that you can build and modify as desired. These projects can be used if you want to quickly get fully working code to build and deploy with minimal effort and without worrying too much about the technical details, which can be picked up by studying the source code and working thru appropriate tutorials.

 1. [Clone the IoT Cloud Services Reference app ](https://github.com/markreha/cloudservices) to your local file system or local GIT repository. 
 2. [Clone the IoT Cloud Reporting Reference app ](https://github.com/markreha/cloudapp) to your local file system or local GIT repository.
 3. If you havn't already create two remote repositories 'cloudservices' and 'cloudapp' in your Github account.
 4. If you cloned files to your local file system (and not GIT) then you will need to copy all of the files from the cloned IoT Cloud Services Reference app to your remote Github 'cloudservices' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser. If cloned file to your local GIT repository then you will not to push all the fils to your remote Github 'cloudservices' repository. Make sure your local GIT repositories are configured properly to manage hidden files (via .gitignore file) so that hidden files are also uploaded.
 5. If you cloned files to your local file system (and not GIT) then you will need to copy all of the files from the cloned IoT Cloud Reporting Reference app to your remote Github 'cloudapp' repository. Note, bulk file upload can be done in Github using your browser but you must use the Chrome browser. If cloned file to your local GIT repository then you will not to push all the fils to your remote Github 'cloudseapp' repository. Make sure your local GIT repositories are configured properly to manage hidden files (via .gitignore file) so that hidden files are also uploaded.
 
 There are a number of training screencasts to help you with your development. All of the screencasts are in the SDK and located in the **/sdk/docs/training/screencasts** directory.
 
Additional documents located in this directory that you need to review and reference include:

* Codenvy, OpenShift, and Azure Cloud Setup Notes - [Cloud Setup Notes](Cloud%20Setup%20Notes.txt)
* Codenvy Tomcat / MySQL Stack Recipe - Codeenvy Custom Tomcat MySQL Stack Recipe.txt
* Codenvy PHP Workspace Recipe - Codenvy CloudApp Recipe.txt
* Codenvy Tomcat / MySQL Workspace Recipe - Codenvy CloudServices Recipe.txt
* OpenShift Getting Started Guide - OpenShift_Online-3-Getting_Started-en-US.pdf

There are API documentation for each application:
* [REST API](https://markreha.github.io/cloudworkshop/sdk/docs/swagger/)
* [Service JavaDoc](https://markreha.github.io/cloudworkshop/sdk/docs/javadoc/)
* [App PhpDpc](https://markreha.github.io/cloudworkshop/sdk/docs/phpdoc/)

You can now use the steps outlined below for setting up your development environment and building the IoT Template applications or building the IoT Reference applications.

Setup your Java MySQL Development Environment
--------------------
It is recommended to use the Cloud based Codenvy IDE as your development environment. This saves you from all the time and complexity of setting up Eclipse, MySQL, and Tomcat in your local environment. However, if you wish, the Template and Reference apps have been built and validated in both the Codenvy IDE and Eclipse IDE so you are also free to setup a local development environment using Eclipse, MySQL, and Tomcat. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

To build in Codenvy:
 1. Log onto Codenvy. 
 2. Click on the Stacks menu from the left Main Menu.
 3. Scroll down to the Java-MySQL stack and click the 'Duplicate stack'
 4. Click on the newly created Java-MySQL stack to edit the stack configuration. In the Name field rename your new stack to 'Java-MySQL-Workshop' (no quotes). Under the Runtimes click under the Machines on the 'Down arrow' icon for the DB. Change the Source field from 'eclipse/mysql' to 'kaloyanraev/mysql-no-volume' (no quotes). This will change the Docker image to an image that works around a bug in the default image where the MySQL database is not maintained during the image snapshotting (and losses all data in the database).
 5. Click the Test button to validate your new stack. Make sure both the Tomcat 'dev-machine' and the MySQL 'db' environments all started without errors. This can be done by looking at the two respective terminal console output at the bottom of the Codenvy IDE.
 6. Click the Save button.
 7. Click on the Workspaces menu from the left Main Menu.
 8. Click the Add Workspace button.
 9. In the Workspace name field rename the Workspace to 'cloudservices' (no quotes).
 10. Select the Runtime icon.
 11. Select the Java-MySQL-Workshop runtime.
 12. Click the Save button.
 13. It is also recommended that you install the Postman Chrome Plugin and MySQL Admin Chrome Plugin.

To build in Eclipse, Tomcat, and MAMP:
 1. Install Eclipse EE. Start Eclipse and create a new empty Workspace. 
 2. Click on the Servers tab. Click on the 'create new server' link.
 3. Select Tomcat 8.5 under the Apache section. Click the Next button. 
 4. Click the Browse button and navigate to the root directory of the Tomcat installation. Click the Next button.
 5. Click the Finish button. The new Tomcat server should be listed in the Servers tab.
 6. Click the Start icon to validate that the Tomcat server starts and runs without errors.
 7. Start MySQL Workbench and connect MySQL Workbench to your local MySQL database to ensure that you can connect to the database.

To build in Eclipse, Jetty, and MAMP:
 1. Install Eclipse EE. Start Eclipse and create a new empty Workspace. 
 2. Go to Eclipse Marketplace, search for Jetty, and install the Eclipse Jetty plugin.
 3. Setup Run Configuration in Eclipse:
* Set Project to local Eclipse Project
* Scan for WebApp Folder, select WebContent option
* Set context to /cloudservices
* Under Options select the option to use the external Jetty runtime
* Under Environment set a variable JVM variable -Djetty.come=[path to your Jetty install]
* Under Dependencies uncheck all the Tomcat librarires
* Under Classpath add a Classpath entry to config/dev directory to pick up config.properties, web.xml, and log4j.xml configuration files
* Click the Run menu to run Jetty
4. Start MySQL Workbench and connect MySQL Workbench to your local MySQL database to ensure that you can connect to the database.

Setup your PHP Development Environment
--------------------
It is recommended to use the Cloud based Codenvy IDE as your development environment. This saves you from all the time and complexity of setting up Eclipse and MAMP in your local environment. However, if you wish, the Template and Reference apps have been built and validated in both the Codenvy IDE and Eclipse IDE so you are also free to setup a local development environment using Eclipse, and MAMP. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

To build in Codenvy:
 1. Log onto Codenvy. 
 2. Click on the Workspaces menu from the left Main Menu.
 3. Click the Add Workspace button.
 4. In the Workspace name field rename the Workspace to 'cloudapp' (no quotes).
 5. Select the Runtime icon.
 6. Select the PHP runtime.
 7. Click the Save button.

To build in Eclipse and MAMP:
 1. Install Eclipse PHP Oxygen. Start Eclipse and create a new empty Workspace. 
 2. Install MAMP.

Build the IoT Services App
--------
The following steps can be used to configure and build the IoT Services app. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK for how to setup the database and command tools in Codeny as well as setup PHP auto deployment in your local Eclipse PHP environment.

Codenvy Build and Configuration Instructions:

 1. Start/open your 'cloudservices' Workspace. 
 2. Once the environment is up and running click the 'Import Project...' link in the left project pane. 
 3. Select the GITHUB option under the Source Control section. Enter the URL for your Github 'cloudservices' repository. Click the Import button.
 4. Select the Java Project Configuration and click the Next button.
 5. Click the Save button.
 6. Configure the application:
	 - In the src/config/dev directory update the config.properties file with your proper database credentials
	 - In the src/config/openshift directory update the config.properties file with your proper database credentials
	 - In the src/config/azure directory update the config.properties file with your proper database credentials
	 - In the src/config/heroku directory update the config.properties file with your proper database credentials
	 - In the src/config/amazon directory update the config.properties file with your proper database credentials
	 - Invoke Maven with the 'dev' Profile to build for your development environment
 7. Setup your MySQL Database. Select the Workspaces menu from the left Main Menu in Codenvy. Select your Workspace. Under the Workspace Runtime configuration expand the DB Machine,  scroll down to the Servers section, and note the address DB URL in the dbserver-3306-tcp entry. This address (URL hostname and port) will be used in MySQL Workbench OR MySQL Admin Chrome Plugin.  Start  MySQL Workbench or log into MySQL Admin as root user (username of root and password of password) and then run the IoT.sql DDL script located in the ***docs\database*** folder within the SDK. You will also need to set the privileges for the *iot* schema for the pet clinic user (username of petclinic and password of password).
 8. Setup the Commands below by selecting the Commands tab (far left under the Projects tab in the Project pane). You can create a new Command by clicking the + icon next to the Command Category. These Custom Commands should be added under the Common Commands.
 9. To build and run the project invoke the following commands from the Custom Commands:
	 - Run 'Start Tomcat' to start the Tomcat Server.
	 - Run 'Build and Deploy' to do a clean Maven build and deployment to the Tomcat Server using the desired Maven Profile.
 
**Maven Build and Deployment Command**
The IoT Services Reference Application uses Maven Profiles to select the appropriate configuration files for the target Cloud Platform. The Maven Profiles are setup on the Maven POM file located in the SDK. The Maven Profile names basically use the platform folder in the src/config/[PROFILE] directory structure.
 Command Name: 
 	<pre>Build and Deploy</pre>
 Command Line:
	<pre>mvn clean package -f ${current.project.path} -P[MAVEN_PROFILE]
	echo Deploying ${current.project.path}/target/cloadservices.war to $TOMCAT_HOME/webapps/cloudservices.war ......
	cp ${current.project.path}/target/cloadservices.war $TOMCAT_HOME/webapps/cloudservices.war
	echo Deployed ${current.project.path}/target/cloadservices.war</pre>
Preview Url: 
		<pre>http://${server.port.8080}/${current.project.relpath}</pre>

**Start Tomcat Command**	
Command Name: 
	<pre>Start Tomcat</pre>
Command Line:
	<pre>$TOMCAT_HOME/bin/catalina.sh jpda run 2>&1</pre>
Preview Url: 
		<pre>http://${server.port.8080}/${current.project.relpath}</pre>

**Stop Tomcat Command**
Command Name:
	<pre>Stop Tomcat</pre>        
 Command Line:
	 <pre>$TOMCAT_HOME/bin/catalina.sh stop</pre>
Preview Url: 
	<pre>None</pre>
NOTE: you should create a backup of the Workspace and environment by selecting the Workspace Config tab within your workspace, select all the configuration text from the edit control, and save this to a standard text file. You can put this Codenvy Recipe under source control (recommended). If your Workspace every becomes corrupt (Codevny has a bug where your Custom Commands set are not snapshotted) you can always use this Recipe to create a new Workspace.


----------


Eclipse Build and Configuration Instructions:
This IoT Services Reference Application uses Maven Profiles to select the appropriate configuration files for the target Cloud Platform. The Maven Profiles are setup on the Maven POM file located in the SDK. The Maven Profile names basically use the platform folder in the src/config/[PROFILE] directory structure.

 1. Setup your MySQL Database. Startup MySQL Workbench as root user (username of root and password of root), create a schema named 'iot' (without quotes), and then run the IoT.sql DDL script located in the ***docs\database*** folder within the SDK. You will also need to set the privileges for the *iot* schema for the pet clinic user (username of petclinic and password of password).
 2. Make sure your MySQL database is running.
 3. Open your Eclipse 'cloudservices' Workspace.
 4. Import the 'cloudservices' Template app from the SDK or the 'cloudservices' Reference app from your local GIT repository. Importing the project into Eclipse can be done by selecting the File->Import menu options in Eclipse, under the General section select the 'Existing Projects into Workspace' open, navigate to the root of the SDK to import the Template app or navigate to one folder higher than were the 'cloudservices' repository was cloned to, **make sure you check the 'copy' checkbox when importing**, and click the Finish button.
 5. Configure the application:
	 - In the src/config/dev directory update the config.properties file with your proper database credentials
	 - In the src/config/openshift directory update the config.properties file with your proper database credentials
	 - In the src/config/azure directory update the config.properties file with your proper database credentials
	 - In the src/config/heroku directory update the config.properties file with your proper database credentials
	 - In the src/config/amazon directory update the config.properties file with your proper database credentials
	 - Invoke Maven with the 'dev' Profile to build for your development environment
 6. To build and run the project invoke the following:
	 - Build the Project by selecting the Run->Run Configurations, select the Maven Build type, click the New Icon, and then set the name to My Cloudservices Build, set the Goals to clean package, set the Profiles to dev, and click the Run button. This build configuration will now be available when you select the Run Icon from the toolbar.
	 - Refresh your Eclipse Workspace by right clicking on the project and selecting the Refresh menu option.
	 - Add the Project to your Tomcat Server. This can be done by right clicking on the Tomcat Server in the Servers tab and adding the 'cloudservices' project to the Configured section. Your should also make sure you use the /cloudservices path for your web module. This can be done by double clicking on the Tomcat Server in the Servers tab, selecting the Modules tab from the Server configuration page, adding or editing the cloudservices Web Module.
	 - Locate the config.properties files located in the src folder of the Eclipse project. Modify the user credentials to match the user that was setup in step 1.
	 - From the Servers tab click the Start icon for Tomcat to start the Tomcat Server. Make sure you MySQL database is setup and running or you will get an error starting the application. 
	 - You will also want to make sure the Maven Build is part of your Build Class Path and so Tomcat picks up your changed files. To do this right click on your Project and select the Properties menu option. Select the Order and Export tabe. Make sure the Maven Dependencies checkbox is checked. The IoT Services Reference Application uses Maven Profiles to select the appropriate configuration files for the target Cloud Platform. The Maven Profiles are setup on the Maven POM file located in the SDK. The Maven Profile names basically use the platform folder in the src/config/[PROFILE] directory structure.

Build the IoT Reporting App
--------
Codenvy Build and Configuration Instructions:

 1. Start your 'cloudapp' Workspace. Once the environment is up and running click the 'Import Project...' link in the left project pane. 
 2. Select the GITHUB option under the Source Control section. Enter the URL for your Github 'cloudapp' repository.
 3. Click the Import button.
 4. Select the PHP Project Configuration and click the Next button.
 5. Click the Save button.
 6. Configure the application:
	 - In the app/http/controllers directory update the WeatherController.php file with your proper IoT Service URL's
	 - In the root directory of the project update the .env file and set the APP_ENV variable to openshift, azure, or local values
 7. In order for Laravel to run properly requires some file level permissions to be setup and the Apache configuration updated to allow HTTP filters to be run. The following needs to be done only once and the first time you run your PHP environment:
 8. To run the project invoke the following (you must do the one time configuration in next step):
 	 - Run 'Start Apache' from the Command Tools
 9. Fix permissions on Codenvy (one time setup issue): 
	 - Run the following in Codenvy Terminal: sudo find /projects/cloudapp -type d -exec chmod 777 {} \;
	 - Fix up .htaccess for Laravel project by updating apache2.conf:
	 -- cd /etc/apache2
	 -- sudo chmod 777 apache2.conf
	 -- sudo apt-get install nano
	 -- nano apache2.conf
	 -- Scroll down to to Virtual Directorys for /project and set AllowOverride to All
	 -- Restart Apache

----------

Eclipse Build and Configuration Instructions:

 1. Open your Eclipse 'cloudapp' Workspace.
 2. Import the 'cloudapp' Template app from the SDK or the 'cloudapp' Reference app from your local GIT repository. Importing the project into Eclipse can be done by selecting the File->Import menu options in Eclipse, under the General section select the 'Existing Projects into Workspace' open, navigate to the root of the SDK to import the Template app or navigate to one folder higher than were the 'cloudapp' repository was cloned to, **make sure you check the 'copy' checkbox when importing**, and click the Finish button.
 3. It should be noted that both the Template app and the Reference app have setup an ANT build file to automatically copy files from your Workspace to your MAMP runtime *htdocs* directory (i.e. auto-deployment). For examples, see the 'build.properties and 'build.xml' files from the Template app or the Reference app and the documentation in the ***developer/eclipsePHP*** directory in the SDK.
 4. Configure the application:
	 - In the app/http/controllers directory update the WeatherController.php file with your proper IoT Service URL's
	 - In the root directory of the project update the .env file and set the APP_ENV variable to openshift, azure, or local values

[Back to Top](#getting-started-building-the-iot-apps)

----------

Deploy the IoT Services App to OpenShift
--------
Once you have tested your IoT Services app you can then setup Cloud Containers in OpenShift and then build and deploy your application to OpenShift. Your IoT Services should FIRST be regression tested using the Postman Test Scripts located in the ***/sdk/developer/testing*** directory in the SDK before building and deploying your application. You may have to customize the hostnames and ports in the Test Scripts from the SDK. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

NOTE: You will need to Create two OpenShift v3 accounts: use one account for the IoT Services application and another account for the IoT Reporting application.

Setup and configure the OpenShift JBoss Tomcat MySQL Container:
 1. Create a new Project in OpenShift named Cloud Workshop.
 2. Click the Add to Project menu.
 3. Add the following types to the Project: JBoss Tomcat 8 image for the REST API Spring project and when prompted for a Github Repository URL for your project enter the URL for your 'cloudservices' Github repository.
 4. Click the Add to Project menu.
 4. Add the following Data Store to the Project: MySQL datastore image for the MySQL database.
 5. Once you have added both Containers to your Project you will need to group the JBoss Tomcat Container with the MySQL Container.

Initialize the MySQL Database (also see the online help [here](https://docs.openshift.com/online/dev_guide/migrating_applications/database_applications.html)):
 1. Download the OpenShift Command Line Interface tool from [here](https://console.starter-us-east-1.openshift.com/console/command-line).
 2. Open a Terminal Window or DOS Box. 
 3. Navigate to the path were the Command Line Tool was installed. 
 4. Get the MySQL Pod Name: ./oc get pods
 5. Copy the IoT.sql DDL script from SDK into a directory called /local/db on your local file system.
 6. Copy the SQL DDL script to the OpenShift MySQL Pod: ./oc rsync /local/db <mysql_pod_name>:/var/lib/mysql/data
 7. Remote into the MySQL Pod: ./oc rsh <mysql_pod> 
 8. Run the command: cd /var/lib/mysql/data
 8. Run the SQL DDL Script: mysql -u root
 9. Run the command: source all.sql
 9. Grant privileges to petclinic user: grant all privileges on iot.* to petclinic
 10. Run the command: flush privileges

NOTE: Because you will not have enough quota during deployment you will need to change the Container deployment strategy for this project. This can be done by selecting the following menu options: click Applications -> Deployments main menu items, select the name of your application, select the Actions -> Edit drop down menu options, and change the Deployment Strategy Type from Rolling to Recreate.

Build and deploy your application:
 1. Select the Builds->Builds main menu items. Click on the name of your JBoss Tomcat Container.
 2. Click the Start Build button. Note, you can monitor your build by clicking on the View Log link. Validate that your build was successful.
 3. Click the Overview main menu item. Note, you can monitor the build and deployment from this
    screen.

[Back to Top](#getting-started-building-the-iot-apps)

Deploy the IoT Reporting App to OpenShift
--------
Once you have tested your IoT Reporting app you can then setup Cloud Containers in OpenShift and then build and deploy your application to OpenShift. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

NOTE: You will need to Create two OpenShift v3 accounts: use one account for the IoT Services application and another account for the IoT Reporting application.

Setup and configure the OpenShift PHP Container:
 1. Create a new Project in OpenShift named Cloud Workshop.
 2. Click the Add to Project menu.
 3. Add the following types to the Project: PHP 7.0 image for PHP Laravel project. When prompted for a Github Repository URL for your project enter the URL for your 'cloudapp' Github repository.

Build and deploy your application:
 1. Select the Builds->Builds main menu items. Click on the name of your PHP Container.
 2. Click the Start Build button. Note, you can monitor your build by clicking on the View Log link. Validate that your build was successful.
 3. Click the Overview main menu item. Note, you can monitor the build and deployment from this
    screen.

----------

Deploy the IoT Services App to Azure
--------
Once you have tested your IoT Services app you can then setup Cloud Containers in Azure and then build and deploy your application to Azure. Your IoT Services should FIRST be regression tested using the Postman Test Scripts located in the ***/sdk/developer/testing*** directory in the SDK before building and deploying your application. You may have to customize the hostnames and ports in the Test Scripts from the SDK. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.A future update to these instructions will include building the application from GitHub in Azure.

NOTE: You will need to a create an Azure account (this is available for free if you are a Grand Canyon University student).

Create Tomcat 8.5 and MySQL Container in Azure:
 1. Log into the Azure Portal.
 2. Click the '+ Create a resource' icon from the Azure Portal and search for Tomcat.
 3. Select the Apache Tomcat 8 Application from Microsoft.
 4. Open your application from your Dashboard. This is an important step! This will ensure that phpMyAdmin is accessible via single sign on.

Initialize the MySQL Database:
 1. Open your application.
 2. Under the Settings section click the MySQL In App icon, make sure your Database is enabled, and click the Manage icon to open phpMyAdmin. Import your Database DDL.
 3. Under the Development Tools section click the Console icon.
 4. Navigate to the D:\home\data\mysql directory and display the ‘MYSQLCONNSTR_localdb.txt' file using the type command to get your MySQL Connection Properties. Note the DB connection information to get your DB hostname, post, and credentials.

Configure Tomcat Manager:
 1. Open your application (by default Tomcat Manager will be invoked for the default URL).
 2. Under the Development Tools section click the Advanced Tools icon, select the Go link, and select the Tools->Zip Push Deploy menu. 
 3. Navigate into the bin->apache-tomcat-8.x.x->conf directory.
 4. Edit the tomcat-users.xml file.
 5. Add a Tomcat User under the manager-gui role within the <tomcat-users> tag. Use the following XML tags:
    <role rolename="manager-gui"/>
    <user username="tomcat" password="admin" roles="manager-gui"/>
 6. Click the Save button.

Build and deploy your application:
 1. Open your application.
 2. Update your MySQL Database Connection properties in your application (note your hostname will need to be formatted as hostname:port).
 3. In Eclipse run a Maven build script or right click on your project and use the Export->WAR file menu options to create a WAR file for your project.
 4. Run the Tomcat Web Application Manager application at https://[Azure app name].azurewebsites.net/manager. Log into the Tomcat Web Application Manager using the credentials in the prior step.
 5. Under the Deploy section use the ‘WAR file to deploy’ to upload your WAR file created from step 3. After a few minutes your application should be listed in Applications with a Running state.

[Back to Top](#getting-started-building-the-iot-apps)

Deploy the IoT Reporting App to Azure
--------
Once you have tested your IoT Reporting app you can then setup a Cloud Container in Azure and then build and deploy your application to Azure. A future update to these instructions will include building the application from GitHub in Azure.

NOTE: You will need to create an Azure accounts (this is available for free if you are a Grand Canyon University student).

Create PHP Container in Azure:
 1. Log into the Azure Portal.
 2. Click the '+ Create a resource' icon from the Azure Portal and search for PHP.
 3. Select the PHP Starter Kit Application.
 4. Open your application from your Dashboard.

Build and deploy your application:
 1. Note: Make sure you have built your Laravel Project with the right version to match the version of PHP you are using.
 2. For the local Laravel codebase make sure to copy the web.config from the public directory to the root of your project.
 3. For the local Laravel codebase zip up your PHP project into a file named [appname].zip.
 4. Under the Development Tools section click the Advanced Tools icon, select the Go link, and select the Tools->Zip Push Deploy menu.
 5. Delete the Azure created default files from the application (if they exist).
 6. Drag and drop your zip file onto the page.

[Back to Top](#getting-started-building-the-iot-apps)

Deploy the IoT Services App to Google Cloud Platform
--------
Once you have tested your IoT Services app you can then setup Cloud Containers in Google and then build and deploy your application to the Google Cloud Platform. Your IoT Services should FIRST be regression tested using the Postman Test Scripts located in the ***/sdk/developer/testing*** directory in the SDK before building and deploying your application. You may have to customize the hostnames and ports in the Test Scripts from the SDK. You will also want to reference the [Cloud Setup Notes](Cloud%20Setup%20Notes.txt) in the SDK.

NOTE: You will need to create a Google Cloud Platform account (this requires a credit card and is free for 12 months).

Create Java (Jetty) Container and deploy your application in the Google App Engine (GAE):

 1. Create an App Engine application of type Java.
 2. Build and deploy (from Google Cloud Shell): 
* git clone [URL to Cloud Services Repo]
* cd to cloudservices
* Test locally in Shell: mvn -Pgoogle clean appengine:run
	 - NOTE: comment out the google-api-client and google-api-client-appengine as dependencies in your maven file
	 - TEST: click on the Web Preview icon in the Shell and go to https://[project name].appspot.com/rest/weather/get/0/1
* In the Google Cloud Dashboard go to APIs & Services and make sure Google Cloud SQL is enabled
* Deploy: mvn -Pgoogle clean appengine:deploy
* Test at https://[project name].appspot.com/rest/weather/get/0/1
	 - To view logs go to App Engine Versions and select Logs from the Tools dropdown

If you need to configure your own application the following steps need to be completed:

 1. Update POM file:
 ```xml
	<plugin>
		<groupId>com.google.cloud.tools</groupId>
		<artifactId>appengine-maven-plugin</artifactId>
		<version>1.3.1</version>
	</plugin>
	
	<dependency>
		<groupId>com.google.cloud.sql</groupId>
		<artifactId>mysql-socket-factory</artifactId>
		<version>1.0.5</version>
	</dependency>
	<dependency>
		<groupId>com.google.api-client</groupId>
		<artifactId>google-api-client</artifactId>
		<version>1.21.0</version>
	</dependency>
	<dependency>
		<groupId>com.google.api-client</groupId>
		<artifactId>google-api-client-appengine</artifactId>
		<version>1.21.0</version>
	</dependency>
 ```
 2. Add appengine.xml to WEB-INF. See example the Cloud Workshop SDK. 
 3. Update appengine-web.xml to set path for log file to /tmp/cloudservices/logs/iotWeatherApp.log. See example the Cloud Workshop SDK. 
 4. Update config.properties to setup db.connection property for Google MySQL database. See example the Cloud Workshop SDK.

See https://cloud.google.com/appengine/docs/flexible/java/dev-jetty9

Create the MySQL Database Container and initialzie the schema in the Google Cloud Platform.

 1. Create a SQL MySQL instance (of type Second Generation).
 2. Go to a browser and search for My IP. Note your IP Address. 
 3. Open the instance of the new database. 
 4. Under Users create a new user test/test that is available for all hosts. Click the Create button. 
 5. Under Authorization click Add Network, name of DevAccess, network of your IP Address, click Done and Save buttons. 
 6. Under IP Address request an IPv4 address. 
 7. Setup a MySQL Workbench connection using the databases IP address and user. 
 8. Connect to the database in MySQL Workbench and run the IoT.sql DDL script. 

Deploy the IoT Services App to Google Cloud Platform using a Docker File
--------
You can also use the Google Cloud Platform along with a Docker File to build a Tomcat Container or JBoss Wildfly Container, which can be used to deploy the IoT Services App. Documentation for how to build a Tomcat or JBoss Docker Image (using a Docker File provided in the SDK) and deploy the IoT Services app can be found in ***/sdk/docs/docker/tomat*** directory or the ***/sdk/docs/docker/jboss*** directory in the SDK. You may have to customize the Docker File as necessary from the SDK. You will also want to reference the [Tomcat Google Notes](/sdk/docs/docker/tomcat/Google%20Notes.txt) or the [JBoss Google Notes](/sdk/docs/docker/jboss/Google%20Notes.txt) in the SDK.

NOTE: You will need to create a Google Cloud Platform account (this requires a credit card and is free for 12 months).

[Back to Top](#getting-started-building-the-iot-apps)

Deploy the IoT Reporting App to Google Cloud Platform
--------
Once you have tested your IoT Reporting app you can then setup a Cloud Container in Google and then build and deploy your application to Google.

NOTE: You will need to create a Google Cloud Platform account (this requires a credit card and is free for 12 months).

Create PHP Container and deploy your application in the Google App Engine (GAE):

1. Create an App Engine application of type PHP.
2. Build and deploy (from Google Cloud Shell):
* git clone [URL to Cloud App Repo]
* cd to cloudapp
* Update .env to set APP_ENV to google
* Test locally in Shell: php -S 0.0.0.0:8080 -t ./
* Deploy: gcloud app deploy --project cloud-workshop-207715
* Test at https://[project name].appspot.com/weather

If you need to configure your own application the following steps need to be completed:

1. Add app.yaml for PHP app into the root directory of the application. See example the Cloud Workshop SDK.

* To Update your APP_KEY in the app.yaml run: php artisan key:generate --show
* NOTE: Apache Web Server is not used in Google App Engine so the public rewrite rule is invalid, you must set your document_root to public and copy all JS, CSS, and IMG from /resources/assets to /public/resources/assets. 			
2. Update composer.son require section (PHP v7.2 does not work at this point) and some post install commands to be ran:
```xml
        "php": "7.1.*",
		"post-install-cmd": [
			"Illuminate\\Foundation\\ComposerScripts::postInstall",
			"chmod -R 755 app bootstrap storage",
			"mkdir -p storage/app",
			"mkdir -p storage/framework/cache",
			"mkdir -p storage/framework/sessions",
			"mkdir -p storage/framework/views",
			"mkdir -p storage/logs",
			"php artisan cache:clear"
	],			
```
3. Update Service Endpoint URL:
 	Update APP_ENV in .env to google 
	
See https://cloud.google.com/community/tutorials/run-laravel-on-appengine-flexible

Deploy the IoT Services App to Heroku Cloud
--------
Once you have tested your IoT Services app you can then setup an Application in Heroku and then build and deploy your application to Heroku.

NOTE: You will need to create a Heroku account (this is free and most services you will need do not require a credit card).

1. Create app in Heroku
* Add heroku/java buildpack
* Add JawsDB MySQL Add-on
* Set variable MAVEN_CUSTOM_OPTS to -Pheroku
2. Update app code in source control or Heroku GIT(see SDK):
* Add webapp-runner to POM file
```xml
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-dependency-plugin</artifactId>
            <version>3.0.2</version>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals><goal>copy</goal></goals>
                    <configuration>
                        <artifactItems>
                            <artifactItem>
                                <groupId>com.github.jsimone</groupId>
                                <artifactId>webapp-runner</artifactId>
                                <version>8.5.31.0</version>
                                <destFileName>webapp-runner.jar</destFileName>
                            </artifactItem>
                        </artifactItems>
                    </configuration>
                </execution>
            </executions>
        </plugin>
```
* Add Maven Heroku Procfile (see the SDK, the build should be invoked using mvn -Pheroku clean package and use the webapp runner)
3. Create Heroku Pipeline and add the Java app to it
4. Start a Build:
* Go to Heroku Pipeline and under the Java App select the Deploy a branch menu option OR push your code to Heroku GIT
* Test the app: https://[APP NAME].herokuapp.com/rest/weather/get/0/1

Deploy the IoT Reporting App to Heroku Cloud
--------
Once you have tested your IoT Reporting app you can then setup an Application in Heroku and then build and deploy your application to Heroku.

NOTE: You will need to create a Heroku account (this is free and most services you will need do not require a credit card).

1. Create app in Heroku
* Add heroku/php buildpack
2. Update app code in source control or Heroku GIT:
* Update APP_ENV to heroku in .env
3. Create Heroku Pipeline and add the PHP app to it
4. Start a Build:
* Go to Heroku Pipeline and under the PHP App select the Deploy a branch menu option OR push your code to Heroku GIT
* Test the app: https://[APP NAME].herokuapp.com
	
Deploy the IoT Services App to Amazon Cloud
--------
Once you have tested your IoT Services app you can then setup an Application in Amazon and then build and deploy your application to AWS Elastic Beanstalk and a RDS MySQL Database.

NOTE: You will need to create an AWS account (this is free 12 month service you will need a credit card).

Create and configure an AWS MySQL databsae:
1. Log into AWS and select Services from the main menu.
2. Select RDS.
3. Under the Create database section click the Create database button.
4. Select the MySQL engine option and the 5.6 version edition radio button. Check the 'Enable options for free tier'. Click the Next button.
5. Fill out the Specify DB details form:
* From Settings enter DB instance identifier enter instance name (i.e. mydatabaseinstance).
* From Settings enter Master username and password.
* Click the Next button.
* Leave all defaults in the Configure advanced settings form.
6. From the RDS Dashboard select your database instance.
* Your database URL is listed under the Connect section under the Endpoint value.
* In MySQL Workbench setup a connection using the AWS Database Endpoint URI and credentials. Create the 'iot' schema and tables by running the DDL script from the SDK.
* Make your database accessible from a Java application by clicking the Security groups link under the Details section for the database.
* In the Security Group setup select the Inbound tab. Click the Edit button. Under the Source dropdown select the Anywhere option.

Create and configure an AWS Tomcat Application:
1. Update app code in source control (see SDK):
* Set up config folder and Maven Profile. 
2. Log into AWS and select Services from the main menu.
3. Select Elastic Beanstalk service.
4. Click the 'Create new Application' link from the top right menu.
5. Give your Application Name (i.e. ServicesApp). Click the Create button.
6. Create your Application Environment by clicking the 'Create one now' link.
7. Select the 'Web server environment' and click the Select button.
8. Fill out the following fields in the Creating web server environment form:
* From Environment information Domain:  Give your Application a name (i.e. services-app).
* From Base configuration: Select Tomcat from the Preconfigured platform options. Upload a WAR file of your Java application.
* Click the Create Environment button. Wait for environment to get built.
* From the Elastic Beanstalk application screen click the App URL to validate application is running properly.

Deploying Manually:
1. Create a WAR file using Maven (make sure to set the Maven Profile to amazon).
2. Log into AWS and select Services from the main menu.
3. Select Elastic Beanstalk. Select your Application.
4. Click the Upload and Deploy button. Upload your WAR file and give your build a label. Click the Deploy button. 

Deploying using a AWS Code Pipeline:
1. Add a buildspec.yml to the root of your application code (see SDK for example).
2. Log into AWS and select Services from the main menu.
3. Select the CodePipeline service.
4. Click the Create Pipeline button.
5. Give your pipeline a name (i.e. ReportingAppPipeline). Click the Next step button.
6. Select GitHub from the Source provider dropdown. Click the Connect to GitHub button and select your repo and master branch. Click the Next step button.
7. Select AWS CodeBuild from the Build provider dropdown. Select the Create a new build project option. Give your build a name. Select Ubuntu operating system with the Java OpenJDK 8 runtime. 
8. Create a Service Role with a name (i.e. servicesapp-build-role)
9. Click the Save build project button. Click the Next step button.
10. Select AWS Elastic Beanstalk from the Deployment provider dropdown. Chose your Application and Environment from the dropdowns. Click the Next step button.
11. Create an AWS Service Role. Click the Next step button.
12. Click the Create pipeline button.
13. To build and deploy your application:
* Select the CodePipeline service from the Services dashboard. Open the Pipeline.
* Either make a change to code in GitHub or click the Release change button to start a build and deployment.
14. To access your application:
* Select the Elastic Beanstalk service from the Services dashboard. Open your Application.
* Test your application: https://[APP NAME].[AWS REGION].elasticbeanstalk.com/rest/weather/get/0/1

Deploy the IoT Reporting App to Amazon Cloud
--------
Once you have tested your IoT Reporting app you can then setup an Application in Amazon and then build and deploy your application to AWS Elastic Beanstalk.

NOTE: You will need to create an AWS account (this is free 12 month service you will need a credit card).

Create and configure the AWS PHP Application:
1. Update app code in source control (see SDK):
* Update APP_ENV to amazon in .env 
2. Log into AWS and select Services from the main menu.
3. Select Elastic Beanstalk service.
4. Click the 'Create new Application' link from the top right menu.
5. Give your Application Name (i.e. ReportingApp). Click the Create button.
6. Create your Application Environment by clicking the 'Create one now' link.
7. Select the 'Web server environment' and click the Select button.
8. Fill out the following fields in the Creating web server environment form:
* From Environment information Domain: Give your Application a name (i.e. reporting-app).
* From Base configuration: Select PHP from the Preconfigured platform options. Upload a ZIP file of your PHP application.
* Click the Create Environment button. Wait for environment to get built.
* From the Elastic Beanstalk application screen click the App URL to validate application is running properly.

Deploy the IoT Reporting App to AWS:
Deploy Manually:
1. Create a ZIP file with all your code (make sure to update APP_ENV to amazon in .env).
2. Log into AWS and select Services from the main menu.
3. Select Elastic Beanstalk. Select your Application.
4. Click the Upload and Deploy button. Upload your ZIP file and give your build a label. Click the Deploy button. 

Deploy using a AWS Code Pipeline:
1. Add a buildspec.yml to the root of your application code (see SDK for example).
2. Log into AWS and select Services from the main menu.
3. Select the CodePipeline service.
4. Click the Create Pipeline button.
5. Give your pipeline a name (i.e. ReportingAppPipeline). Click the Next step button.
6. Select GitHub from the Source provider dropdown. Click the Connect to GitHub button and select your repo and master branch. Click the Next step button.
7. Select AWS CodeBuild from the Build provider dropdown. Select the Create a new build project option. Give your build a name. Select Ubuntu operating system with the Base runtime. 
8. Create a Service Role with a name (i.e. reportingapp-build-role)
9. Click the Save build project button. Click the Next step button.
10. Select AWS Elastic Beanstalk from the Deployment provider dropdown. Chose your Application and Environment from the dropdowns. Click the Next step button.
11. Create an AWS Service Role. Click the Next step button.
12. Click the Create pipeline button.
13. To build and deploy your application:
* Select the CodePipeline service from the Services dashboard. Open the Pipeline.
* Either make a change to code in GitHub or click the Release change button to start a build and deployment.
14. To access your application:
* Select the Elastic Beanstalk service from the Services dashboard. Open your Application.
* Test your application: https://[APP NAME].[AWS REGION].elasticbeanstalk.com/


[Back to Top](#getting-started-building-the-iot-apps)

