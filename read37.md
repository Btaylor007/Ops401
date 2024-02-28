Readings: Automated AppSec with ZAP
Below you will find reading materials and additional resources that support today’s topic and the upcoming lecture.

Review the Submission Instructions for guidance on completing and submitting this assignment.

Reading
Getting Started with Zed Attack Proxy

What are the three common stages of the Penetration Testing process and what tasks are performed at each one?  Pre-Engagement- preparation , Engagement- Actions , Post Engagement AFtermath

Explain a “main-in-the-middle proxy” in non-technical terms. Someone between the person your conversating with catfishes you 

What are the 2 spiders available for use in ZAP?
Show drafts










ZAP offers 2 distinct spiders to explore and discover web application vulnerabilities:

Traditional ZAP Spider: This spider operates like a web crawler, examining the HTML code within responses from the target web application. It efficiently identifies links embedded in the HTML, making it a fast option for basic exploration. However, its effectiveness diminishes when dealing with modern web applications heavily reliant on JavaScript for generating dynamic content and links.

AJAX Spider: This spider leverages browsers to navigate the web application. It simulates user interactions and follows links created dynamically through JavaScript, making it adept at exploring AJAX-heavy applications. While the AJAX spider provides a more thorough exploration, it's generally slower than the traditional spider and might require additional configuration for headless (without a graphical user interface) environments.

What situations are they best suited for?

Bookmark and Review
Python Tools for Cyber
