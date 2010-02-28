%define pkgname rake
Summary:	Rake is a Make-like program implemented in Ruby
Name:		ruby-%{pkgname}
Version:	0.8.7
Release:	0.1
License:	MIT/X Consortium License
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	d9eb83525310ad1a0e8a3eeddfe3c65f
Group:		Development/Languages
URL:		http://rubyforge.org/projects/rake/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Rake is a Make-like program implemented in Ruby. Tasks and
dependencies are specified in standard Ruby syntax.

%package rdoc
Summary:	Documentation files for rake
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for rake.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

%{__sed} -i -e 's|/usr/bin/env ruby|%{__ruby}|' bin/rake

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/rake
%{ruby_rubylibdir}/rake.rb
%{ruby_rubylibdir}/rake

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Rake*
