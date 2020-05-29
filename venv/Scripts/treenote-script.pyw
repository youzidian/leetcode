#!C:\workspace\Python\leetCode\venv\Scripts\pythonw.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'TreeNote==1.7.8','gui_scripts','treenote'
__requires__ = 'TreeNote==1.7.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('TreeNote==1.7.8', 'gui_scripts', 'treenote')()
    )
