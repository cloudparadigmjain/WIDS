# WIDS - Wireless Intrusion Detection System

## **Requirements:**
* A Network Adaptor with _prefrably_ Packet Injection Capabilities - Tenda or Alpha
* A Kali Linux Operating System
* Twilio Account with SMS API - **Account SID with Auth Token**
* A Gmail Account to send Email alerts from - Should have [Less Secure App Access](https://myaccount.google.com/lesssecureapps) Enabled 

# Initial Setup
1.  Setting the External Adaptor in Monitor Mode
* Navigate to _adaptormon.py_ and _tsharkmodule.py_ file and change `wlan1` to your external adaptor's current interface(Can be found out by `ifconfig`).

2. Setting up Twilio for Alerting through SMS
* Navigate to _send.py_ and _fchkandsendmail.py_ **and** add in your ** Account_SID and auth_token** provided to you by Twilio.
* You will also need to add **1**) All Reciever Numbers in {`Numbers_to_message`}) and **2)** Sender Phone Number provided to you by Twilio in `from_`.

3. Email Address from which Emails will be sent from(and it's authentication will happen in Run Time- **Secured by TLS**)

4. Email Address to which the alerts will have to reach (the nearest network administrator) is also added at Runtime.

# Usage:
Run: `$python run.py`
