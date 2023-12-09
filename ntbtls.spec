#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Not Too Bad Transport Layer Security
Summary(pl.UTF-8):	Not Too Bad Transport Layer Security - "nie taka zła" implementacja TLS
Name:		ntbtls
Version:	0.3.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/ntbtls/%{name}-%{version}.tar.bz2
# Source0-md5:	970dd056419b98594b3318e3dc552cb9
URL:		https://wiki.gnupg.org/NTBTLS
BuildRequires:	libgcrypt-devel >= 1.9.0
BuildRequires:	libgpg-error-devel >= 1.25
BuildRequires:	libksba-devel >= 1.2.0
BuildRequires:	zlib-devel
Requires:	libgcrypt >= 1.9.0
Requires:	libgpg-error >= 1.25
Requires:	libksba >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NTBTLS ("Not Too Bad TLS") is a TLS client-only library developed by
Werner Koch.

It started (2014) as a stripped down fork of PolarSSL (now called mbed
tls), using libgcrypt and existing GnuPG modules for X.509 certificate
handling.

%description -l pl.UTF-8
MTBTLS ("Not Too Bad TLS" - nie taki zły TLS) to biblioteka
(wyłącznie) kliencka TLS tworzona przez Wernera Kocha.

Projekt wystartował w 2014 roku jako przycięte odgałęzienie projektu
PolarSSL (teraz mającego nazwę mbed tls), wykorzystujące libgcrypt
oraz istniejące moduły GnuPG do obsługi certyfikatów X.509.

%package devel
Summary:	Header files for NTBTLS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki NTBTLS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.9.0
Requires:	libgpg-error-devel >= 1.25
Requires:	libksba-devel >= 1.2.0
Requires:	zlib-devel

%description devel
Header files for NTBTLS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki NTBTLS.

%package static
Summary:	Static NTBTLS library
Summary(pl.UTF-8):	Statyczna biblioteka NTBTLS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static NTBTLS library.

%description static -l pl.UTF-8
Statyczna biblioteka NTBTLS.

%prep
%setup -q

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libntbtls.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libntbtls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libntbtls.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libntbtls.so
%{_includedir}/ntbtls.h
%{_pkgconfigdir}/ntbtls.pc
%{_aclocaldir}/ntbtls.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libntbtls.a
%endif
