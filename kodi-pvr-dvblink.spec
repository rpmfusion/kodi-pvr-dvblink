%global commit 339c3ea77f8b1c052ad106419a8f857ac8f53e60
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20170827

%global kodi_addon pvr.dvblink
%global kodi_version 17.0

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
# Use Epoch to manage upgrades from older upstream
# (https://github.com/opdenkamp/xbmc-pvr-addons/)
Epoch:          1
Version:        3.4.8
Release:        3%{?dist}
Summary:        Kodi's DVBLink client addon

Group:          Applications/Multimedia
# Addon is GPLv2+. lib/dvblinkremote is MIT
License:        GPLv2+ and MIT
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        https://github.com/kodi-pvr/%{kodi_addon}/archive/%{short_commit}/%{name}-%{short_commit}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel >= %{kodi_version}
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  platform-devel
Requires:       kodi >= %{kodi_version}
ExclusiveArch:  i686 x86_64

%description
PVR plugin for DVBLink. Supports streaming of Live TV & recordings, EPG, timers.


%prep
%autosetup -n %{kodi_addon}-%{commit}

# Drop bundled tinyxml2 library
rm -r depends/common/tinyxml2/

cp -p %{SOURCE1} .


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}/kodi/ .
%make_build


%install
%make_install


%files
%doc README.md %{kodi_addon}/changelog.txt
%license gpl-2.0.txt
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Apr 10 2018 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1:3.4.8-3
- Rebuild for tinyxml2 update

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
