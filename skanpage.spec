%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: skanpage
Version: 23.08.0
Release: 1
%if 0%{?git:1}
Source0:        https://invent.kde.org/utilities/%{name}/-/archive/master/%{name}-master.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif
Summary: Utility to scan images and multi-page documents
URL: https://github.com/skanpage/skanpage
License: GPL
Group: Utilities
BuildRequires: cmake ninja
Provides: scanner-gui

%description
Utility to scan images and multi-page documents

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/skanpage
%{_datadir}/applications/org.kde.skanpage.desktop
%{_datadir}/icons/hicolor/*/*/skanpage.*
%{_datadir}/metainfo/org.kde.skanpage.appdata.xml
%{_datadir}/qlogging-categories5/skanpage.categories
