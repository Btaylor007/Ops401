Readings: XSS with w3af, DVWA
Below you will find reading materials and additional resources that support today’s topic and the upcoming lecture.

Review the Submission Instructions for guidance on completing and submitting this assignment.

Reading
Cross-site scripting


Explain how a cross-site scripting attack works in non-technical terms.
t's like someone sneaking a hidden message or harmful content onto your favorite website, and when you visit that site, you unwittingly activate or execute their malicious instructions.

What are the three types of XSS attacks?

Stored XSS (Persistent XSS):

In a Stored XSS attack, the malicious script is permanently stored on the target server. This typically occurs when user input is not properly validated or sanitized before being stored in a database.
When a user requests a particular page, the server retrieves the stored script and includes it in the response sent to the user's browser.
The victim, unaware of the presence of the malicious script, executes it when they visit the compromised page.
Reflected XSS (Non-Persistent XSS):

Reflected XSS involves the injection of a malicious script that is not permanently stored on the target server. Instead, it is included in the response sent directly to the victim's browser.
This type of attack often relies on tricking users into clicking on a specially crafted link that contains the malicious payload.
The injected script is then reflected back to the user within the response, executing in the context of their current session.
DOM-based XSS:

DOM-based XSS (Document Object Model-based XSS) occurs when the client-side script manipulates the Document Object Model (DOM) of a web page.
Unlike traditional XSS attacks that involve server-side vulnerabilities, DOM-based XSS takes advantage of flaws in the client-side script itself.
The attack is usually initiated by manipulating the DOM through changes in the URL or other client-side data, leading to the execution of malicious code.
If an attacker successfully exploits a XSS vulnerability, what malicious actions would they be able to perform? the impact of an XSS attack can vary depending on the attacker's goals and the specific vulnerabilities present on the targeted website


What are some security controls that can be implemented to prevent XSS attacks?
Headers Help: Sites tell browsers how to deal with content, blocking sneaky notes.
Content Rules (CSP): Sites set rules to allow only safe stuff, blocking risky notes.

Bookmark and Review
Security Report for In-Production Web Applications
chatgpt
