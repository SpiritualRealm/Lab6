# **Lab 8 Report**  
##### CSCY 4742: Cybersecurity Programming and Analytics, Spring 2026

**Name & Student ID**: Earnest Kyle, 109969905 

---

# **Task 1: Snort Setup and Basic Packet Capture (20 pts)**

---

## **🔹 Step 1: Snort Installation and Configuration**

### **Questions**:
1. How many rules were loaded when Snort started? What does this number tell you about the configuration?
2. Did Snort report any warnings or errors during startup? Explain.
3. What interface did Snort bind to? Was it the expected one? Why is selecting the correct interface important?
4. What output mode was used (`alert_fast`, etc.)? Briefly explain differences between modes and appropriate use cases.

### **Screenshots**:
- Screenshot of successful Snort startup (`Snort successfully validated the configuration`).
- Screenshot of `snort.lua` showing updated `HOME_NET`.

---

## **🔹 Step 2: Simulating and Detecting a Port Scan**

### **Questions**:
1. What types of scan activity did Snort detect from the Nmap scan? Provide examples.
2. Which ports or protocols were probed by Nmap? Mention a few and their significance.
3. How did promiscuous mode help in detection?
4. Compare Snort alerts and Wireshark output. What extra insights does Wireshark provide?

### **Screenshots**:
- Snort console showing scan-related alerts.
- Wireshark packet capture showing SYN scan activity.

---

# **Task 2: Writing Custom Rules – ICMP, FIN, NULL, and Xmas Scan Detection (20 pts)**

---

## **Deliverables for Task 2**

### **Questions**:
1. Why are FIN, NULL, and Xmas scans considered stealthy compared to normal TCP scans?
2. What do the flags `F`, `0`, and `FPU` represent in these rules?
3. Compare Snort detection with Wireshark TCP flag analysis.
4. What `classtype` would you select for these rules and why?

### **Screenshots**:
- Snort alert showing ICMP detection.
- Snort alerts for FIN, NULL, and Xmas scans.
- Wireshark TCP flag views for one FIN, one NULL, and one Xmas packet.

---

# **Task 3: FTP Login and Brute Force Detection (20 pts)**

---

## **Deliverables for Task 3**

### **Questions**:
1. What does the `"530 "` FTP response indicate, and why is it useful for detection?
2. Why is `flow:from_server,established` needed for failed login detection?
3. Explain `detection_filter:track by_src, count 3, seconds 60;` and how it works.
4. How does thresholding (`detection_filter`) help reduce alert fatigue?
5. How would you improve the FTP detection rules for a production deployment?

### **Screenshots**:
- Snort alert for FTP connection attempt.
- Snort alert for FTP failed login.
- Snort alert for FTP brute force detection.

---

# **Task 4: Sensitive Data Exfiltration Detection via FTP (20 pts)**

---

## **Deliverables for Task 4**

### **Questions**:
1. Why is regex (PCRE) used instead of simple content matching for SSN detection?
2. Why is FTP considered dangerous for transmitting sensitive data like SSNs?
3. How could attackers exploit anonymous FTP servers?
4. How would detection change if traffic were encrypted (SSH, FTPS, SFTP)?

### **Screenshots**:
- Snort alert triggered for SSN leak detection.
- Wireshark capture showing SSN pattern during file transfer.

---

# **Task 5: SYN Flood Detection and Thresholding (20 pts)**

---

## **Deliverables for Task 5**

### **Questions**:
1. Why is `detection_filter` important for detecting SYN floods?
2. Why is `event_filter` important? What happens if we do not define this?
3. How would using `--rand-source` affect Snort’s detection?
4. Why can't Snort itself block SYN floods directly?
5. How could a firewall or IPS help defend against SYN floods?

### **Screenshots**:
- Snort alert showing SYN flood detection.
- Screenshot of `local.rules` containing the correct SYN flood rule.
- Screenshot of `snort.lua` showing the correct `event_filter`.


