### RPM external py2-ipython 5.5.0
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}


%define pip_name ipython
Requires: py2-prompt_toolkit py2-pathlib2 py2-traitlets py2-simplegeneric py2-six py2-wcwidth py2-ptyprocess py2-packaging py2-Pygments py2-appdirs py2-setuptools py2-pexpect py2-pyparsing py2-ipython_genutils py2-pickleshare py2-decorator py2-scandir 

## IMPORT build-with-pip

%define PipPostBuild \
   perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/*; perl -p -i -e "s|^#!.*python3|#!/usr/bin/env python3|" %{i}/bin/*


