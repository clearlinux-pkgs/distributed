#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : distributed
Version  : 1.25.3
Release  : 1
URL      : https://files.pythonhosted.org/packages/fc/73/39f7ddf1bc12e2bcc6ba7e5152107fd53398dbe7c8839f95161da5605615/distributed-1.25.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/fc/73/39f7ddf1bc12e2bcc6ba7e5152107fd53398dbe7c8839f95161da5605615/distributed-1.25.3.tar.gz
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
Requires: futures
Requires: msgpack
Requires: psutil
Requires: singledispatch
Requires: six
Requires: sortedcontainers
Requires: toolz
Requires: tornado
BuildRequires : buildreq-distutils3

%description
Distributed
===========
A library for distributed computation.  See documentation_ for more details.

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
%setup -q -n distributed-1.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549029612
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/distributed
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/distributed/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dask-mpi
/usr/bin/dask-remote
/usr/bin/dask-scheduler
/usr/bin/dask-ssh
/usr/bin/dask-submit
/usr/bin/dask-worker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/distributed/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
