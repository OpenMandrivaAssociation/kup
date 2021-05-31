%define major 0
%define libgit24kup %mklibname git24kup %{major}

Summary:	A KDE-based frontend for the very excellent backup software
Name:		kup
Version:	0.9.0
Release:	1
License:	GPLv2+
Group:		Archiving/Backup
# Also https://github.com/spersson/Kup
Url:		https://invent.kde.org/system/kup
Source0:	https://download.kde.org/stable/kup/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5)
BuildRequires: pkgconfig(libgit2)
BuildRequires:	pkgconfig(openssl)
Requires:	rsync
Suggests:	bup

%description
Kup is created for helping people to keep up-to-date backups of their personal
files.

Backup types:
 - Synchronized folders with the use of "rsync".
 - Incremental backup archive with the use of "bup"
Backup destinations:
 - local filesystem, monitored for availability. That means you can set
   a destination folder which only exist when perhaps a network shared drive
   is mounted and Kup will detect when it becomes available.
 - external storage, like usb hard drives. Also monitored for availability.
Schedules:
 - manual only (triggered from tray icon popup menu)
 - interval (suggests new backup after some time has passed since last backup)
 - usage based (suggests new backup after you have been active on your computer
   for some hours since last backup).

%files -f %{name}.lang
%doc MAINTAINER README.md
%{_kde5_autostart}/kup-daemon.desktop
%{_kde5_bindir}/kup-daemon
%{_kde5_bindir}/kup-filedigger
%{_kde5_bindir}/kup-purger
%_qt5_plugindir/kcm_kup.so
%_qt5_plugindir/kio_bup.so
%_qt5_plugindir/plasma/dataengine/plasma_engine_kup.so
%{_kde5_libdir}/libkdeinit5_kup-daemon.so
%{_kde5_iconsdir}/hicolor/*/*/*
%{_kde5_services}/bup.protocol
%{_kde5_services}/kcm_kup.desktop
%{_kde5_services}/plasma*.desktop
%{_kde5_datadir}/plasma/plasmoids/org.kde.kupapplet
%{_kde5_datadir}/metainfo/org.kde.kupapplet.appdata.xml
%{_datadir}/metainfo/org.kde.kup.appdata.xml
%{_kde5_datadir}/plasma/services/kupservice.operations
%{_kde5_datadir}/plasma/services/kupdaemonservice.operations
%{_datadir}/knotifications5/kupdaemon.notifyrc
%{_datadir}/qlogging-categories5/kup.categories

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

