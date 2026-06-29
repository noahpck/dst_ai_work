# Incident Response Playbook – SSH Brute Force and Credential Stuffing

## Incident Description

This playbook provides operational response procedures for SSH brute force and credential stuffing attacks targeting Linux and UNIX systems. It applies when repeated authentication failures or anomalous SSH login activity indicate an attempt to gain unauthorized access.

---

# 1. Preparation

### Logging and Monitoring

* Ensure SSH authentication logs are enabled (e.g., `/var/log/auth.log` or `/var/log/secure`).
* Forward authentication logs to the SIEM.
* Configure alerts for:

  * Rapid increases in failed SSH login attempts.
  * Multiple failed logins against a single account.
  * Multiple usernames targeted from a single IP address.
  * Successful login following repeated failures.
  * SSH logins occurring outside normal operating hours.
  * SSH logins originating from unfamiliar geographic regions or IP addresses.

### Security Controls

* Enforce multi-factor authentication where supported.
* Disable password authentication where feasible and require SSH key authentication.
* Configure account lockout or rate limiting.
* Implement IP reputation or threat intelligence feeds.
* Maintain asset inventory and authorized administrator list.

---

# 2. Detection and Analysis

## Detection Signals

Investigate when one or more of the following are observed:

* Rapid spike in failed SSH authentication events.
* Numerous authentication failures from a single source IP.
* Authentication attempts against multiple accounts.
* Successful authentication immediately following repeated failures.
* Login attempts outside approved maintenance windows.
* SSH connections from unusual geographic locations or unknown IP addresses.

## Validation Steps

1. Review SIEM alerts.
2. Examine SSH authentication logs.
3. Identify:

   * Source IP addresses
   * Target accounts
   * Timestamp pattern
   * Number of failures
   * Any successful authentications
4. Determine whether source IPs are known administrative hosts.
5. Check threat intelligence for malicious IP indicators.
6. Determine whether any account compromise has occurred.

## Severity Indicators

Escalate severity if:

* A successful login follows repeated failures.
* Privileged accounts are targeted.
* Multiple hosts are targeted simultaneously.
* Evidence of lateral movement exists.

---

# 3. Containment and Eradication

## Containment

If no successful login occurred:

* Block offending IP addresses using firewall or IDS controls.
* Enable temporary rate limiting.
* Continue monitoring authentication attempts.

If compromise is confirmed:

* Disable or lock affected accounts.
* Terminate active SSH sessions.
* Isolate affected systems if post-authentication activity is detected.
* Preserve relevant logs before making additional changes.

## Eradication

* Reset affected user credentials.
* Rotate SSH keys if compromise is suspected.
* Remove unauthorized accounts or SSH authorized keys.
* Verify SSH daemon configuration.
* Apply security updates if vulnerabilities contributed to the incident.
* Verify no persistence mechanisms have been established.

---

# 4. Post-Incident Activity

## Recovery

* Re-enable affected accounts after credential reset.
* Restore normal SSH access.
* Continue heightened monitoring for recurring authentication attempts.

## Lessons Learned

Document:

* Timeline of events.
* Source IP addresses.
* Targeted accounts.
* Root cause.
* Detection effectiveness.
* Containment actions.
* Opportunities to improve detection rules or preventive controls.

## Evidence Retention

Preserve:

* Authentication logs.
* Firewall logs.
* SIEM alerts.
* Threat intelligence results.
* Analyst investigation notes.
