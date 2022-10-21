# SSRF PINGBACK
Python script to check SSRF pingback



![out](https://user-images.githubusercontent.com/72538652/194700614-08a8c378-d202-49a7-a525-904f2ea0193e.png)


Run using python
    
    python3 ssrf-pingback.py
    
Direct invoke from terminal
    
    chmod +x ssrf-pingback.py
    sudo mv ssrf-pingback.py /usr/local/bin
		



Create input url file

Install qsreplace  https://github.com/tomnomnom/qsreplace 
    
    cat urls.txt | qsreplace burp-collaborator-url > url-file.txt
    

    
What is biid and how to capture it 

Biid is a persistent url for getting poll results for burp collaborators. For each burp collaborator string there is a unique biid url.
For capturing the biid.

Open Burp Suite , go to =>  Project Options  => Misc => tickmark , Poll over unencrypted HTTP


![poll-over-un](https://user-images.githubusercontent.com/72538652/197195032-0af6fa56-2a48-4659-9ed5-b95b7195dc7e.png)

Generate one collaborator payload , note down the payload id.
Open wireshark , trigger above generated payload in any browser.
Find biid in wireshark by the filter ‘http’ and search string ‘biid’.
	Note down collaborator id and biid. Both are persistent.
	
![wireshark](https://user-images.githubusercontent.com/72538652/197195171-55f22425-4178-46d4-abb0-02b735fb2119.png)

