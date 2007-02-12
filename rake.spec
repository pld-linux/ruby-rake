Summary:	Ruby program like Make
Summary(pl.UTF-8):   Program typu Make dla języka Ruby
Name:		rake
Version:	0.7.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://rubyforge.org/download.php/9499/%{name}-%{version}.tgz
# Source0-md5:	045fcdf3425c800a343179bc10d13cd6
Patch0:		%{name}-libdir.patch
URL:		http://rake.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rake is a simple Ruby build program with capabilities similar to make.
It has the following features:
- Rakefiles (rake's version of Makefiles) are completely defined in
  standard Ruby syntax. No XML files to edit. No quirky Makefile syntax
  to worry about (is that a tab or a space?)
- Users can specify tasks with prerequisites.
- Rake supports rule patterns to synthesize implicit tasks.
- Rake is lightweight. It can be distributed with other projects as a
  single file. Projects that depend upon rake do not require that rake
  be installed on target systems.

%description -l pl.UTF-8
Rake to prosty program do budowania w języku Ruby o możliwościach
podobnych do make. Ma następujące cechy:
- Pliki Rakefile (rake'owa odmiana plików Makefile) są definiowane
  całkowicie w standardowej składni języka Ruby. Nie trzeba modyfikować
  plików XML. Nie trzeba martwić się kaprysami składni Makefile (czy to
  tabulacja czy spacja?).
- Użytkownicy mogą określać zadania z ich zależnościami.
- Rake obsługuje wzorce reguł do tworzenia z nich wynikowych zadań.
- Rake jest lekki. Może być rozpowszechniany z innymi projektami jako
  pojedynczy plik. Projekty używające rake'a nie wymagają go
  zainstalowanego na systemach docelowych.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT \
ruby install.rb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/rake
%{ruby_rubylibdir}/rake.rb
%{ruby_rubylibdir}/rake
