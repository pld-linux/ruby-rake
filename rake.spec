%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby program like Make
Summary(pl):	Program typu Make dla j�zyka Ruby
Name:		rake
Version:	0.3.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://rubyforge.org/download.php/226/%{name}-%{version}.tgz
# Source0-md5:	ef26fb54829dad77765a7d0d76f0b27f
Patch0:		%{name}-libdir.patch
URL:		http://rake.rubyforge.org/
BuildRequires:	ruby
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rake is a simple Ruby build program with capabilities similar to make.
It has the following features:
- Rakefiles (rake's version of Makefiles) are completely defined in
  standard Ruby syntax. No XML files to edit. No quirky Makefile
  syntax to worry about (is that a tab or a space?)
- Users can specify tasks with prerequisites.
- Rake supports rule patterns to synthesize implicit tasks.
- Rake is lightweight. It can be distributed with other projects as a
  single file. Projects that depend upon rake do not require that rake
  be installed on target systems.

%description -l pl
Rake to prosty program do budowania w j�zyku Ruby o mo�liwo�ciach
podobnych do make. Ma nast�puj�ce cechy:
- Pliki Rakefile (rake'owa odmiana plik�w Makefile) s� definiowane
  ca�kowicie w standardowej sk�adni j�zyka Ruby. Nie trzeba
  modyfikowa� plik�w XML. Nie trzeba martwi� si� kaprysami sk�adni
  Makefile (czy to tabulacja czy spacja?).
- U�ytkownicy mog� okre�la� zadania z ich zale�no�ciami.
- Rake obs�uguje wzorce regu� do tworzenia z nich wynikowych zada�.
- Rake jest lekki. Mo�e by� rozpowszechniany z innymi projektami jako
  pojedynczy plik. Projekty u�ywaj�ce rake'a nie wymagaj� go
  zainstalowanego na systemach docelowych.

%prep
%setup -q
%patch0 -p1

%install
DESTDIR=$RPM_BUILD_ROOT \
ruby install.rb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rake
%{ruby_rubylibdir}/rake.rb
%{ruby_rubylibdir}/rake