Summary:	KDE 4 KIOslave for Windows Mobile devices
Name:		kde4-kio-rapip
Version:	0.2
Release:	4
License:	MIT
Group:		Graphical desktop/KDE
Url:		https://synce.sourceforge.net/
Source0:	http://downloads.sourceforge.net/synce/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(librapi2)
BuildRequires:	pkgconfig(libsynce)

%description
This is a full featured KIOslave used to browse through the file
system of a Windows Mobile device, and to copy files to and from the
PDA by drag and drop via Konqueror.

To use, simply open Konqueror, Dolphin, or any other KIO-enabled file
manager and type in rapip://DEVICENAME/ to the address bar. If you are
not sure about the name of your device, simply go to rapip:/ which
will show the first device it finds.

%prep
%setup -q

%build
rm -f CMakeCache.txt
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS LICENSE ChangeLog README
%{_kde_libdir}/kde4/kio_rapip.so
%{_kde_services}/rapip.protocol
%{_kde_services}/synce.protocol
%{_datadir}/mime/packages/synce-kde4-kio-rapip.xml
%{_iconsdir}/hicolor/*/apps/*.png
