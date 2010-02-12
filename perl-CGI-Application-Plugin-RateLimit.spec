%define upstream_name    CGI-Application-Plugin-RateLimit
%define upstream_version 1.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Limits runmode call rate per user
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CGI::Application)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides protection against a user calling a runmode too
frequently. A typical use-case might be a contact form that sends email.
You'd like to allow your users to send you messages, but thousands of
messages from a single user would be a problem.

This module works by maintaining a database of hits to protected runmodes.
It then checks this database to determine if a new hit should be allowed
based on past activity by the user. The user's identity is, by default,
tied to login (via REMOTE_USER) or IP address (via REMOTE_IP) if login info
is not available. You may provide your own identity function via the
identity_callback() method.

To use this module you must create a table in your database with the
following schema (using MySQL-syntax, although other DBs may work as well
with minor alterations):

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
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/CGI
