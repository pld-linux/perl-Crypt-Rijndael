#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Rijndael
Summary:	Crypt::Rijndael Perl module - Rijndael encryption algorithm
Summary(pl):	Modu³ Perla Crypt::Rijndael - algorytm szyfrowania Rijndael
Name:		perl-Crypt-Rijndael
Version:	0.05
Release:	4
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af8628fee8648f26c94916ef8edf32d9
Patch0:		%{name}-types.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is Crypt::CBC compliant Rijndael cipher implementation.
Rijndael has just been selected as the Advanced Encryption Standard.

%description -l pl
Ten modu³ jest zgodn± z Crypt::CBC implementacj± szyfru Rijndael.
Rijndael zosta³ niedawno wybrany jako standard zaawansowanego
szyfrowania (AES).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/Crypt/Rijndael.pm
%dir %{perl_vendorarch}/auto/Crypt/Rijndael
%{perl_vendorarch}/auto/Crypt/Rijndael/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Rijndael/*.so
%{_mandir}/man3/*
