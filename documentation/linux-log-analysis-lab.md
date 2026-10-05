\# Linux Log Analysis Lab



\## Overview



This lab demonstrates basic Linux security log analysis using Ubuntu authentication logs. Controlled SSH authentication failures were generated from a Kali Linux testing system and investigated using `/var/log/auth.log`.



The objective was to identify failed authentication activity, determine the affected username and recorded source address, establish the event timeline, and quantify repeated authentication failures.



All activity was performed in an isolated VirtualBox host-only laboratory environment using systems owned and controlled by the lab operator.



\---



\## Objectives



\* Examine Linux authentication logs.

\* Generate controlled failed SSH authentication events.

\* Identify failed authentication attempts.

\* Identify invalid usernames involved in authentication failures.

\* Determine the source address recorded by the target system.

\* Establish the timeline of repeated events.

\* Count authentication failures associated with a source.

\* Document findings using reproducible Linux commands.



\---



\## Lab Environment



| System       | Role                                    | Address        |

| ------------ | --------------------------------------- | -------------- |

| Ubuntu Linux | Log analysis target                     | 192.168.56.101 |

| Kali Linux   | Security testing system                 | 192.168.56.104 |

| Windows 11   | Documentation and repository management | Host system    |



\### Network



The systems were connected through an isolated VirtualBox host-only network.



No external systems were targeted during testing.



\---



\## Authentication Log



Ubuntu stores SSH authentication events in:



```text

/var/log/auth.log

```



The log was verified before testing:



```bash

ls -l /var/log/auth.log

```



The file was accessible with elevated privileges and contained current authentication activity.



\---



\## Baseline Log Review



Initial authentication activity was reviewed with:



```bash

sudo tail -n 20 /var/log/auth.log

```



The baseline contained normal system authentication activity, including `sudo` session events.



This established a baseline before generating controlled SSH authentication failures.



\---



\## Controlled SSH Testing



\### Testing System



The controlled authentication attempts were generated from the Kali Linux VM.



The following SSH command was used:



```bash

ssh fakeuser@192.168.56.101

```



A synthetic incorrect password was entered for the test.



The attempt was repeated three times.



The username `fakeuser` was intentionally selected because it does not represent a legitimate account on the Ubuntu system.



No real credentials were used.



\---



\## Detected Authentication Events



Ubuntu recorded the controlled attempts in `/var/log/auth.log`.



The relevant event format was:



```text

Failed password for invalid user fakeuser from 192.168.56.1 port XXXXX ssh2

```



The events demonstrated several important log fields:



| Field           | Finding         |

| --------------- | --------------- |

| Service         | `sshd`          |

| Event           | Failed password |

| Account         | `fakeuser`      |

| Account status  | Invalid user    |

| Recorded source | `192.168.56.1`  |

| Protocol        | SSHv2           |



The target system consistently recorded the source as `192.168.56.1`.



Although the testing traffic originated from the isolated Kali VM, the Ubuntu authentication log recorded the connection source as `192.168.56.1`. This demonstrates the importance of validating network addressing and understanding how virtualization networking can affect source-address visibility.



\---



\## Timeline Analysis



The three controlled authentication failures occurred at:



```text

2026-10-05 13:37:29

2026-10-05 13:37:47

2026-10-05 13:37:57

```



The first and third events occurred approximately 28 seconds apart.



The repeated failures within a short period represent a pattern that could be relevant to authentication monitoring and brute-force detection.



\---



\## Event Count



The number of failed-password events associated with the recorded source was verified with:



```bash

sudo grep "Failed password" /var/log/auth.log | grep "192.168.56.1" | wc -l

```



Result:



```text

3

```



This confirmed the three controlled failed authentication events generated during the lab.



\---



\## Evidence



The primary evidence screenshot shows the failed SSH authentication events captured from the Ubuntu authentication log.



!\[Failed SSH Authentication Events](../screenshots/linux-log-analysis/linux-log-analysis-failed-ssh.png)



\---



\## Security Findings



\### Finding 1 — Invalid Account Authentication



The SSH service recorded authentication attempts against an invalid username:



```text

fakeuser

```



This is a useful indicator because repeated attempts against nonexistent accounts can be relevant when investigating automated scanning or authentication attacks.



\### Finding 2 — Repeated Authentication Failures



Three failed authentication events were generated and detected within approximately 28 seconds.



Repeated failures occurring in a short period can indicate password guessing or automated authentication activity.



\### Finding 3 — Source Address Visibility



Ubuntu consistently recorded the source as:



```text

192.168.56.1

```



This differed from the Kali VM's configured lab address. The observation demonstrates that the address visible to an application or service may differ from the originating system's expected address depending on the virtualization or network configuration.



\---



\## Analyst Workflow



The investigation followed a basic security log-analysis workflow:



1\. Establish a baseline.

2\. Generate controlled test activity.

3\. Identify relevant authentication events.

4\. Extract event details.

5\. Correlate timestamps.

6\. Count repeated events.

7\. Identify potentially suspicious patterns.

8\. Document findings and evidence.



This workflow can be extended to larger authentication datasets and centralized security monitoring systems.



\---



\## Limitations



This lab represents a controlled authentication-testing scenario and does not demonstrate a real external attack.



The recorded source address was affected by the laboratory network configuration.



The exercise also used only three intentionally generated authentication failures, which is insufficient by itself to establish a real brute-force attack.



Additional indicators such as account behavior, geographic location, successful authentication events, event frequency over longer periods, and other system logs would be required for a production investigation.



\---



\## Skills Demonstrated



\* Linux system administration

\* Linux authentication log analysis

\* SSH troubleshooting and monitoring

\* Security event identification

\* Log filtering with `grep`

\* Event counting with `wc`

\* Timeline analysis

\* Authentication monitoring

\* Incident investigation fundamentals

\* Evidence collection

\* Security documentation



\---



\## Ethical and Safety Considerations



All authentication attempts were intentionally generated against an Ubuntu VM controlled by the lab operator.



The environment used an isolated VirtualBox host-only network.



No unauthorized systems, accounts, or external infrastructure were targeted.



Synthetic test credentials were used for the exercise.



\---



\## Key Takeaways



This lab demonstrates how Linux authentication logs can provide valuable evidence during a security investigation.



By examining failed authentication events, an analyst can identify invalid accounts, determine recorded source addresses, establish event timelines, and detect repeated authentication activity.



The exercise provides a foundation for more advanced security monitoring involving centralized logging, SIEM platforms, alerting, authentication anomaly detection, and automated incident response.



