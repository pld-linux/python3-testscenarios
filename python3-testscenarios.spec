#
# Conditional build:
%bcond_with	tests	# unit tests (not in sdist)

Summary:	Testscenarios - pyunit extension for dependency injection
Summary(pl.UTF-8):	Testscenarios - rozszerzenie pyunit do wstrzykiwania zależności
Name:		python3-testscenarios
Version:	0.6.2
Release:	1
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/testscenarios/
Source0:	https://files.pythonhosted.org/packages/source/t/testscenarios/testscenarios-%{version}.tar.gz
# Source0-md5:	db0045ff023a3f2742034cdbacc108eb
URL:		https://launchpad.net/testscenarios
BuildRequires:	python3-build
BuildRequires:	python3-hatch-vcs
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
%if %{with tests}
BuildRequires:	python3-testtools >= 2.8.7
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testscenarios provides clean dependency injection for python unittest
style tests. This can be used for interface testing (testing many
implementations via a single test suite) or for classic dependency
injection (provide tests with dependencies externally to the test code
itself, allowing easy testing in different situations).

%description -l pl.UTF-8
Moduł testscenarios zapewnia czyste wstrzykiwanie zależności dla
testów pythonowych w stylu unittest. Może to być używane do testowania
interfejsów (testowania wielu implementacji poprzez prosty zestaw
testów) albo klasycznego wstrzykiwania zależności (dostarczania testów
z zależnościami zewnętrznymi w stosunku do kodu testującego, co
pozwala na łatwiejsze testowanie w różnych sytuacjach).

%prep
%setup -q -n testscenarios-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__make} check \
	PYTHON=%{__python3}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSD COPYING GOALS NEWS README.rst
%{py3_sitescriptdir}/testscenarios
%{py3_sitescriptdir}/testscenarios-%{version}.dist-info
