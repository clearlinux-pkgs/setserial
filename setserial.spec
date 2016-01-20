#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : setserial
Version  : 2.17
Release  : 1
URL      : http://downloads.sourceforge.net/project/setserial/setserial/2.17/setserial-2.17.tar.gz
Source0  : http://downloads.sourceforge.net/project/setserial/setserial/2.17/setserial-2.17.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: setserial-bin
Requires: setserial-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : groff
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: build.patch

%description
setserial Version 2.17 (27-Jan-2000)
Setserial is a program which allows you to look at and change various
attributes of a serial device, including its port, its IRQ, and other
serial port options.

%package bin
Summary: bin components for the setserial package.
Group: Binaries

%description bin
bin components for the setserial package.


%package doc
Summary: doc components for the setserial package.
Group: Documentation

%description doc
doc components for the setserial package.


%prep
%setup -q -n setserial-2.17
%patch1 -p1

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/setserial

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
