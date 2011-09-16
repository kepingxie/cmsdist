### RPM external bz2lib 1.0.5
# Build system patches by Lassi A. Tuura <lat@iki.fi>
Source: http://www.bzip.org/%realversion/bzip2-%realversion.tar.gz
%define cpu %(echo %cmsplatf | cut -f2 -d_)
Provides: libbz2.so.1
%if "%cpu" == "amd64"
Provides: libbz2.so.1()(64bit)
%endif

%prep
%setup -n bzip2-%realversion
sed -e 's/ -shared/ -dynamiclib/' \
    -e 's/ -Wl,-soname -Wl,[^ ]*//' \
    -e 's/libbz2\.so/libbz2.dylib/g' \
    < Makefile-libbz2_so > Makefile-libbz2_dylib

%build
case $(uname) in Darwin ) so=dylib ;; * ) so=so ;; esac
make %makeprocesses -f Makefile-libbz2_$so

%install
case $(uname) in Darwin ) so=dylib ;; * ) so=so ;; esac
make install PREFIX=%i
# For bzip2 1.0.5, the library appears to retain the name libbz2.so.1.0.4
# rather than libbz2.so.1.0.5 as one would expect, so use this "tmpversion"
# instead of realversion
%define tmpversion 1.0.4
cp libbz2.$so.%tmpversion %i/lib
ln -s libbz2.$so.%tmpversion %i/lib/libbz2.$so
ln -s libbz2.$so.%tmpversion %i/lib/libbz2.$so.`echo %tmpversion | cut -d. -f 1,2`
ln -s libbz2.$so.%tmpversion %i/lib/libbz2.$so.`echo %tmpversion | cut -d. -f 1`
ln -sf bzdiff %i/bin/bzcmp
ln -sf bzgrep %i/bin/bzegrep
ln -sf bzgrep %i/bin/bzfgrep
ln -sf bzmore %i/bin/bzless

# Strip libraries, we are not going to debug them.
find %i/lib -type f -perm -a+x -exec strip {} \;

# Don't need archive libraries.
rm -f %i/lib/*.{l,}a

# Look up documentation online.
rm -rf %i/man
