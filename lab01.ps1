#!/bin/bash

# Create a PowerShell script for enabling automatic OS updates
cat <<EOL > EnableAutomaticUpdates.ps1
# Configure Automatic Windows Updates
\$automaticUpdatesPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
\$automaticUpdatesKey = "AU"

# Check if the Windows Update registry key exists, if not, create it
if (-not (Test-Path \$automaticUpdatesPath)) {
    New-Item -Path \$automaticUpdatesPath -Force
}

# Set the Automatic Updates registry values
Set-ItemProperty -Path \$automaticUpdatesPath -Name "AUOptions" -Value 4
Set-ItemProperty -Path \$automaticUpdatesPath -Name "ScheduledInstallDay" -Value 0
Set-ItemProperty -Path \$automaticUpdatesPath -Name "ScheduledInstallTime" -Value 3
Set-ItemProperty -Path \$automaticUpdatesPath -Name "NoAutoRebootWithLoggedOnUsers" -Value 1

# Notify user about the configuration
Write-Host "Automatic OS updates have been configured."

# Restart Windows Update service to apply changes
Restart-Service -Name wuauserv -Force
EOL

# Execute the PowerShell script
powershell.exe -ExecutionPolicy Bypass -File EnableAutomaticUpdates.ps1

# Remove the PowerShell script after execution
rm -f EnableAutomaticUpdates.ps1
