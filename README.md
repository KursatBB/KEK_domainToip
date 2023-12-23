# Domain to IP
Gets the IP's of active domains and writes txt. If you want to get xlsx output, gives the xlsx output with table.

# Usage
you can start typing `python domainToip.py` . Filename and output parameter is required.

### Example
`python domainToip.py -f domainlist.txt -o kek.txt`
### Help
```
  options:
    -h, --help            show this help message and exit
    -f FILENAME, --filename FILENAME
                          The filename/filepath to get domains from
    -o OUTPUT, --output OUTPUT
                          The output path and name of the IPs, this will automatically create a txt file. dont write extension      
    -x, --excel           If you want to excel output
```
