%define upstream_name	 SCUBA-Table-NoDeco
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Calculate no-decompression dive times
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Scuba/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/SCUBA
%{_mandir}/*/*
