%define	name	fuseiso
%define version	20070708
%define release	%mkrel 1

Name:		%name
Version:	%version
Release:	%release
Source:		http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
URL:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-root
Summary:	FuseIso is a FUSE module to mount ISO filesystem images
Group:		File tools
BuildRequires:	fuse-devel >= 2.2, glib2-devel >= 2.2, zlib-devel
Requires:	fuse >= 2.2
%description
FuseIso is a FUSE module to mount ISO filesystem images (.iso files,
.bin files, .nrg files..).

The main advantage of using this is that you don't have to be root.

%prep
%setup -q

%build
autoreconf
%configure
%make

%install
%makeinstall

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ChangeLog README 
%{_bindir}/%{name}

