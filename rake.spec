%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby program like Make
Name:		rake
Version:	0.3.1
Release:	1
License:	GPL
URL:		http://rake.rubyforge.org/
Group:		Development/Libraries
Source0:	http://rubyforge.org/download.php/226/%{name}-%{version}.tgz
# Source0-md5:	ef26fb54829dad77765a7d0d76f0b27f
Patch0:	%{name}-libdir.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArchitectures:	noarch
BuildRequires:	ruby

%description
Ruby FastCGI Library

%prep
%setup -q
%patch0 -p1

%build

%install
DESTDIR=$RPM_BUILD_ROOT ruby install.rb

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rake
%{ruby_rubylibdir}/rake.rb
%{ruby_rubylibdir}/rake/

%clean
rm -rf $RPM_BUILD_ROOT
