#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distributed
Version  : 2.8.1
Release  : 28
URL      : https://files.pythonhosted.org/packages/65/2f/df6a239ca9792585915c840d224becd35aaa3adcdc04215d10234679bc2f/distributed-2.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/2f/df6a239ca9792585915c840d224becd35aaa3adcdc04215d10234679bc2f/distributed-2.8.1.tar.gz
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
BuildRequires : sortedcontainers
BuildRequires : tblib
BuildRequires : toolz
BuildRequires : tornado
BuildRequires : zict

%description
Distributed
===========
|Build Status| |Doc Status| |Gitter| |Version Status| |NumFOCUS|

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

%description python3
python3 components for the distributed package.


%prep
%setup -q -n distributed-2.8.1
cd %{_builddir}/distributed-2.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574693978
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
cp %{_builddir}/distributed-2.8.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/distributed/f43ec84283c31d12e523a8b1abbf7428fdfa5f6a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dask-remote
/usr/bin/dask-scheduler
/usr/bin/dask-ssh
/usr/bin/dask-submit
/usr/bin/dask-worker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distributed/f43ec84283c31d12e523a8b1abbf7428fdfa5f6a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
