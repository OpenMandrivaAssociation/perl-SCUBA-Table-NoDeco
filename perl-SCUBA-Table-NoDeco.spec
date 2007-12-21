%define module	SCUBA-Table-NoDeco
%define name	perl-%{module}
%define version	0.03
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Calculate no-decompression dive times
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Scuba/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides the ability to perform useful calculations using
dive-tables, including calculating dive groups and maximum no-decompression
times for repetitive dives. A selection of tables are available. The module
assumes that the diver is using air as their breathing gas.

%prep
%setup -n %{module}-%{version}
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

