Summary:	LibASS - SSA/ASS subtitles rendering library
Summary(pl.UTF-8):	LibASS - biblioteka renderująca napisy SSA/ASS
Name:		libass
Version:	0.9.11
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/libass/downloads/list
Source0:	http://libass.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	f9042884397002ba40aa89dc7d34f59f
URL:		http://code.google.com/p/libass/
BuildRequires:	enca-devel
BuildRequires:	fontconfig-devel >= 2.4.2
BuildRequires:	freetype-devel >= 1:2.4.0
BuildRequires:	pkgconfig
Requires:	fontconfig-libs >= 2.4.2
Requires:	freetype >= 1:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibASS is a portable subtitle renderer for the ASS/SSA (Advanced
Substation Alpha/Substation Alpha) subtitle format. It is mostly
compatible with VSFilter.


%description -l pl.UTF-8
LibASS to przenośna biblioteka renderująca napisy w formacie ASS/SSA
(Advanced Substation Alpha/Substation Alpha). Jest w większości
kompatybilna z VSFiltrem.

%package devel
Summary:	Header files for LibASS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LibASS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	enca-devel
Requires:	fontconfig-devel >= 2.4.2
Requires:	freetype-devel >= 1:2.4.0

%description devel
This package contains the header files for developing applications
that use LibASS library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę LibASS.

%package static
Summary:	Static LibASS library
Summary(pl.UTF-8):	Statyczna biblioteka LibASS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibASS library.

%description static -l pl.UTF-8
Statyczna biblioteka LibASS.

%prep
%setup -q

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_libdir}/libass.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libass.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libass.so
%{_libdir}/libass.la
%{_includedir}/ass
%{_pkgconfigdir}/libass.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libass.a
