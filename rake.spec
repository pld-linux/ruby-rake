Summary:	Ruby program like Make
Summary(pl):	Program typu Make dla jêzyka Ruby
Name:		rake
Version:	0.6.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://rubyforge.org/download.php/6357/%{name}-%{version}.tgz
# Source0-md5:	9813cf922ef8fc08b96f880faf883e5e
Patch0:		%{name}-libdir.patch
URL:		http://rake.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
#BuildRequires:	ruby-modules
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

%description -l pl
Rake to prosty program do budowania w jêzyku Ruby o mo¿liwo¶ciach
podobnych do make. Ma nastêpuj±ce cechy:
- Pliki Rakefile (rake'owa odmiana plików Makefile) s± definiowane
  ca³kowicie w standardowej sk³adni jêzyka Ruby. Nie trzeba modyfikowaæ
  plików XML. Nie trzeba martwiæ siê kaprysami sk³adni Makefile (czy to
  tabulacja czy spacja?).
- U¿ytkownicy mog± okre¶laæ zadania z ich zale¿no¶ciami.
- Rake obs³uguje wzorce regu³ do tworzenia z nich wynikowych zadañ.
- Rake jest lekki. Mo¿e byæ rozpowszechniany z innymi projektami jako
  pojedynczy plik. Projekty u¿ywaj±ce rake'a nie wymagaj± go
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
