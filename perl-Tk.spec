%include	/usr/lib/rpm/macros.perl
Summary:	Tk perl module
Summary(pl):	Modu³ perla Tk
Name:		perl-Tk
Version:	800.014
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Tk/Tk%{version}.tar.gz
Patch0:		perl-Tk-paths.patch
Patch1:		perl-Tk-misc.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	XFree86-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
Provides:	perl(Tk::LabRadio)
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This package gives you the ability to develop perl applications using
the Tk GUI.

%description -l pl
Ten pakiet daje Ci mo¿liwo¶æ tworzenia aplikacji perla z wykorzystaniem
GUI Tk.

%prep
%setup -q -n Tk%{version}
%patch0 -p1
%patch1 -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tk -name \*.so \
	-exec strip --strip-unneeded {} \;

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Tk
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README README.linux ToDo  Funcs.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,ToDo,README.linux,Funcs.doc}.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitearch}/Tk.pm
%{perl_sitearch}/Tk/*.pm
%{perl_sitearch}/Tk/prolog.ps
%{perl_sitearch}/Tk/*.xbm
%{perl_sitearch}/Tk/*.xpm
%{perl_sitearch}/Tk/*.gif
%{perl_sitearch}/Tk/tkGlue*
%{perl_sitearch}/Tk/typemap
%{perl_sitearch}/Tk/DragDrop
%{perl_sitearch}/Tk/Menu
%{perl_sitearch}/Tk/Text
%{perl_sitearch}/Tk/demos
%{perl_sitearch}/Tk/pTk

%dir %{perl_sitearch}/auto/Tk
%attr(755,root,root) %{perl_sitearch}/auto/Tk/Tk.so
%{perl_sitearch}/auto/Tk/Tk.bs
%{perl_sitearch}/auto/Tk/autosplit.ix
%{perl_sitearch}/auto/Tk/*.al
%{perl_sitearch}/auto/Tk/.packlist
%{perl_sitearch}/auto/Tk/Frame
%{perl_sitearch}/auto/Tk/Clipboard
%{perl_sitearch}/auto/Tk/CmdLine

%dir %{perl_sitearch}/auto/Tk/Bitmap
%dir %{perl_sitearch}/auto/Tk/Canvas
%dir %{perl_sitearch}/auto/Tk/Entry
%dir %{perl_sitearch}/auto/Tk/HList
%dir %{perl_sitearch}/auto/Tk/IO
%dir %{perl_sitearch}/auto/Tk/InputO
%dir %{perl_sitearch}/auto/Tk/Listbox
%dir %{perl_sitearch}/auto/Tk/Menubutton
%dir %{perl_sitearch}/auto/Tk/Mwm
%dir %{perl_sitearch}/auto/Tk/NBFrame
%dir %{perl_sitearch}/auto/Tk/Photo
%dir %{perl_sitearch}/auto/Tk/Pixmap
%dir %{perl_sitearch}/auto/Tk/Scale
%dir %{perl_sitearch}/auto/Tk/Scrollbar
%dir %{perl_sitearch}/auto/Tk/TList
%dir %{perl_sitearch}/auto/Tk/Table
%dir %{perl_sitearch}/auto/Tk/Text
%dir %{perl_sitearch}/auto/Tk/TextUndo
%dir %{perl_sitearch}/auto/Tk/TixGrid
%dir %{perl_sitearch}/auto/Tk/Toplevel
%dir %{perl_sitearch}/auto/Tk/Widget
%dir %{perl_sitearch}/auto/Tk/WinPhoto
%dir %{perl_sitearch}/auto/Tk/Wm
%dir %{perl_sitearch}/auto/Tk/X
%dir %{perl_sitearch}/auto/Tk/Xlib

%{perl_sitearch}/auto/Tk/Listbox/*.al
%{perl_sitearch}/auto/Tk/Listbox/autosplit.ix
%{perl_sitearch}/auto/Tk/Scale/*.al
%{perl_sitearch}/auto/Tk/Scale/autosplit.ix
%{perl_sitearch}/auto/Tk/Scrollbar/*.al
%{perl_sitearch}/auto/Tk/Scrollbar/autosplit.ix
%{perl_sitearch}/auto/Tk/Table/*.al
%{perl_sitearch}/auto/Tk/Table/autosplit.ix
%{perl_sitearch}/auto/Tk/Text/autosplit.ix
%{perl_sitearch}/auto/Tk/TextUndo/*.al
%{perl_sitearch}/auto/Tk/TextUndo/autosplit.ix
%{perl_sitearch}/auto/Tk/Toplevel/*.al
%{perl_sitearch}/auto/Tk/Toplevel/autosplit.ix
%{perl_sitearch}/auto/Tk/Widget/*.al
%{perl_sitearch}/auto/Tk/Widget/autosplit.ix
%{perl_sitearch}/auto/Tk/Wm/*.al
%{perl_sitearch}/auto/Tk/Wm/autosplit.ix
%{perl_sitearch}/auto/Tk/X/autosplit.ix

%{perl_sitearch}/auto/Tk/*/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Tk/*/*.so

%{_mandir}/man[13]/*
