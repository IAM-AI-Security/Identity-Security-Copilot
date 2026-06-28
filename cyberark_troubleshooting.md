# CyberArk Troubleshooting Guide

## Central Policy Manager (CPM) Failures

### 1. Password Rotation Failure (Error: "Network path not found")
- **Symptom:** CPM cannot reach the target machine to change the password.
- **Root Cause:** Network firewall blocking SMB (port 445) or WMI (port 135), or the target machine is offline.
- **Resolution:**
  1. Verify the target machine is powered on.
  2. Test connectivity from the CPM server to the target using `Test-NetConnection -ComputerName <TargetIP> -Port 445`.
  3. Request firewall rule adjustment if blocked.

### 2. Password Verification Failure (Error: "Logon failure: unknown user name or bad password")
- **Symptom:** CPM can reach the machine but authentication fails.
- **Root Cause:** The password stored in the Vault does not match the password on the target machine, or the account is locked out.
- **Resolution:**
  1. Check if the account is locked out in Active Directory or locally.
  2. If the password is out of sync, perform a manual password reset on the target machine and update the Vault, or trigger a reconciliation process.

### 3. Reconciliation Failure (Error: "Access is denied")
- **Symptom:** The reconcile account lacks permissions to reset the target account's password.
- **Root Cause:** Reconcile account is not in the local Administrators group or lacks "Reset Password" delegation in AD.
- **Resolution:**
  1. Verify the reconcile account's group membership.
  2. Ensure the reconcile account is correctly associated with the target account or platform in CyberArk.

## Privileged Session Manager (PSM) Failures

### 1. Session Connection Timeout
- **Symptom:** User clicks "Connect" but the RDP window times out.
- **Root Cause:** Client cannot reach the PSM server on port 3389, or the PSM server cannot reach the target machine.
- **Resolution:**
  1. Verify the user's network allows outbound 3389 to the PSM.
  2. Check the PSM server's connectivity to the target machine on the required port (3389 for Windows, 22 for Linux).

### 2. PSM Service Not Running
- **Symptom:** Connections fail immediately; PSM health check shows offline.
- **Root Cause:** The PSM service crashed or failed to start due to a configuration error or missing prerequisites.
- **Resolution:**
  1. Check the Windows Event Viewer and PSM logs (`PSMConsole.log`, `PSMTrace.log`) on the PSM server.
  2. Restart the `CyberArk Privileged Session Manager` service.

### 3. AppLocker Blocking PSM Components
- **Symptom:** PSM connection fails with an AppLocker error in the event logs.
- **Root Cause:** A PSM component or required executable is not allowed by the local AppLocker policy.
- **Resolution:**
  1. Review the AppLocker event logs (`Microsoft-Windows-AppLocker/EXE and DLL`).
  2. Update the AppLocker rules using the `PSMConfigureAppLocker.ps1` script to allow the blocked executable.
