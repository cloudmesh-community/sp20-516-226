#!C:\Users\btrac\PycharmProjects\sp20-516-226\ENV3\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Pygments==2.5.2','console_scripts','pygmentize'
__requires__ = 'Pygments==2.5.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Pygments==2.5.2', 'console_scripts', 'pygmentize')()
    )
