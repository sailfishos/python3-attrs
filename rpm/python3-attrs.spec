# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-attrs
Summary:    Classes Without Boilerplate
Version:    19.3.0
Release:    1
License:    MIT or ASL 2.0
URL:        https://pypi.org/project/attrs/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-setuptools

%description
attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods).

Its main goal is to help you to write concise and correct software without slowing down your code.

%prep
%setup -q -n %{name}-%{version}/attrs

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitearch}/attr
%{python3_sitearch}/attrs-*.egg-info
