**

## DevOps in the Cloud Workshop
Some principles of DevOps are demonstrated in the IoT Reference Applications. The following diagram illustrates where DevOps principles are demonstrated in the Cloud Workshop SDK. Return to the [Cloud Workshop SDK](https://github.com/markreha/cloudworkshop/blob/master/README.md).

<p align="center">
	<img src="sdk/docs/architecture/images/devops.png" alt="IoT DevOps Architecture"/>
</p>

**Resources:**
 - TODO

**Logging, Monitoring, and Alerts:**
 - Logging:
	 - The IoT Services Application demonstrates logging using SLF4J with the Log4J logging provider.
	 - Depending on your Cloud Platform these log files can be accessed or pulled for analysis.
	 -  The following briefly outlines how to access log files for each of the Cloud Platforms supported by the SDK:
	 - - *OpenShift*: To view the Application Server log file from the Portal, select your Application from the Application->Deployments menu and then click the View Log menu. To view the Application Logs from the Portal, select your Application from the Application->Pods menu and then click the Terminal menu. From the Terminal tail your log file.
	 - - *Google*: To view the Application Server log, Application log, or stdout from the Portal, select your Project and then the App Engine->Versions menu and then click the Logs option from the dropdown Tools menu. To view  the Application log from the Portal, select your Project and then the App Engine->Instances menu, and then SSH into the server to tail your log file.
	 - - *Azure*: To view the Application Server log, Application log, or stdout from the Portal, select your Project and then the Advanced Tools menu, select the Tools->Zip Push Deploy menu options, navigate to the log file, and click the View menu. You must set the logging configuration to log to stdout.
	 - - *Heroku*: To view the Application Server log, Application log, or stdout from the Portal, select your application, select the View Logs menu. You must set the logging configuration to log to stdout.
 - Monitoring:
	 - Application Performance Management (APM): 
		 - To monitor your application performance you can use a product, such as New Relic or AppDynamics. Both of these products are available as "free" add-ons in the Heroku Cloud. Other options include using Stackdriver on Google Cloud or enabling Monitoring Alert rules in Azure Cloud.
	 - Application Availability: 
		 - To be notified that your application is not running you can use a free service such as Uptime Robot (at https://uptimerobot.com). This service will monitor a URL of your application and notify via email is your application is not running. For the IoT Reporting Application you can simply test access by using the Root URL. For the IoT Services Application you can simply test access by using the Test URL (at /rest/weather/test).
 - Alerts:
	 - In an ideal DevOps design your log files would be pushed to a platform like Splunk where rules and alerts could be setup.
	 - In an ideal DevOps design your APM (Application Performance Monitor) tool and your Availability Monitoring tool would generate alerts if there were issues with your application.

**Continuous Integration/Continuous Deployment:**
 - Automation Testing:
	 - Unit Testing:
	 -- Unit tests can be written, such as JUnit, and invoked via your Maven POM file configuration during the Test Phase in GitLab or Jenkins.
	 - Performance Testing:
	 - - Performance tests can be written, such as JMeter, and invoked from a free Cloud based provider like Flood IO (at https://flood.io/) during the Test Phase in GitLab or Jenkins.
	 - Functional Testing:
	 - - There are not any known free Cloud based providers that support functional testing.
 - GitLab CI/CD Pipeline: 
	 - The IoT Reporting Application and the IoT Services Application each have an example CI/CD configuration file in the SDK (i.e. .gitlab-ci.yml) that demonstrates how CI/CD is integrated using GitLab. It should be noted that the current GitLab Pipeline is setup for manual builds however simply changing the CI/CD configuration from manual to auto could automate your build and deployment.
	 - The example CI/CD configuration file in the SDK provides examples how to build the PHP application via Composer or the Java Spring application via Maven using a GitLab project that mirrors GIT repositories located on GitHub.
	 - The example CI/CD configuration file in the SDK provides examples how to deploy the PHP application or the the Java Spring application to the OpenShift, Azure, Google, and Heroku Cloud Platforms using a GitLab project that mirrors GIT repositories located on GitHub.
	 - To start using GitLab create a new Project, mirror your GitHub repository (or use GitLab as your GIT repo), add a .gitlab-ci.yml to the root of your project (using the examples in the SDK as a guide), setup any Environment Variables (located in the Settings->CI/CD->Variables menu options), and finally create a Pipeline (located in the CI/CD->Pipelines menu options).
 - Jenkins CI/CD Pipeline:
	 - This will be added in a future release of the Cloud Workshop SDK. 

