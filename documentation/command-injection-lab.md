\# Command Injection Lab



\## Overview



This lab demonstrates a command injection vulnerability in a deliberately vulnerable PHP web application running on an isolated Ubuntu server.



The exercise follows a security testing workflow:



1\. Establish normal application behavior

2\. Identify command injection

3\. Demonstrate command execution

4\. Determine the execution context

5\. Remediate the vulnerability

6\. Verify the remediation



The testing was performed entirely within an isolated VirtualBox host-only network.



\---



\## Lab Environment



| System | Role | IP Address |

|---|---|---|

| Kali Linux | Security testing workstation | 192.168.56.104 |

| Ubuntu | Web application target | 192.168.56.101 |



\### Software



\- Apache 2.4.58

\- PHP 8.3.6

\- Kali Linux

\- Ubuntu Linux

\- VirtualBox Host-Only Networking



\---



\## Network Architecture



```text

Kali Linux

192.168.56.104

&#x20;     |

&#x20;     | HTTP

&#x20;     |

&#x20;     v

Ubuntu Linux

192.168.56.101

Apache + PHP



The environment was isolated using VirtualBox host-only networking.



\---------------------------------------------------------------------------------------------------



1. Initial Application Testing



The application was accessed from Kali Linux:



http://192.168.56.101/command.php



A normal IP address was submitted:



192.168.56.101



The application successfully returned ping results:



4 packets transmitted, 4 packets received



This established the expected behavior before security testing.



\---------------------------------------------------------------------------------------------------



2\. Command Injection Discovery



The application accepted user-controlled input and incorporated it into a system command.



The vulnerable implementation used:



shell\_exec("ping -c 4 " . $host);



The input was not validated before being passed to the shell.



A test payload was entered:



192.168.56.101; whoami



the application returned:



www-data



This demonstrated that the input was being interpreted by the operating system shell rather than being treated strictly as an IP address.



Evidence



\---------------------------------------------------------------------------------------------------



3\. Command Execution Context



A second harmless command was used to determine the privileges associated with the web application process.



Input:



192.168.56.101; id



Output: 



uid=33(www-data) gid=33(www-data) groups=33(www-data)



This showed that commands were executing under the Apache www-data account.



Evidence



\---------------------------------------------------------------------------------------------------



4\. Vulnerability Analysis



The vulnerability occurred because untrusted user input was concatenated directly into a shell command.



Vulnerable Code



$host = $\_GET\["host"];

$output = shell\_exec("ping -c 4 " . $host);



The application assumed that the submitted value would contain only a legitimate hostname or IP address.



Because no input validation was performed, shell metacharacters could alter the intended command.



Security Impact



Command injection can allow an attacker to execute operating-system commands using the privileges of the vulnerable application's process.



In this lab, command execution occurred as:



www-data



The actual impact of a command injection vulnerability depends on the privileges of the effected service account and the permissions available to that account.



\---------------------------------------------------------------------------------------------------



5\. Remediation



The application was modified to validate the submitted value before executing the ping command.



The remediation included:



if (filter\_var($host, FILTER\_VALIDATE\_IP)) {

&#x20;  $output = shell\_exec("ping -c 4 " . escapehellarg($host));

}



Two protections were added:



filter\_var($host, FILTERED\_VALIDATE\_IP)



This ensures the application accepts only a valid IP address.



Shell Argument Escaping



escapehellarg($host)



This safely treats the validated value as a single shell argument.



The application also returns an error when invalid input is supplied.



Invalid IP address.



\---------------------------------------------------------------------------------------------------



6\. Remediation Verification



Normal functionality was tested again using:



192.168.56.101



The ping operation continued to work successfully.



The original command-injection test was then repeated:



192.168.56.101; whoami



The application rejected the input and returned:



Invalid Ip address.



The whoami command was no longer executed.



Evidence



\---------------------------------------------------------------------------------------------------



7\. Security Testing Methodology



This lab followed a simplified vulnerability-management workflow: 



Baseline

&#x20;  ↓

Identify

&#x20;  ↓

Test

&#x20;  ↓

Confirm

&#x20;  ↓

Remediate

&#x20;  ↓

Retest



This approach demonstrates the importance of verifying both the existence of a vulnerability and the effectiveness of the remediation.



\---------------------------------------------------------------------------------------------------



Skill Demonstrated



* Linux administration
* Apache configuration
* PHP
* Web application security testing
* Command injection identification
* Input validation
* Secure command construction
* Vulnerability remediation
* Security testing methodology
* Technical documentation
* Evidence collection
* Git/GitHub portfolio development



\---------------------------------------------------------------------------------------------------



Key Takeaways



This lab demonstrated how unsafe handling of user-controlled input can result in operating-system command execution.



The vulnerability was identified in a controlled environment, demonstrated using harmless commands, remediated through input validation and shell argument escaping, and retested to verify that the original injection no linger executed.



All testing was performed against intentionally vulnerable software within an isolated lab environment.



