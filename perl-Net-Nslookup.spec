%define upstream_name    Net-Nslookup
%define upstream_version 2.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Provide nslookup(1)-like capabilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Nslookup-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Net::Nslookup provides the capabilities of the standard UNIX command line
tool nslookup(1). Net::DNS is a wonderful and full featured module, but
quite often, all you need is `nslookup $host`. This module provides that
functionality.

Net::Nslookup exports a single function, called 'nslookup'. 'nslookup' can
be used to retrieve A, PTR, CNAME, MX, and NS records.

  my $a  = nslookup(host => "use.perl.org", type => "A");

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.190.0-2mdv2011.0
+ Revision: 657803
- rebuild for updated spec-helper

* Sun Oct 03 2010 Shlomi Fish <shlomif@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 582695
- import perl-Net-Nslookup


