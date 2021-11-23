Name:       python3-attrs
Summary:    Classes Without Boilerplate
Version:    19.3.0
Release:    1
License:    MIT
URL:        https://pypi.org/project/attrs/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods).

Its main goal is to help you to write concise and correct software without slowing down your code.

%prep
%setup -q -n %{name}-%{version}/attrs

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%license LICENSE
%{python3_sitelib}/attr
%{python3_sitelib}/attrs-*.egg-info
