#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Sereal
%define		pnam	Decoder
%include	/usr/lib/rpm/macros.perl
Summary:	Sereal::Decoder - Fast, compact, powerful binary deserialization
Name:		perl-Sereal-Decoder
Version:	3.002
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/Y/YV/YVES/Sereal-Decoder-%{version}.tar.gz
# Source0-md5:	c26033b258dc3ee2e4e485f7293ccb63
URL:		http://search.cpan.org/dist/Sereal-Decoder/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::LongString)
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
found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod, there is
a discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the
output of our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/Sereal/*.pm
%dir %{perl_vendorarch}/Sereal/Decoder
%{perl_vendorarch}/Sereal/Decoder/*.pm
%dir %{perl_vendorarch}/auto/Sereal
%dir %{perl_vendorarch}/auto/Sereal/Decoder
%attr(755,root,root) %{perl_vendorarch}/auto/Sereal/Decoder/*.so
%{_mandir}/man3/*
