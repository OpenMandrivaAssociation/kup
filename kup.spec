%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Backup scheduler for KDE Plasma
Name:		kup
Version:	6.8.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Archiving/Backup
URL:		https://invent.kde.org/plasma/kup
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/kup/-/archive/%{gitbranch}/kup-%{gitbranchd}.tar.bz2#/kup-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{plasmaver}/kup-%{version}.tar.xz
%endif
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6IdleTime)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6WindowSystem)
# KDELibs4Support provides an unversioned cmake(Plasma), which satisfies any version.
BuildRequires:	cmake(PlasmaQuick) >= 6.8
BuildRequires:	pkgconfig(libgit2)
Requires:	rsync
Requires:	bup

%description
Kup keeps up-to-date backups of personal files. Plans are configured in
System Settings, and a Plasma applet shows when a backup is due.

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
%license LICENSES/*.txt
%doc MAINTAINER README.md
%{_bindir}/kup-daemon
%{_bindir}/kup-filedigger
%{_bindir}/kup-purger
%{_iconsdir}/hicolor/scalable/apps/kup.svg
%{_datadir}/metainfo/org.kde.kup.appdata.xml
%{_sysconfdir}/xdg/autostart/kup-daemon.desktop
%{_datadir}/applications/kup-daemon.desktop
%{_datadir}/applications/kcm_kup.desktop
%{_datadir}/knotifications6/kupdaemon.notifyrc
%{_datadir}/qlogging-categories6/kup.categories
%{_qtdir}/plugins/kf6/kio/kio_bup.so
%{_qtdir}/plugins/kf6/kfileitemaction/kupfileitemaction.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%{_qtdir}/plugins/plasma/applets/org.kde.kupapplet.so
