# autouiaviata
Automated UI testing framework with one aautotest without using assert from pytest.  

How to use:  
1.) Install all requirenments from requirenments.txt file, or use this list:  
		1. pip install selenium  
		2. pip install pytest  
		3. pip install webdriver-manager  
  
2.) Install Google Chrome (any version isn't necessary)  
3.) Download my code via zip file from github  
4.) Open main folder (001) with terminal and run command, it runs small UI test:  
		pytest -s -v  
 
P.S. if you don't need open a browser window, open conftest.py by IDE and put 'headless' instead of 'chrome' in 11 line  
