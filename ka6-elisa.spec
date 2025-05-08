#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.04.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		elisa
Summary:	Elisa music player
Name:		ka6-%{kaname}
Version:	25.04.1
Release:	1
License:	LGPL v3+
Group:		Applications/Multimedia
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	283a26922ac864fbd7dc9212199ccb46
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel >= 5.15.2
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel >= 5.15.2
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel >= 5.15.2
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	kf6-baloo-devel >= 5.85.0
BuildRequires:	kf6-extra-cmake-modules >= 5.85.0
BuildRequires:	kf6-kauth-devel >= 5.92.0
BuildRequires:	kf6-kcodecs-devel >= 5.92.0
BuildRequires:	kf6-kcompletion-devel >= 5.92.0
BuildRequires:	kf6-kconfig-devel >= 5.92.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.92.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.92.0
BuildRequires:	kf6-kcrash-devel >= 5.85.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.85.0
BuildRequires:	kf6-kdeclarative-devel >= 5.85.0
BuildRequires:	kf6-kdoctools-devel >= 5.85.0
BuildRequires:	kf6-kfilemetadata-devel >= 5.85.0
BuildRequires:	kf6-ki18n-devel >= 5.85.0
BuildRequires:	kf6-kiconthemes-devel >= 5.85.0
BuildRequires:	kf6-kio-devel >= 5.85.0
BuildRequires:	kf6-kirigami-devel >= 5.85.0
BuildRequires:	kf6-kitemviews-devel >= 5.92.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.92.0
BuildRequires:	kf6-kpackage-devel >= 5.85.0
BuildRequires:	kf6-kservice-devel >= 5.92.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.92.0
BuildRequires:	kf6-kxmlgui-devel >= 5.92.0
BuildRequires:	kf6-solid-devel >= 5.92.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-phonon-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	vlc-devel
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Elisa is a simple music player aiming to provide a nice experience for
its users. Elisa allows to browse music by album, artist or all
tracks. The music is indexed using either a private indexer or an
indexer using Baloo. The private one can be configured to scan music
on chosen paths. The Baloo one is much faster because Baloo is
providing all needed data from its own database. You can build and
play your own playlist.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elisa
%dir %{_libdir}/elisa
%ghost %{_libdir}/elisa/libelisaLib.so.0
%attr(755,root,root) %{_libdir}/elisa/libelisaLib.so.0.1
%{_desktopdir}/org.kde.elisa.desktop
%{_datadir}/dbus-1/services/org.kde.elisa.service
%{_iconsdir}/hicolor/128x128/apps/elisa.png
%{_iconsdir}/hicolor/16x16/apps/elisa.png
%{_iconsdir}/hicolor/22x22/apps/elisa.png
%{_iconsdir}/hicolor/32x32/apps/elisa.png
%{_iconsdir}/hicolor/48x48/apps/elisa.png
%{_iconsdir}/hicolor/64x64/apps/elisa.png
%{_iconsdir}/hicolor/scalable/apps/elisa.svg
%{_datadir}/metainfo/org.kde.elisa.appdata.xml
%{_datadir}/qlogging-categories6/elisa.categories
