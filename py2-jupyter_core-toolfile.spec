### RPM external py2-jupyter_core-toolfile 1.0
Requires: py2-jupyter_core

%prep

%build

%install

mkdir -p %{i}/etc/scram.d
cat << \EOF_TOOLFILE >%{i}/etc/scram.d/py2-jupyter_core.xml
<tool name="py2-jupyter_core" version="@TOOL_VERSION@">
  <client>
    <environment name="PY2_JUPYTER_CORE_BASE" default="@TOOL_ROOT@"/>
  </client>
  <runtime name="PATH" value="$PY2_JUPYTER_CORE_BASE/bin" type="path"/>
</tool>
EOF_TOOLFILE


export PYTHON_LIB_SITE_PACKAGES
export PYTHON3_LIB_SITE_PACKAGES

## IMPORT scram-tools-post
