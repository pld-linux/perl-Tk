%include	/usr/lib/rpm/macros.perl
Summary:	Tk perl module
Summary(pl):	Modu³ perla Tk
Name:		perl-Tk
Version:	800.023
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tk/Tk%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-nolibpt.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Tie-Watch
BuildRequires:	XFree86-devel
Provides:	perl(Tk::LabRadio)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package gives you the ability to develop perl applications using
the Tk GUI.

%description -l pl
Ten pakiet daje Ci mo¿liwo¶æ tworzenia aplikacji perla z
wykorzystaniem GUI Tk.

%prep
%setup -q -n Tk%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
perl Makefile.PL
perl -i -p -e 's/<default.h>/"default.h"/g' pTk/tixDef.h
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_sitearch}/{auto/Tk/.packlist,Tk/reindex.pl} \
	$RPM_BUILD_ROOT%{_mandir}/man3/Tie::Watch.3pm

gzip -9nf Changes README README.linux ToDo Funcs.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Tk.pm
%{perl_sitearch}/Tk.pod
%{perl_sitearch}/Tk
%attr( - ,root, root) %{perl_sitearch}/auto/Tk
%{_mandir}/man[13]/*
