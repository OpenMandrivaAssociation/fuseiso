Summary:	FUSE module to mount ISO filesystem images
Name:		fuseiso
Version:	20070708
Release:	18
License:	GPLv2+
Group:		File tools
Url:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
Source0:	http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
Patch0:		fuseiso-automake-1.13.patch

BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(zlib)
Requires:	fuse >= 2.2

%description
FuseIso is a FUSE module to mount ISO filesystem images (.iso files,
.bin files, .nrg files..).

The main advantage of using this is that you don't have to be root.

%prep
%setup -q
%autopatch -p1
autoreconf

%build
export LDFLAGS="`pkg-config glib-2.0 --libs` -lz"
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING NEWS ChangeLog README 
%{_bindir}/%{name}

