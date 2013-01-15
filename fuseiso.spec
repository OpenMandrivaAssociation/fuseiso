Name:		fuseiso
Version:	20070708
Release:	7
Source0:	http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
Patch0:		fuseiso-automake-1.13.patch
URL:		http://fuse.sourceforge.net/wiki/index.php/FuseIso
License:	GPLv2+
Summary:	FUSE module to mount ISO filesystem images
Group:		File tools
BuildRequires:	fuse-devel >= 2.2, glib2-devel >= 2.2, zlib-devel
Requires:	fuse >= 2.2

%description
FuseIso is a FUSE module to mount ISO filesystem images (.iso files,
.bin files, .nrg files..).

The main advantage of using this is that you don't have to be root.

%prep
%setup -q
%apply_patches

%build
export LDFLAGS="`pkg-config glib-2.0 --libs` -lz"
autoreconf
%configure
%make

%install
%makeinstall

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS ChangeLog README 
%{_bindir}/%{name}

%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20070708-6mdv2011.0
+ Revision: 618375
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20070708-5mdv2010.0
+ Revision: 428973
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20070708-4mdv2009.0
+ Revision: 245513
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 20070708-2mdv2008.1
+ Revision: 170848
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 17 2007 Nicolas Vigier <nvigier@mandriva.com> 20070708-1mdv2008.0
+ Revision: 64896
- update license tag
- new version
- run autoreconf before ./configure

* Wed May 23 2007 Nicolas Vigier <nvigier@mandriva.com> 20061017-1mdv2008.0
+ Revision: 30340
- Import fuseiso

