%define major 0
%define libgit24kup %mklibname git24kup %{major}

Summary:	A KDE-based frontend for the very excellent backup software
Name:		kup
Version:	0.10.0
Release:	2
License:	GPLv2+
Group:		Archiving/Backup
# Also https://github.com/spersson/Kup
Url:		https://invent.kde.org/system/kup
Source0:	https://download.kde.org/stable/kup/%{name}-%{version}.tar.xz
BuildSystem:	cmake
BuildOption:	-DQT_MAJOR_VERSION=6
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(Plasma5Support)
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	pkgconfig(libgit2)
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
%{_bindir}/kup-daemon
%{_bindir}/kup-filedigger
%{_bindir}/kup-purger
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/plasma/plasmoids/org.kde.kupapplet
%{_datadir}/metainfo/org.kde.kupapplet.appdata.xml
%{_datadir}/metainfo/org.kde.kup.appdata.xml
%{_sysconfdir}/xdg/autostart/kup-daemon.desktop
%{_datadir}/applications/kcm_kup.desktop
%{_datadir}/knotifications6/kupdaemon.notifyrc
%{_datadir}/plasma5support/services/kupdaemonservice.operations
%{_datadir}/plasma5support/services/kupservice.operations
%{_datadir}/qlogging-categories6/kup.categories
%{_qtdir}/plugins/kf6/kio/kio_bup.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%{_qtdir}/plugins/plasma5support/dataengine/plasma_engine_kup.so
