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
Version:	800.024
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-misc.patch
Patch2:		%{name}-man_section.patch
BuildRequires:	XFree86-devel
BuildRequires:	perl-Tie-Watch
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
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

%build
%{__perl} Makefile.PL
%{__perl} -pi -e 's/<default.h>/"default.h"/g' pTk/tixDef.h
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitelib}/Tk

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_sitearch}/{auto/Tk/.packlist,Tk/reindex.pl} \
	$RPM_BUILD_ROOT%{_mandir}/man3/Tie::Watch.3pm \
	$RPM_BUILD_ROOT%{perl_sitearch}/Tk/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.linux ToDo Funcs.doc
%attr(755,root,root) %{_bindir}/*
%dir %{perl_sitelib}/Tk
%{perl_sitearch}/Tk.pm
%{perl_sitearch}/Tk
%dir %{perl_sitearch}/auto/Tk
%{perl_sitearch}/auto/Tk/Tk.bs
%attr(755,root,root) %{perl_sitearch}/auto/Tk/Tk.so
%{perl_sitearch}/auto/Tk/autosplit.ix
%{perl_sitearch}/auto/Tk/*.al
%dir %{perl_sitearch}/auto/Tk/[BHLMNPWXp]*
%dir %{perl_sitearch}/auto/Tk/Canvas
%dir %{perl_sitearch}/auto/Tk/C[lo]*
%dir %{perl_sitearch}/auto/Tk/Entry
%dir %{perl_sitearch}/auto/Tk/Event
%dir %{perl_sitearch}/auto/Tk/Frame
%dir %{perl_sitearch}/auto/Tk/IO
%dir %{perl_sitearch}/auto/Tk/InputO
%dir %{perl_sitearch}/auto/Tk/Sc*
%dir %{perl_sitearch}/auto/Tk/T[Laeio]*
%{perl_sitearch}/auto/Tk/*/autosplit.ix
%{perl_sitearch}/auto/Tk/*/*.al
%{perl_sitearch}/auto/Tk/*/*.bs
%{perl_sitearch}/auto/Tk/*/*.ld
%attr(755,root,root) %{perl_sitearch}/auto/Tk/*/*.so
%{_mandir}/man[13]/*
