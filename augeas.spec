Summary:	Augeas is configuration editing tool
Summary(pl.UTF-8):	Augeas to narzędzie do edytowania konfiguracji
Name:		augeas
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://augeas.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	e425bcfc46fd5b18473a4ff47c2878d3
Patch0:		%{name}-pld_interfaces.patch
URL:		http://augeas.net
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

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

%description devel
This package contains the include files used to develop using augeas
APIs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkow służące do programowania z użyciem
API augeasa.

%package static
Summary:	Ageas static libraries
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
%configure

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
%attr(755,root,root) %{_bindir}/augparse
%attr(755,root,root) %{_bindir}/augtool
%attr(755,root,root) %{_bindir}/fadot
%{_datadir}/augeas
%{_mandir}/man1/augparse.1.*
%{_mandir}/man1/augtool.1.*
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
%{_includedir}/augeas.h
%{_includedir}/fa.h
%attr(755,root,root) %{_libdir}/libaugeas.a
%attr(755,root,root) %{_libdir}/libaugeas.so
%attr(755,root,root) %{_libdir}/libfa.a
%attr(755,root,root) %{_libdir}/libfa.so
%{_pkgconfigdir}/augeas.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libaugeas.la
%{_libdir}/libfa.la
