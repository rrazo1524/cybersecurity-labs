\# Honeypot Detection and Logging Lab



\## Overview



This lab demonstrates the design and deployment of a basic Python-based honeypot designed to detect and log unauthorized connection attempts.



The honeypot listens on TCP port `2222`, records connection information and received data, and presents a simulated SSH service banner to connecting clients.



Testing was performed from a Kali Linux security testing VM against an Ubuntu server running the honeypot.



All testing was intentionally generated within an isolated VirtualBox host-only network. No real credentials or external systems were targeted.



\---



\## Objectives



\* Deploy a basic network honeypot using Python.

\* Monitor incoming TCP connections.

\* Record source IP addresses, source ports, timestamps, and received payloads.

\* Simulate an SSH service banner.

\* Generate controlled connection attempts from a security testing system.

\* Analyze collected honeypot logs.

\* Restrict honeypot access using UFW.

\* Document detection evidence and security observations.



\---



\## Lab Environment



| System       | Role                                  | IP Address       |

| ------------ | ------------------------------------- | ---------------- |

| Ubuntu Linux | Honeypot / Server                     | `192.168.56.101` |

| Kali Linux   | Security Testing / Traffic Generation | `192.168.56.104` |

| Windows 11   | Management / Documentation            | `192.168.56.106` |



\### Virtualization



\* VirtualBox

\* Host-only isolated network

\* Ubuntu Apache/PHP environment

\* Python 3

\* Kali Linux

\* UFW firewall



The honeypot was intentionally isolated from external networks during testing.



\---



\## Network Architecture



```text

&#x20;                VirtualBox Host-Only Network

&#x20;                      192.168.56.0/24

&#x20;                             |

&#x20;            +----------------+----------------+

&#x20;            |                                 |

&#x20;            |                                 |

&#x20;    Kali Linux VM                       Ubuntu Linux VM

&#x20;    Security Testing                   Honeypot Server

&#x20;    192.168.56.104                     192.168.56.101

&#x20;                                            |

&#x20;                                            |

&#x20;                                      TCP Port 2222

&#x20;                                            |

&#x20;                                     Python Honeypot

```



Kali was used to generate controlled connection attempts against the Ubuntu honeypot.



\---



\## Honeypot Design



The honeypot was implemented in Python using the `socket` library.



The service:



1\. Binds to all available interfaces.

2\. Listens on TCP port `2222`.

3\. Accepts incoming connections.

4\. Assigns a connection number.

5\. Records the source IP address and source port.

6\. Receives up to 1024 bytes of data.

7\. Records the timestamp and received payload.

8\. Closes the client connection.

9\. Continues listening for additional connections.



The implementation uses a five-second receive timeout so that connections that send no data do not remain open indefinitely.



\### Source Code



The complete implementation is available in:



```text

honeypot/honeypot.py

```



\---



\## Firewall Configuration



The Ubuntu firewall was configured to allow the honeypot port only from the Kali testing VM.



The rule used was:



```bash

sudo ufw allow from 192.168.56.104 to any port 2222 proto tcp

```



This restricted TCP port `2222` to the designated security testing system within the lab.



The firewall configuration helped maintain the isolated nature of the exercise while still allowing controlled testing.



\---



\## Initial Connectivity Testing



Before generating test payloads, the honeypot was verified as listening on TCP port `2222`.



The Ubuntu system reported:



```text

LISTEN 0 5 0.0.0.0:2222

```



Local connectivity was tested from Ubuntu before testing from Kali.



Kali connectivity was then restored after verifying that its network interface had the expected lab IP address:



```text

192.168.56.104

```



\---



\## Connection Detection



A controlled connection was generated from Kali using Netcat:



```bash

echo "SSH\_LOGIN\_ATTEMPT" | nc -nv 192.168.56.101 2222

```



The honeypot recorded the connection and payload.



Example:



```text

Connection #1 | ... | Source: 192.168.56.104:53134 | Data: SSH\_LOGIN\_ATTEMPT

```



This demonstrated that the honeypot could identify:



\* Connection number

\* Source IP

\* Source port

\* Received data



\### Evidence



!\[Honeypot connection detected](../screenshots/honeypot/honeypot-connection-detected.png)



\---



\## Multiple Connection Detection



Additional controlled traffic was generated from Kali:



```bash

echo "SSH\_LOGIN\_ATTEMPT" | nc -nv 192.168.56.101 2222

echo "ADMIN\_LOGIN\_ATTEMPT" | nc -nv 192.168.56.101 2222

echo "INVALID\_COMMAND" | nc -nv 192.168.56.101 2222

```



The honeypot assigned sequential connection numbers and recorded each event.



Example:



```text

Connection #1 | ... | Source: 192.168.56.104:59998 | Data: SSH\_LOGIN\_ATTEMPT

Connection #2 | ... | Source: 192.168.56.104:59000 | Data: ADMIN\_LOGIN\_ATTEMPT

Connection #3 | ... | Source: 192.168.56.104:40376 | Data: INVALID\_COMMAND

```



\### Evidence



!\[Multiple honeypot connections](../screenshots/honeypot/honeypot-multiple-connections.png)



\---



\## Simulated SSH Service



