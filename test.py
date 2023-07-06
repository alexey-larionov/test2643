## Description: Read a file line by line
## Usage: python test.py
## Output: This is a test file.
## Note: test.txt file should be in the same directory as test.py
## Author: Prashant Srivastava (
## Creation Date: 2017-09-20 12:00:00
## Modification Date: 2017-09-20 12:00:00
## Version: 1.0
## Website: http://www.prashantsrivastava.com
## Subject: Python
## Category: File Handling
## Sub-Category: Read a file line by line
## Tested on OS: Kali Linux 4.12.0-kali1-amd64
## Tested with Python Version: Python 2.7.13
## Python snippet:
```python
#!/usr/bin/python

# Read the file
with open('test.txt', 'r') as f:
    lines = f.readlines()
    # print lines one by one
    for line in lines:
        print line
```
Output:
```
$ python test.py
This is a test file.
```


