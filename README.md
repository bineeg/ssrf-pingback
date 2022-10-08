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
    

    
