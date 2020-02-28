#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distributed
Version  : 2.11.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/11/ca/c0bfa813387130c8f4b2578abcd852392f5915e1ee3378489b902d069cca/distributed-2.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/ca/c0bfa813387130c8f4b2578abcd852392f5915e1ee3378489b902d069cca/distributed-2.11.0.tar.gz
Summary  : Distributed scheduler for Dask
Group    : Development/Tools
License  : BSD-3-Clause
Requires: distributed-bin = %{version}-%{release}
Requires: distributed-license = %{version}-%{release}
Requires: distributed-python = %{version}-%{release}
Requires: distributed-python3 = %{version}-%{release}
Requires: PyYAML
Requires: click
Requires: cloudpickle
Requires: dask
Requires: msgpack
Requires: psutil
Requires: setuptools
Requires: sortedcontainers
Requires: tblib
Requires: toolz
Requires: tornado
Requires: zict
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : cloudpickle
BuildRequires : dask
BuildRequires : msgpack
BuildRequires : psutil
BuildRequires : setuptools
BuildRequires : sortedcontainers
BuildRequires : tblib
BuildRequires : toolz
BuildRequires : tornado
BuildRequires : zict

%description
Distributed
===========

|Linux Build Status| |Windows Build Status| |Doc Status| |Gitter| |Version Status| |NumFOCUS|

A library for distributed computation.  See documentation_ for more details.

.. _documentation: https://distributed.dask.org
.. |Linux Build Status| image:: https://travis-ci.org/dask/distributed.svg?branch=master
   :target: https://travis-ci.org/dask/distributed
.. |Windows Build Status| image:: https://github.com/dask/distributed/workflows/Windows%20CI/badge.svg?branch=master
   :target: https://github.com/dask/distributed/actions?query=workflow%3A%22Windows+CI%22
.. |Doc Status| image:: https://readthedocs.org/projects/distributed/badge/?version=latest
   :target: https://distributed.dask.org
   :alt: Documentation Status
.. |Gitter| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/dask/dask
   :target: https://gitter.im/dask/dask?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Version Status| image:: https://img.shields.io/pypi/v/distributed.svg
   :target: https://pypi.python.org/pypi/distributed/
.. |NumFOCUS| image:: https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A
   :target: https://www.numfocus.org/

%package bin
Summary: bin components for the distributed package.
Group: Binaries
Requires: distributed-license = %{version}-%{release}

%description bin
bin components for the distributed package.


%package license
Summary: license components for the distributed package.
Group: Default

%description license
license components for the distributed package.


%package python
Summary: python components for the distributed package.
Group: Default
Requires: distributed-python3 = %{version}-%{release}

%description python
python components for the distributed package.


%package python3
Summary: python3 components for the distributed package.
Group: Default
Requires: python3-core
Provides: pypi(distributed)

%description python3
python3 components for the distributed package.


%prep
%setup -q -n distributed-2.11.0
cd %{_builddir}/distributed-2.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582917230
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distributed
cp %{_builddir}/distributed-2.11.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/distributed/f43ec84283c31d12e523a8b1abbf7428fdfa5f6a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dask-scheduler
/usr/bin/dask-ssh
/usr/bin/dask-worker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distributed/f43ec84283c31d12e523a8b1abbf7428fdfa5f6a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
