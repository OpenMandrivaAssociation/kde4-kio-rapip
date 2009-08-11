%define svn		0
%define rel		1
%if %svn
%define release		%mkrel 0.%svn.%rel
%define distname	%name-%svn.tar.lzma
%define	dirname		synce-gvfs
%else
%define release		%mkrel %rel
%define distname	%name-%version.tar.gz
%define dirname		%name-%version
%endif

Name:		kde4-kio-rapip
Summary:	KDE 4 KIOslave for Windows Mobile devices
Version:	0.2
Release:	%{release}
License:	MIT
Source0:	http://downloads.sourceforge.net/synce/%{distname}
URL:		http://synce.sourceforge.net/
Group:		Communications
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libsynce-devel
BuildRequires:	librapi-devel
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel

%description
This is a full featured KIOslave used to browse through the file
system of a Windows Mobile device, and to copy files to and from the
PDA by drag and drop via Konqueror.

To use, simply open Konqueror, Dolphin, or any other KIO-enabled file
manager and type in rapip://DEVICENAME/ to the address bar. If you are
not sure about the name of your device, simply go to rapip:/ which
will show the first device it finds.

%prep
%setup -q -n %{dirname}

%build
rm -f CMakeCache.txt 
%cmake
%make

%install
rm -rf %{buildroot}
pushd build
%makeinstall_std
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE ChangeLog README
%{_kde_libdir}/kde4/kio_rapip.so
%{_kde_services}/rapip.protocol
%{_kde_services}/synce.protocol
%{_datadir}/mime/packages/synce-kde4-kio-rapip.xml
%{_iconsdir}/hicolor/*/apps/*.png
