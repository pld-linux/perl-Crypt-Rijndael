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
Version:	1.11
Release:	5
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c26594420342f4ccddc535b878962db9
Patch0:		%{name}-types.patch
URL:		http://search.cpan.org/dist/Crypt-Rijndael/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Manifest >= 1.21
BuildRequires:	perl-Test-Simple
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
%{perl_vendorarch}/Crypt/Rijndael.pm
%dir %{perl_vendorarch}/auto/Crypt/Rijndael
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Rijndael/Rijndael.so
%{_mandir}/man3/Crypt::Rijndael.3*
