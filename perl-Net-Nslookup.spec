%define upstream_name    Net-Nslookup
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provide nslookup(1)-like capabilities
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Net::DNS)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


