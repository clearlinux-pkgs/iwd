#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v25
# autospec commit: 9594167
#
Name     : iwd
Version  : 3.8
Release  : 73
URL      : https://mirrors.kernel.org/pub/linux/network/wireless/iwd-3.8.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/network/wireless/iwd-3.8.tar.gz
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
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(ell)
BuildRequires : pkgconfig(libedit)
BuildRequires : pkgconfig(readline)
BuildRequires : pkgconfig(systemd)
BuildRequires : pypi-docutils
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: systemd

%description services
services components for the iwd package.


%prep
%setup -q -n iwd-3.8
cd %{_builddir}/iwd-3.8
pushd ..
cp -a iwd-3.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1746641775
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-wired
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-wired
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1746641775
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iwd
cp %{_builddir}/iwd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/iwd/32c7c5556c56cdbb2d507e27d28d081595a35a9b || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/systemd/network/80-iwd.link

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/iwctl
/V3/usr/bin/iwmon
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
/V3/usr/libexec/ead
/V3/usr/libexec/iwd
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
