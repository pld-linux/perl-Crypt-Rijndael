#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Rijndael
Summary:	Crypt::Rijndael Perl module - Rijndael encryption algorithm
Summary(pl.UTF-8):	Moduł Perla Crypt::Rijndael - algorytm szyfrowania Rijndael
Name:		perl-Crypt-Rijndael
Version:	1.07_02
Release:	1
# included COPYING contains LGPL v2, but README and module source says GPL
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	61b2ebf10194b1f94f14d999cf68f5f9
Patch0:		%{name}-types.patch
URL:		http://search.cpan.org/dist/Crypt-Rijndael/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Manifest) >= 1.14
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is Crypt::CBC compliant Rijndael cipher implementation.
Rijndael has just been selected as the Advanced Encryption Standard.

%description -l pl.UTF-8
Ten moduł jest zgodną z Crypt::CBC implementacją szyfru Rijndael.
Rijndael został niedawno wybrany jako standard zaawansowanego
szyfrowania (AES).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc Changes NEWS README
%{perl_vendorarch}/Crypt/*.pm
%dir %{perl_vendorarch}/auto/Crypt/Rijndael
%{perl_vendorarch}/auto/Crypt/Rijndael/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Rijndael/*.so
%{_mandir}/man3/*
