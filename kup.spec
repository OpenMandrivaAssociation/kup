%define major 0
%define libgit24kup %mklibname git24kup %{major}

Summary:	A KDE-based frontend for the very excellent backup software
Name:		kup
Version:	0.4.2
Release:	2
License:	GPLv2+
Group:		Archiving/Backup
# Also https://github.com/spersson/Kup
Url:		http://kde-apps.org/content/show.php/Kup+Backup+System?content=147465
Source0:	https://github.com/spersson/Kup/archive/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
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
%doc LICENSE MAINTAINER README.md
%dir %{_kde_appsdir}/kup-daemon/
%{_kde_appsdir}/kup-daemon/*
%{_kde_autostart}/kup-daemon.desktop
%{_kde_bindir}/kup-daemon
%{_kde_bindir}/kup-filedigger
%{_kde_libdir}/kde4/kcm_kup.so
%{_kde_libdir}/kde4/kio_bup.so
%{_kde_libdir}/libkdeinit4_kup-daemon.so
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_services}/bup.protocol
%{_kde_services}/kcm_kup.desktop

#----------------------------------------------------------------------------

%package -n %{libgit24kup}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgit24kup}
Shared library for %{name}.

%files -n %{libgit24kup}
%{_kde_libdir}/libgit24kup.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
chmod 0644 LICENSE

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_libdir}/libgit24kup.so

%find_lang %{name}

