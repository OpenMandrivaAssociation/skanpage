#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: plasma6-skanpage
Version: 24.02.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/skanpage/-/archive/%{gitbranch}/skanpage-%{gitbranchd}.tar.bz2#/skanpage-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/utilities/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/skanpage/-/archive/%{gitbranch}/skanpage-%{gitbranchd}.tar.bz2#/skanpage-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/skanpage-%{version}.tar.xz
%endif
%endif
Summary: Utility to scan images and multi-page documents
URL: https://github.com/skanpage/skanpage
License: GPL
Group: Utilities
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(tesseract)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlModels)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Purpose)
BuildRequireS: cmake(KF6Config)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KSaneCore6)
BuildRequires: cmake(KQuickImageEditor)
Provides: scanner-gui

%description
Utility to scan images and multi-page documents

%prep
%autosetup -p1 -n skanpage-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang skanpage

%files -f skanpage.lang
%{_bindir}/skanpage
%{_datadir}/applications/org.kde.skanpage.desktop
%{_datadir}/icons/hicolor/*/*/skanpage.*
%{_datadir}/metainfo/org.kde.skanpage.appdata.xml
%{_datadir}/qlogging-categories6/skanpage.categories
