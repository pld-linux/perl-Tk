%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	Tk
Summary:	Tk Perl module
Summary(cs):	Modul Tk pro Perl
Summary(da):	Perlmodul Tk
Summary(de):	Tk Perl Modul
Summary(es):	Módulo de Perl Tk
Summary(fr):	Module Perl Tk
Summary(it):	Modulo di Perl Tk
Summary(ja):	Tk Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Tk ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Tk
Summary(pl):	Modu³ Perla Tk
Summary(pt):	Módulo de Perl Tk
Summary(pt_BR):	Módulo Perl Tk
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Tk
Summary(sv):	Tk Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Tk
Summary(zh_CN):	Tk Perl Ä£¿é
Name:		perl-Tk
Version:	800.023
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-nolibpt.patch
Patch3:		%{name}-man_section.patch
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
%setup -q -n %{pnam}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
perl Makefile.PL
perl -i -p -e 's/<default.h>/"default.h"/g' pTk/tixDef.h
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitelib}/Tk

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_sitearch}/{auto/Tk/.packlist,Tk/reindex.pl} \
	$RPM_BUILD_ROOT%{_mandir}/man3/Tie::Watch.3pm \
	$RPM_BUILD_ROOT%{perl_sitearch}/Tk/*.pod \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Tk/{*.ix,*/*.ix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.linux ToDo Funcs.doc
%attr(755,root,root) %{_bindir}/*
%dir %{perl_sitelib}/Tk
%{perl_sitearch}/Tk.pm
%{perl_sitearch}/Tk
%attr( - ,root, root) %{perl_sitearch}/auto/Tk
%{_mandir}/man[13]/*
