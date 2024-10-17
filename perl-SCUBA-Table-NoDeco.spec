%define upstream_name	 SCUBA-Table-NoDeco
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Calculate no-decompression dive times
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Scuba/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides the ability to perform useful calculations using
dive-tables, including calculating dive groups and maximum no-decompression
times for repetitive dives. A selection of tables are available. The module
assumes that the diver is using air as their breathing gas.

%prep
%setup -n %{upstream_name}-%{upstream_version}
# fix perms
chmod 644 README Changes lib/SCUBA/Table/NoDeco.pm
# fix encoding
perl -pi -e 's/\015$//' README Changes lib/SCUBA/Table/NoDeco.pm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files 
%doc Changes README
%{perl_vendorlib}/SCUBA
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404378
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-7mdv2009.0
+ Revision: 258354
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.03-6mdv2009.0
+ Revision: 246412
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.03-4mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-4mdv2008.0
+ Revision: 47030
- rebuild


* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-3mdv2007.0
- spec cleanup
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdk 
- better url
- drop useless empty directories
- spec cleanup
- make test in %%check

* Sun Dec 19 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3-1mdk 
- first mdk release

