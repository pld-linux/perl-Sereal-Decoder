#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Sereal
%define		pnam	Decoder
%include	/usr/lib/rpm/macros.perl
Summary:	Sereal::Decoder - Fast, compact, powerful binary deserialization
Summary(pl.UTF-8):	Sereal::Decoder - szybka, zwarta, potężna deserializacja binarna
Name:		perl-Sereal-Decoder
Version:	4.005
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YV/YVES/Sereal-Decoder-%{version}.tar.gz
# Source0-md5:	68a7a2220cc9d05585100e4eace9da9f
URL:		http://search.cpan.org/dist/Sereal-Decoder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-LongString
BuildRequires:	perl-Test-Warn
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements a deserializer for an efficient,
compact-output, and feature-rich binary protocol called Sereal. Its
sister module Sereal::Encoder implements an encoder for this format.
The two are released separately to allow for independent and safer
upgrading.

The Sereal protocol versions that are compatible with this decoder
implementation are currently protocol versions 1, 2, and 3. As it
stands, it will refuse to attempt to decode future versions of the
protocol, but if necessary there is likely going to be an option to
decode the parts of the input that are compatible with version 3 of
the protocol. The protocol was designed to allow for this.

The protocol specification and many other bits of documentation can be
found in the github repository at <https://github.com/Sereal/Sereal>.

%description -l pl.UTF-8
Ten moduł implementuje deserializer dla wydajnego, mającego zwarte
wyjście i wiele możliwości, binarnego protokołu o nazwie Sereal.
Siostrzany moduł Sereal::Encoder implementuje koder dla tego formatu.
Moduły wydawane są osobno, aby umożliwić niezależne i bezpieczniejsze
aktualizacje.

Ten dekoder jest obecnie zgodny z protokołem Sereal w wersjach 1, 2,
3. Odmówi prób dekodowania późniejszych wersji, ale w razie potrzeby
może być opcja dekodowania części wejścia zgodnej z wersją 3
protokołu.

Specyfikację protokołu i inną dokumentację można znaleźć w
repozytorium github <https://github.com/Sereal/Sereal>.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} -j1 \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorarch}/Sereal
%{perl_vendorarch}/Sereal/Decoder.pm
%{perl_vendorarch}/Sereal/Performance.pm
%dir %{perl_vendorarch}/Sereal/Decoder
%{perl_vendorarch}/Sereal/Decoder/*.pm
%dir %{perl_vendorarch}/auto/Sereal
%dir %{perl_vendorarch}/auto/Sereal/Decoder
%attr(755,root,root) %{perl_vendorarch}/auto/Sereal/Decoder/Decoder.so
%{_mandir}/man3/Sereal::Decoder.3pm*
%{_mandir}/man3/Sereal::Performance.3pm*
