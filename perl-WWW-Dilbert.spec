#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test" (uses network)
#
%define	pdir	WWW
%define	pnam	Dilbert
Summary:	WWW::Dilbert - Retrieve Dilbert of the day comic strip images
Summary(pl.UTF-8):	WWW::Dilbert - pobieranie aktualnej strony komiksu "Dilbert of the day"
Name:		perl-WWW-Dilbert
Version:	1.19
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f1725fde846c27b7a38ca4ea3ed3182
URL:		http://search.cpan.org/dist/WWW-Dilbert/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will download the latest Dilbert of the Day cartoon strip
from the Dilbert website and return a binary blob of the image, or
write it to disk. 

%description -l pl.UTF-8
Ten moduł ściąga ostatnią stronę komiksu "Dilbert of the Day" ze
strony WWW Dilberta i zwraca ją w postaci binarnej lub zapisuje na
dysk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
AUTOMATED_TESTING=1
export AUTOMATED_TESTING
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL TODO
%{perl_vendorlib}/WWW/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
