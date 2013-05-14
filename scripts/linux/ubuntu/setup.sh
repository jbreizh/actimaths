 #!/bin/bash
cd ..
cd ..
cd ..
cd src
python2 setup.py --command-packages=stdeb.command bdist_deb
