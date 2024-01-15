Readings: Cloud Identity and Access Management (IAM) with AWS
Below you will find reading materials and additional resources that support today’s topic and the upcoming lecture.

Review the Submission Instructions for guidance on completing and submitting this assignment.

Reading
Lessons Learned from the Capital One Data Breach (PDF)

What were the three commands used for the attack? Code for 3 commands used for the attack
• Get Credentials - First command when executed obtained security
credentials known as ****-WAF-Role account (an IAM account) for an
elevated role access AWS Web Application Firewall (WAF)
• List Buckets - Second command, when executed, used the security
credentials *****-WAF-Role account to list files and folders (aka S3 buckets)
• Download Files - Third command, when executed used the *****-WAF-Role
account to download files that were accessible by the credentials
What misconfiguration of AWS components allowed the attacker to access sensitive data? the most likely root cause of the attack was a poor security architecture design that exposed S3
buckets via AWS WAF/EC2 instance to anyone with an IAM role. While S3 buckets were not exposed to the
Internet like many other breaches, an EC2 instance with an excessive IAM role might have been the culprit.
The deployed architecture would have looked something like this. It was a trivial step to “compromise” the
poorly configured WAF.
What are two of the AWS Governance practices that could have prevented such attack? e following AWS governance practices would prevent such attacks:
1. 	 Review all access paths and permissions from human identities or non-human identities (e.g., ec2
	 machine) to data storages (e.g., S3 buckets). Use Cloud Infrastructure Entitlement Management 		
	 (CIEM) solutions to automate the detection of over-privileged identities and over-exposed data.
2. 	 AWS lists a few basics here https://aws.amazon.com/premiumsupport/knowledge-center/secure-	
	 s3-resources/. Zscaler Workload Posture with Cloud Security Posture Management (CSPM) 	 	
	 automates 100’s of these policies. It provides security and compliance views across all AWS, 	 	
	 including verification of the use of version 2 of the EC2 Metadata service instead of version 1 that
	 would have prevented the compromise of the credentials.
© Code Fellows 2024
