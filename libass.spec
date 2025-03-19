Summary:	LibASS - SSA/ASS subtitles rendering library
Summary(pl.UTF-8):	LibASS - biblioteka renderująca napisy SSA/ASS
Name:		libass
Version:	0.17.3
Release:	1
License:	MIT-like
Group:		Libraries
#Source0Download: https://github.com/libass/libass/releases
Source0:	https://github.com/libass/libass/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	baed6dfc87bed705c1955cc6b932d7f6
URL:		https://github.com/libass/libass/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	fontconfig-devel >= 1:2.10.92
# pkgconfig(freetype2) >= 9.17.3
BuildRequires:	freetype-devel >= 1:2.3.6
BuildRequires:	fribidi-devel >= 0.19.1
BuildRequires:	harfbuzz-devel >= 1.2.3
BuildRequires:	libtool >= 2:2
BuildRequires:	libunibreak-devel >= 1.1
%ifarch %{ix86} %{x8664} x32
BuildRequires:	nasm
%endif
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	fontconfig-libs >= 1:2.10.92
Requires:	freetype >= 1:2.3.6
Requires:	fribidi >= 0.19.1
Requires:	harfbuzz >= 1.2.3
Requires:	libunibreak >= 1.1
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
Requires:	fontconfig-devel >= 1:2.10.92
Requires:	freetype-devel >= 1:2.3.6
Requires:	fribidi-devel >= 0.19.1
Requires:	harfbuzz-devel >= 1.2.3
Requires:	libunibreak-devel >= 1.1

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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libass.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING Changelog
%attr(755,root,root) %{_libdir}/libass.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libass.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libass.so
%{_includedir}/ass
%{_pkgconfigdir}/libass.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libass.a
