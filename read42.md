Readings: Pass the Hash with Mimikatz
Below you will find reading materials and additional resources that support today’s topic and the upcoming lecture.

Review the Submission Instructions for guidance on completing and submitting this assignment.

Reading
What is Mimikatz?

Name the six credential-gathering techniques which Mimikatz is able to perform and explain how two of them work.  

Pass-the-Ticket (PTT):

In Windows, Kerberos authentication issues tickets for users after they log in. These tickets can be used for authentication without the need for the user's password. Mimikatz can extract these tickets from memory and reuse them to authenticate as the user without knowing the actual password. This is known as Pass-the-Ticket.
Pass-the-Key (PTK):

Pass-the-Key involves extracting the NTLM or Kerberos authentication keys from LSASS (Local Security Authority Subsystem Service) memory. Once the keys are obtained, an attacker can use them to authenticate as the user without needing the actual password. This technique is effective for lateral movement within a network.
Pass-the-Hash (PTH):

This technique involves extracting password hashes (such as NTLM hashes) from memory instead of plaintext passwords. Mimikatz can obtain these hashes and use them to authenticate as the user, providing unauthorized access to systems. Pass-the-Hash is a common method for attackers to escalate privileges and move laterally within a network.
Pass-the-Certificate:

Pass-the-Certificate is a technique where Mimikatz extracts X.509 certificates and private keys from LSASS memory. These certificates can then be used to impersonate a user and access resources on a network. This technique is particularly effective in environments that use smart cards for authentication.
Pass-the-Provider:

This technique involves extracting authentication providers and their credentials from LSASS memory. Authentication providers are used in Windows to support different authentication mechanisms (e.g., smart cards, fingerprints). By extracting these providers, Mimikatz can obtain the associated credentials and use them for unauthorized access.
Overpass-the-Hash:

Overpass-the-Hash is a technique where Mimikatz intercepts the plaintext password during a password change process. When a user changes their password, the new password is provided in plaintext to LSASS. Mimikatz can intercept and extract this new password, allowing the attacker to gain unauthorized access.

What are four ways we can defend against Mimikatz attacks. Explain how two of the mitigations can stop Mimikatz. 

Regular Credential Rotations:

How it works: Regularly changing passwords and cryptographic keys reduces the window of opportunity for attackers. If Mimikatz extracts credentials, they become obsolete quickly.
Mitigation: Even if Mimikatz successfully captures credentials, frequent rotations limit the time an attacker can use them. Regularly changing service account passwords and ensuring strong password policies are essential components of this defense.
Application Whitelisting:

How it works: By allowing only authorized applications to run, application whitelisting prevents unauthorized tools like Mimikatz from executing on a system.
Mitigation: If Mimikatz is not allowed to run on a system due to application whitelisting policies, it becomes challenging for attackers to carry out credential-gathering activities using Mimikatz.


chatgpt.com
