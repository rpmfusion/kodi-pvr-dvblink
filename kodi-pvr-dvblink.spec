%global commit 72ef8a0e9a939ec770552300c39b791c0093f385
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20180825

%global kodi_addon pvr.dvblink
%global kodi_version 18.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        4.6.2
Release:        1%{?dist}
Summary:        Kodi's DVBLink client addon

# Addon is GPLv2+. lib/dvblinkremote is MIT
License:        GPLv2+ and MIT
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{shortcommit}/%{kodi_addon}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64 aarch64

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{commit}

# Drop bundled tinyxml2 library
rm -r depends/common/tinyxml2/


%build
%cmake .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Sat Sep 01 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.6.2-1
- Update to 4.6.2
- Enable aarch64 build

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1:4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.5.2-1
- Update to 4.5.2

* Mon Apr 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:4.4.4-2
- Rebuilt for tinyxml2

* Fri Mar 16 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:4.4.4-1
- Update to latest stable release for Kodi 18

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1:3.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 03 2017 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.8-1
- Update to 3.4.8

* Thu Apr 27 2017 Mohamed El Morabity <melmorabity@fedorapeople.org> - 1:3.4.4-1
- Update to 3.4.4

* Sun Jul 24 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:2.1.10-1
- Update to latest stable release for Kodi 16

* Mon Aug 24 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:1.10.9-1
- Initial RPM release
