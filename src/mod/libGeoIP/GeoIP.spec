Name:	    GeoIP
Version:    1.6.12
Summary:    GeoIP is a C library finds the location of an IP address.
Release:    1
Group:	    System Environment/Libraries
URL:	    http://dev.maxmind.com/geoip/downloadable
Vendor:	    MaxMind, Inc.
Source0:    http://www.maxmind.com/download/geoip/api/c/GeoIP-latest.tar.gz
License:    LGPLv2.1+
BuildRoot:  %{_tmppath}/%{name}-%{version}-root

%description
GeoIP is a C library that enables the user to find geographical and
network information of an IP address.
Included is a free GeoLite Country database
that is updated at the beginning of every month.
To download the latest free GeoLite databases, go to:
http://dev.maxmind.com/geoip/geolite

%package devel
Summary: GeoIP headers, libraries
Group: Development/Libraries
Requires: %name = %{version}

%description devel
This package contain the devel files for GeoIP.

%prep
%setup -q

%build
%configure
make
make check

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall
# Fixup permissions on shared libraries so that findreqs will work right.
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README.md TODO
%attr(0755,root,root) %{_libdir}/*.so.*.*
%{_bindir}/*
%{_sysconfdir}/*
%dir %{_datadir}/GeoIP
%{_datadir}/GeoIP/*
%{_libdir}/*.so
%{_mandir}/*/*

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Fri Apr 14 2006 Thomas Mather <support@maxmind.com>
- Updated description to reference free GeoLite City database

* Thu Jul  7 2005 Thomas Mather <support@maxmind.com>
- Updated description to reflect monthly updates for free country database.

* Mon Sep  8 2003 Dr. Peter Bieringer
- Fix for RHL 9, created a new devel package definition.

* Thu Feb 27 2003 Ryan Weaver <ryanw@falsehope.com>
- Initial RPM Build
