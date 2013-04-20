#
# Conditional build:
%bcond_without	doc		# build without ri/rdoc
%bcond_without	tests	# build without tests

%define pkgname rake
Summary:	Rake is a Make-like program implemented in Ruby
Name:		ruby-%{pkgname}
Version:	10.0.4
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	510fad70ab126fad98aa3707eed7c417
URL:		http://rubyforge.org/projects/rake/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-minitest
%endif
Requires:	ruby-rubygems
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rake is a Make-like program implemented in Ruby. Tasks and
dependencies are specified in standard Ruby syntax.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
%if %{with tests}
ruby -Ilib ./bin/rake test
%endif

%if %{with doc}
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
rm -rf ri/{Object,CompositePublisher,FileUtils,Module,Ssh*,String,Sys,Test,Time}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir}/tasks,%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.rdoc TODO
%attr(755,root,root) %{_bindir}/rake
%dir %{ruby_rubylibdir}/tasks
%{ruby_rubylibdir}/rake.rb
%{ruby_rubylibdir}/rake

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Rake*
