# Incident Response Playbook – Network Port Scanning and Reconnaissance

## Incident Description

This playbook provides operational response procedures for network reconnaissance and port scanning activity targeting enterprise systems and network infrastructure. It applies when network monitoring, intrusion detection systems, firewalls, or SIEM alerts indicate attempts to identify open ports, services, operating systems, or network topology that may precede further malicious activity.

---

# 1. Preparation

### Logging and Monitoring

* Ensure firewall, IDS/IPS, and network device logging is enabled.
* Forward firewall, IDS/IPS, router, and switch logs to the SIEM.
* Configure alerts for:
  * High-volume connection attempts to multiple ports.
  * Sequential or randomized port scanning behavior.
  * Connections to numerous hosts from a single source.
  * TCP SYN scan patterns.
  * UDP scan activity.
  * ICMP reconnaissance or network sweeps.
  * Service enumeration attempts.
  * Network scanning originating from known malicious IP addresses.

### Security Controls

* Maintain firewall rules limiting unnecessary exposed services.
* Enable IDS/IPS signatures for reconnaissance detection.
* Segment critical systems using network segmentation.
* Disable unused services and close unnecessary ports.
* Maintain an inventory of authorized externally exposed services.
* Subscribe to threat intelligence feeds for known scanning infrastructure.

---

# 2. Detection and Analysis

## Detection Signals

Investigate when one or more of the following are observed:

* Multiple connection attempts across numerous ports.
* Sequential or randomized scanning of TCP or UDP ports.
* One source IP probing multiple internal hosts.
* Large numbers of rejected firewall connections.
* ICMP echo requests across multiple systems.
* Service version enumeration attempts.
* Scanning activity originating from known malicious infrastructure.

## Validation Steps

1. Review SIEM alerts.
2. Examine firewall, IDS/IPS, and network device logs.
3. Identify:
   * Source IP address
   * Destination hosts
   * Targeted ports
   * Network protocols
   * Timestamp pattern
   * Scan duration
4. Determine whether the source belongs to an authorized vulnerability scanner.
5. Check threat intelligence for malicious indicators.
6. Determine whether reconnaissance progressed to exploitation attempts.

## Severity Indicators

Escalate severity if:

* Scanning targets critical infrastructure or high-value assets.
* Multiple internal hosts are targeted.
* Reconnaissance is followed by exploitation attempts.
* Known malicious infrastructure is identified.
* Credential attacks or lateral movement activity follows reconnaissance.

---

# 3. Containment and Eradication

## Containment

If reconnaissance activity only is observed:

* Block malicious source IP addresses where appropriate.
* Increase monitoring of targeted systems.
* Verify firewall policies are functioning correctly.
* Continue monitoring for escalation to exploitation.

If malicious activity progresses beyond reconnaissance:

* Block offending IP addresses at perimeter devices.
* Isolate affected systems if compromise is suspected.
* Preserve firewall, IDS/IPS, and network logs.
* Increase logging verbosity on targeted assets.

## Eradication

* Remove unnecessary exposed services.
* Close unused network ports.
* Harden firewall and IDS/IPS rules.
* Apply security updates to exposed services.
* Verify network segmentation is functioning correctly.
* Review externally exposed systems for misconfigurations.

---

# 4. Post-Incident Activity

## Recovery

* Verify exposed services are operating normally.
* Confirm firewall and IDS/IPS rules remain effective.
* Continue monitoring for repeated reconnaissance attempts.
* Validate no unauthorized access occurred following the scanning activity.

## Lessons Learned

Document:

* Timeline of events.
* Source IP addresses.
* Targeted hosts.
* Targeted ports and services.
* Detection methods.
* Containment actions.
* Any security gaps identified.
* Opportunities to improve detection rules and network hardening.

## Evidence Retention

Preserve:

* Firewall logs.
* IDS/IPS alerts.
* Network device logs.
* SIEM alerts.
* Packet captures (if available).
* Threat intelligence results.
* Analyst investigation notes.