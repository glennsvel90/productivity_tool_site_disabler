# productivity_tool_site_disabler

App that shows prevents sites from being accesse during working hours that can be adjusted.

The terminal program works by editing the host file on a windows computer. By listing the websites in the hosts file, these sites are not able to be accessed. After working hours, the program erases the name of the websites from the hosts file, which now allows the sites to be accessed.

## Getting Started

Clone the repository. Unzip the contents. Open the terminal and change directory to be located inside the repository. The hosts file need administrative permissions alloweable in order to be edited. To do this we have to right click the hosts file. The hosts file is located in C:\Windows\System32\drivers\etc\hosts. After right clicking the hosts file, go to properties. Then go to the security tab and click 'Edit' to change permissions. Click to highlight 'Users' Group or user names. Check all of the checkboxes that allow permissions. Allow permissions for 'Full control', 'Modify', 'Read & execute', 'Read', and 'Write'. Apply all of the permissions.

### Prerequisites

Python 3
Microsoft Windows

### Running the program

```
python site_disabler.py
```