The honeypot was enhanced with a simulated SSH banner:



```text

SSH-2.0-OpenSSH\_8.2p1 Ubuntu-4ubuntu0

```



This was used to make the listening service appear more representative of an SSH endpoint during controlled testing.



The honeypot does \*\*not\*\* implement a real OpenSSH service. The banner is only simulated application data.



Kali connected using Netcat:



```bash

nc -nv 192.168.56.101 2222

```



The simulated banner was displayed to the client.



Synthetic test values were then entered to verify that the honeypot could capture received input.



\### Evidence



!\[Simulated SSH interaction](../screenshots/honeypot/honeypot-ssh-interaction.png)



\---



\## Log Analysis



The honeypot recorded events in:



```text

honeypot.log

```



The log format was:



```text

Connection #N | Timestamp | Source: IP:Port | Data: Payload

```



Source IP frequency was analyzed using:



```bash

awk -F'Source: ' '{print $2}' honeypot.log | cut -d: -f1 | sort | uniq -c

```



The test environment produced entries from:



```text

127.0.0.1

192.168.56.101

192.168.56.104

```



The majority of externally generated test events originated from the Kali VM:



```text

192.168.56.104

```



These events were intentionally generated as part of the lab and should not be interpreted as real-world attacks.



\---



\## Sample Log



A sanitized version of the collected data is included in:



```text

honeypot/sample-honeypot.log

```



Example:



```text

Connection #1 | 2026-10-02 15:00:01 | Source: 192.168.56.104:53134 | Data: SSH\_LOGIN\_ATTEMPT

Connection #2 | 2026-10-02 15:00:05 | Source: 192.168.56.104:59000 | Data: ADMIN\_LOGIN\_ATTEMPT

Connection #3 | 2026-10-02 15:00:09 | Source: 192.168.56.104:40376 | Data: INVALID\_COMMAND

Connection #5 | 2026-10-02 15:01:12 | Source: 192.168.56.104:51564 | Data: <REDACTED\_TEST\_VALUE>

Connection #6 | 2026-10-02 15:01:15 | Source: 192.168.56.104:51576 | Data: <REDACTED\_TEST\_VALUE>

```



The raw log was intentionally excluded from the repository because it contained credential-like synthetic test values.



\---



\## Security Findings



The lab demonstrated several important defensive security concepts.



\### 1. Network Service Visibility



A listening TCP service can be detected by clients that can reach the host and port.



\### 2. Connection Logging



Even a simple service can collect useful metadata such as:



\* Timestamp

\* Source IP

\* Source port

\* Connection number

\* Received application data



\### 3. Firewall-Based Restriction



UFW can restrict access to a service based on source IP address.



\### 4. Service Simulation



A simulated protocol banner can be used in a controlled honeypot to make the service appear more representative of a real endpoint.



\### 5. Centralized Monitoring Potential



The collected events could serve as input for future security monitoring systems such as a SIEM or log-analysis pipeline.



\---



\## Limitations



This honeypot is intentionally basic and should not be considered a production deception system.



Limitations include:



\* No persistent database

\* No authentication system

\* No TLS encryption

\* No automated alerting

\* No IP reputation analysis

\* No geolocation enrichment

\* No log rotation

\* No multi-client concurrency

\* No protocol-level SSH implementation

\* No automated threat classification



The simulated SSH banner does not provide actual SSH functionality.



\---



\## Lessons Learned



This exercise provided practical experience with:



\* Python socket programming

\* TCP networking

\* Linux service monitoring

\* UFW firewall configuration

\* Netcat-based network testing

\* Source IP identification

\* Log collection

\* Command-line log analysis

\* Security event documentation

\* Honeypot design concepts

\* Controlled security testing



The lab also demonstrated the importance of validating network configuration before troubleshooting an application. Initial connectivity issues were traced to the Kali VM's network configuration and firewall rules rather than a problem with the Python socket listener.



\---



\## Skills Demonstrated



\*\*Cybersecurity\*\*



\* Network monitoring

\* Defensive security

\* Honeypot deployment

\* Security event collection

\* Log analysis

\* Firewall configuration

\* Controlled penetration testing



\*\*Networking\*\*



\* TCP/IP

\* TCP port monitoring

\* Source/destination addressing

\* Network isolation

\* Host-only networking



\*\*Linux\*\*



\* Ubuntu administration

\* UFW

\* `ss`

\* `tcpdump`

\* `awk`

\* `grep`

\* Linux permissions

\* Process/service troubleshooting



\*\*Programming\*\*



\* Python

\* Socket programming

\* File-based logging

\* Exception handling

\* Network service development



\---



\## Ethical and Safety Considerations



This project was conducted exclusively within an isolated, authorized VirtualBox laboratory.



All connection attempts and payloads were intentionally generated by the lab operator.



Credential-like values used during testing were synthetic and were not real account credentials.



No external systems, public IP addresses, or unauthorized services were targeted.



\---



\## Key Takeaways



This lab demonstrates how a lightweight Python service can function as a basic honeypot by accepting connections, collecting connection metadata, recording application data, and providing evidence for subsequent analysis.



The project also establishes a foundation for future security monitoring work involving centralized logging, intrusion detection, automated alerting, and SIEM platforms.



