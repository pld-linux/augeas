Summary:	Augeas - configuration editing tool
Summary(pl.UTF-8):	Augeas - narzędzie do modyfikowania konfiguracji
Name:		augeas
Version:	0.8.1
Release:	1
License:	LGPL v2.1+
Group:		Applications/System
Source0:	http://augeas.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	62d47bdc60e175f93aed3b81cb8e2785
Patch0:		%{name}-pld_interfaces.patch
URL:		http://augeas.net
BuildRequires:	libselinux-devel
BuildRequires:	readline-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Augeas is a library and command line tool that focuses on the most
basic problem in handling Linux configurations programmatically:
editing actual configuration files in a controlled manner.

%description -l pl.UTF-8
Augeas to biblioteka i działające z linii poleceń narzędzie
skupiające się na najbardziej podstawowym problemie przy programowej
obsłudze konfiguracji Linuksa: modyfikowaniu w sposób kontrolowany
właściwych plików konfiguracyjnych.

%package libs
Summary:	Augeas libraries
Summary(pl.UTF-8):	Biblioteki augeasa
Group:		Libraries

%description libs
This package contains the augeas libraries.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki augeasa.

%package devel
Summary:	Augeas development files
Summary(pl.UTF-8):	Pliki programistyczne augeasa
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libselinux-devel

%description devel
This package contains the include files used to develop using augeas
APIs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkow służące do programowania z użyciem
API augeasa.

%package static
Summary:	Augeas static libraries
Summary(pl.UTF-8):	Statyczne biblioteki augeasa
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains augeas static libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki augeasa.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/augparse
%attr(755,root,root) %{_bindir}/augtool
%attr(755,root,root) %{_bindir}/fadot
%{_datadir}/augeas
%{_mandir}/man1/augparse.1*
%{_mandir}/man1/augtool.1*
#%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
#%{_datadir}/vim/vimfiles/syntax/augeas.vim

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaugeas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaugeas.so.0
%attr(755,root,root) %{_libdir}/libfa.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfa.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaugeas.so
%attr(755,root,root) %{_libdir}/libfa.so
%{_libdir}/libaugeas.la
%{_libdir}/libfa.la
%{_includedir}/augeas.h
%{_includedir}/fa.h
%{_pkgconfigdir}/augeas.pc

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaugeas.a
%attr(755,root,root) %{_libdir}/libfa.a
