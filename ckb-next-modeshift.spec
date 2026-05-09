Name:           ckb-next-modeshift
Version:        0.6.2
Release:        1%{?dist}
Summary:        Open Source driver for Corsair keyboards and mice (with mode shift enhancement)

License:        GPLv2
URL:            https://github.com/storymode-exe/ckb-next
Source0:        https://github.com/storymode-exe/ckb-next/archive/refs/heads/master.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  quazip-qt6-devel
BuildRequires:  libusb1-devel
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  wayland-protocols-devel

Requires:       qt6-qtbase
Requires:       quazip-qt6
Requires:       libusb1
Requires:       systemd-libs
Requires:       zlib

Conflicts:      ckb-next
Provides:       ckb-next

%description
Fork of ckb-next adding hold-to-shift mode switching for Corsair keyboards.

New features in the Special binding tab:
- Trigger on release (instead of press)
- Retain original key function (passthrough)
- Fixed: unchecking mode radio now properly clears the binding

%prep
%autosetup -n ckb-next-master

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
/usr/bin/ckb-next
/usr/bin/ckb-next-daemon
/usr/libexec/ckb-next-animations/
/usr/share/applications/ckb-next.desktop
/usr/share/icons/hicolor/*/apps/ckb-next*
/usr/lib/systemd/system/ckb-next-daemon.service
/etc/xdg/autostart/ckb-next.autostart.desktop

%post
%systemd_post ckb-next-daemon.service

%preun
%systemd_preun ckb-next-daemon.service

%postun
%systemd_postun_with_restart ckb-next-daemon.service

%changelog
* %(date "+%a %b %d %Y") storymode-exe <story.mode@icloud.com> - 0.6.2-1
- Fork of ckb-next 0.6.2 with mode shift enhancements
- Added "Trigger on release" option to Special binding tab
- Added "Retain original key function" (passthrough) option
- Fixed: unchecking mode radio now properly clears binding
