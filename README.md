\# Cybersecurity Labs



Hands-on cybersecurity labs focused on vulnerability identification, security testing, remediation, and technical documentation.



These projects are performed in an isolated VirtualBox home lab and are designed to demonstrate practical cybersecurity and IT skills through documented exercises and evidence.



\---



\## Lab Environment



| System | Role | IP Address |

|---|---|---|

| Kali Linux | Security testing workstation | 192.168.56.104 |

| Ubuntu Linux | Web application / server target | 192.168.56.101 |

| Windows 11 | Administration / client system | 192.168.56.106 |



\### Virtualization



\- VirtualBox

\- Host-Only Networking

\- Isolated lab environment



\---



\## Completed Labs



\### Command Injection



A deliberately vulnerable PHP web application was tested for command injection.



The lab demonstrates:



\- Establishing application baseline behavior

\- Identifying command injection

\- Demonstrating controlled command execution

\- Identifying the execution context

\- Input validation

\- Secure shell argument handling

\- Remediation verification

\- Evidence collection



\*\*Documentation:\*\* \[Command Injection Lab](documentation/command-injection-lab.md)



\---



\## Security Testing Methodology



My labs generally follow this workflow:



```text

Reconnaissance

&#x20;     ↓

Identify

&#x20;     ↓

Test

&#x20;     ↓

Validate

&#x20;     ↓

Document

&#x20;     ↓

Remediate

&#x20;     ↓

Retest



The goal is to demonstrate not only how a vulnerability can be identified, but also how it can be understood, mitigated, and verified.



\---------------------------------------------------------------------------------------------------





Skills Demonstrated



* Linux administration
* Web application security
* Vulnerability identification
* Command injection testing
* Input validation
* Secure coding practices
* Apache
* PHP
* Networking
* VirtualBox
* Security documentation
* Evidence collection
* Git/GitHub



\---------------------------------------------------------------------------------------------------



Planned Labs



Future exercises will expand into: 



* Honeypot deployment
* Linux log analysis
* Metasploitable 2 testing
* Privilege escalation
* Web application vulnerabilities
* Active Directory security
* Windows administration and security
* Network segmentation
* SIEM and security monitoring
* Incident response
* Linux hardening
* Security automation
* IDS and anomaly detection
* Cloud security



\---------------------------------------------------------------------------------------------------



Repository Structure



cybersecurity-labs/

│

├── documentation/

│   └── command-injection-lab.md

│

├── screenshots/

│   └── command-injection/

│       ├── command-injection-fixed.png

│       ├── command-injection-id.png

│       └── command-injection-success.png

│

└── README.md



\---------------------------------------------------------------------------------------------------



Purpose



This repository serves as a practical cybersecurity portfolio demonstrating hands-on experience with security testing, Linux systems, networking, vulnerability analysis, remediation, and technical documentation. 



All security testing is performed in controlled lab environments against intentionally vulnerable systems or applications.



