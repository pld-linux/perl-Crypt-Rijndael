%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Rijndael
Summary:	Crypt::Rijndael Perl module - Rijndael encryption algorithm
Summary(pl):	Modu³ Perla Crypt::Rijndael - algorytm szyfrowania Rijndael
Name:		perl-Crypt-Rijndael
Version:	0.05
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_sitearch}/Crypt/Rijndael.pm
%dir %{perl_sitearch}/auto/Crypt/Rijndael
%{perl_sitearch}/auto/Crypt/Rijndael/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Crypt/Rijndael/*.so
%{_mandir}/man3/*
