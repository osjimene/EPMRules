<copyright file="readme.txt" company="Microsoft Corporation">
Copyright (C) Microsoft Corporation. All rights reserved.
</copyright>

Epm Agent provides a set of PowerShell cmdlets to help visualize, diagnose and troubleshoot its functionality, covering the following topics: 

- Elevation rules policies received.
- Client settings policies received.
- WinDC documents received by declared configuration.
- WinDC documents processed by the Epm Agent.
- Elevation rules lookup functionality.

Steps to use the cmdlets:

- Open PowerShell with admin privileges.
- Go to EpmTools folder (cd 'C:\Program Files\Microsoft EPM Agent\EpmTools\')
- Import the Epm Agent cmdlets (Import-Module .\EpmCmdlets.dll)

Available commands

- Get-Policies: Retrieves a list of all policies received by the Epm Agent for a given PolicyType (ElevationRules, ClientSettings)
    E.g. Get-Policies -PolicyType ElevationRules -Verbose | Format-Table -AutoSize
         Get-Policies -PolicyType ClientSettings -Verbose | Format-Table -AutoSize

- Get-DeclaredConfiguration: Retrieves a list of WinDC documents received by Declared Configuration targeting a given PolicyType (ElevationRules, ClientSettings). These are the policies targeted to the device, for every policy two WinDC documents are received in the device, one of type MSFTPolicies (actual policy) and one of type MSFTInventory (inventory operation)
    E.g. Get-DeclaredConfiguration -PolicyType ElevationRules -Verbose | Format-Table -AutoSize
         Get-DeclaredConfiguration -PolicyType ClientSettings -Verbose | Format-Table -AutoSize

- Get-DeclaredConfigurationAnalysis: Retrieves a list of WinDC documents of type MSFTPolicies and checks if the policy is already present in Epm Agent (Processed column)
    E.g. Get-DeclaredConfigurationAnalysis -PolicyType ElevationRules -Verbose | Format-Table -AutoSize
         Get-DeclaredConfigurationAnalysis -PolicyType ClientSettings -Verbose | Format-Table -AutoSize

- Get-ElevationRules: Query the EpmAgent lookup functionality and retrieves rules given lookup and target, currently two kinds of lookups are supported (FileName, CertificatePayload) 

    E.g. Get-ElevationRules -Target 0F8E191824716C293476BA7BCA6A8A3859C4E4D8C9BC261ED14086C782453701 -Lookup CertificatePayload -Verbose
         Get-ElevationRules -Target ccmclean.exe -Lookup FileName -Verbose

- Get-ClientSettings: Process all existing client settings policies, analyze conflicts (multiple policies with different values for same setting) and use hardcoded defaults if needed for policies not present or in conflict, resulting in diplaying the effective client settings used by the EPM Agent.
    E.g. Get-ClientSettings -Verbose

- Get-FileAttributes: Retrieves File Attributes for a .exe file and extract its Publisher and CA certificates to a set location that can be used to populate Elevation Rule Properties for a particular application. Default Hash Algorithm used is Sha256 to get the File Hash.
  Note: 1) Currently does not support Catalog signed certificates. 2) CA Cert chain is indexed. Index 1 : Root Cert, Index 2 : Intermediary CA cert issued by Root Cert 3) Hash Algorithms Supported : Sha256, Sha384, Sha512
    E.g. Get-FileAttributes -FilePath "C:\\Program Files\\Notepad++\\notepad++.exe" -CertOutputPath "C:\\Certs" -HashAlgorithm "Sha256" -Verbose