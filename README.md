

# Cybersecurity Labs

Hands-on cybersecurity labs focused on vulnerability identification, security testing, defensive monitoring, remediation, and technical documentation.

These projects are performed in an isolated VirtualBox home lab and are designed to demonstrate practical cybersecurity and IT skills through documented exercises and evidence.

---

## Lab Environment

| System       | Role                            | IP Address       |
| ------------ | ------------------------------- | ---------------- |
| Kali Linux   | Security testing workstation    | `192.168.56.104` |
| Ubuntu Linux | Web application / server target | `192.168.56.101` |
| Windows 11   | Administration / client system  | `192.168.56.106` |

### Virtualization

* VirtualBox
* Host-Only Networking
* Isolated lab environment

---

## Completed Labs

### 1. Command Injection

A deliberately vulnerable PHP web application was tested for command injection.

The lab demonstrates:

* Establishing application baseline behavior
* Identifying command injection
* Demonstrating controlled command execution
* Identifying the execution context
* Input validation
* Secure shell argument handling
* Remediation verification
* Evidence collection

**Documentation:** [Command Injection Lab](documentation/command-injection-lab.md)

---

### 2. Honeypot Detection & Logging

A basic Python-based honeypot was deployed on Ubuntu to detect and log controlled connection attempts from a Kali Linux testing system.

The lab demonstrates:

* Python socket programming
* TCP service monitoring
* Connection detection
* Source IP and port identification
* Payload logging
* Simulated SSH service banner
* UFW firewall configuration
* Network troubleshooting
* Log analysis
* Evidence collection
* Defensive security monitoring

**Documentation:** [Honeypot Lab](documentation/honeypot-lab.md)

**Implementation:** [honeypot.py](honeypot/honeypot.py)

**Sample Log:** [sample-honeypot.log](honeypot/sample-honeypot.log)

---

### 3. Linux Log Analysis

**Focus:** Linux authentication monitoring and security event investigation

This lab demonstrates analysis of Ubuntu authentication logs using `/var/log/auth.log`. Controlled SSH authentication failures were generated from Kali Linux and investigated to identify invalid usernames, recorded source addresses, timestamps, repeated authentication activity, and event frequency.

**Skills demonstrated:**

- Linux authentication log analysis
- SSH monitoring
- Security event investigation
- Log filtering with grep
- Event counting
- Timeline analysis
- Authentication monitoring
- Security documentation

**Documentation:** [`linux-log-analysis-lab.md`](documentation/linux-log-analysis-lab.md)

---

### 4. Metasploitable 2 Vulnerability Assessment

A controlled vulnerability assessment was performed against an intentionally vulnerable Metasploitable 2 virtual machine in an isolated VirtualBox host-only network.

The assessment demonstrates:

* Network reconnaissance
* Nmap service enumeration
* Service and version identification
* FTP banner validation
* Vulnerability identification
* Metasploit Framework
* Controlled exploitation
* Meterpreter
* Root privilege verification
* Linux shell verification
* Security findings analysis
* Evidence collection
* Vulnerability remediation recommendations

The assessment identified vsFTPd 2.3.4 on TCP port 21 and successfully demonstrated exploitation of the associated backdoor vulnerability, resulting in a Meterpreter session with root-level privileges.

Documentation: Metasploitable 2 Lab

Evidence: Metasploitable 2 Screenshots

---

## Security Testing Methodology

My labs generally follow this workflow:

```text
Reconnaissance
      ↓
Identify
      ↓
Test
      ↓
Validate
      ↓
Document
      ↓
Remediate
      ↓
Retest
```

The goal is to demonstrate not only how a security issue can be identified, but also how it can be understood, mitigated, monitored, and verified.

---

## Skills Demonstrated

### Cybersecurity

* Vulnerability identification
* Command injection testing
* Honeypot deployment
* Security monitoring
* Log analysis
* Defensive security
* Input validation
* Secure coding practices
* Evidence collection
* Technical security documentation

### Linux & Networking

* Linux administration
* TCP/IP networking
* TCP port monitoring
* UFW firewall configuration
* Network troubleshooting
* Service monitoring
* Apache
* VirtualBox
* Host-only networking

### Programming & Tools

* Python
* PHP
* Socket programming
* Netcat
* Nmap
* Wireshark
* Git/GitHub

---

## Planned Labs

Future exercises will expand into:

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

---

## Repository Structure

```text
cybersecurity-labs/
│
├── documentation/
│   ├── command-injection-lab.md
│   └── honeypot-lab.md
│
├── honeypot/
│   ├── honeypot.py
│   └── sample-honeypot.log
│
├── screenshots/
│   ├── command-injection/
│   │   ├── command-injection-fixed.png
│   │   ├── command-injection-id.png
│   │   └── command-injection-success.png
│   │
│   └── honeypot/
│       ├── honeypot-connection-detected.png
│       ├── honeypot-multiple-connections.png
│       └── honeypot-ssh-interaction.png
│
├── .gitignore
└── README.md
```

---

## Purpose

This repository serves as a practical cybersecurity portfolio demonstrating hands-on experience with security testing, Linux systems, networking, vulnerability analysis, defensive monitoring, remediation, programming, and technical documentation.

All security testing is performed in controlled lab environments against intentionally vulnerable systems, simulated services, or intentionally generated test traffic.

No unauthorized external systems are targeted.
