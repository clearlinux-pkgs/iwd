#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iwd
Version  : 1.15
Release  : 22
URL      : https://www.kernel.org/pub/linux/network/wireless/iwd-1.15.tar.xz
Source0  : https://www.kernel.org/pub/linux/network/wireless/iwd-1.15.tar.xz
Summary  : Wireless daemon for Linux
Group    : Development/Tools
License  : LGPL-2.1
Requires: iwd-bin = %{version}-%{release}
Requires: iwd-config = %{version}-%{release}
Requires: iwd-data = %{version}-%{release}
Requires: iwd-libexec = %{version}-%{release}
Requires: iwd-license = %{version}-%{release}
Requires: iwd-man = %{version}-%{release}
Requires: iwd-services = %{version}-%{release}
BuildRequires : docutils
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(ell)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(systemd)
BuildRequires : readline-dev

%description
Wireless daemon for Linux
*************************
Compilation and installation
============================

%package bin
Summary: bin components for the iwd package.
Group: Binaries
Requires: iwd-data = %{version}-%{release}
Requires: iwd-libexec = %{version}-%{release}
Requires: iwd-config = %{version}-%{release}
Requires: iwd-license = %{version}-%{release}
Requires: iwd-services = %{version}-%{release}

%description bin
bin components for the iwd package.


%package config
Summary: config components for the iwd package.
Group: Default

%description config
config components for the iwd package.


%package data
Summary: data components for the iwd package.
Group: Data

%description data
data components for the iwd package.


%package libexec
Summary: libexec components for the iwd package.
Group: Default
Requires: iwd-config = %{version}-%{release}
Requires: iwd-license = %{version}-%{release}

%description libexec
libexec components for the iwd package.


%package license
Summary: license components for the iwd package.
Group: Default

%description license
license components for the iwd package.


%package man
Summary: man components for the iwd package.
Group: Default

%description man
man components for the iwd package.


%package services
Summary: services components for the iwd package.
Group: Systemd services

%description services
services components for the iwd package.


%prep
%setup -q -n iwd-1.15
cd %{_builddir}/iwd-1.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623683626
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-wired
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1623683626
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iwd
cp %{_builddir}/iwd-1.15/COPYING %{buildroot}/usr/share/package-licenses/iwd/32c7c5556c56cdbb2d507e27d28d081595a35a9b
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/systemd/network/80-iwd.link

%files bin
%defattr(-,root,root,-)
/usr/bin/iwctl
/usr/bin/iwmon

%files config
%defattr(-,root,root,-)
/usr/lib/modules-load.d/pkcs8.conf

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system-services/net.connman.ead.service
/usr/share/dbus-1/system-services/net.connman.iwd.service
/usr/share/dbus-1/system.d/ead-dbus.conf
/usr/share/dbus-1/system.d/iwd-dbus.conf

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ead
/usr/libexec/iwd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iwd/32c7c5556c56cdbb2d507e27d28d081595a35a9b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/iwctl.1
/usr/share/man/man1/iwmon.1
/usr/share/man/man5/iwd.ap.5
/usr/share/man/man5/iwd.config.5
/usr/share/man/man5/iwd.network.5
/usr/share/man/man7/iwd.debug.7
/usr/share/man/man8/ead.8
/usr/share/man/man8/iwd.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ead.service
/usr/lib/systemd/system/iwd.service
