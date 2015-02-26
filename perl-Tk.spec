#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires valid $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	Tk
Summary:	Tk - a graphical user interface toolkit for Perl
Summary(pl.UTF-8):	Tk - toolkit graficznego interfejsu użytkownika dla Perla
Name:		perl-Tk
Version:	804.032
Release:	3
# same as perl (except pTk dir - BSD-like)
License:	GPL v1+ or Artistic, parts BSD-like
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SR/SREZIC/%{pnam}-%{version}.tar.gz
# Source0-md5:	47a84c70d1fd254ccece208303e6e9d5
Patch0:		%{name}-misc.patch
Patch1:		%{name}-man_section.patch
Patch2:		%{name}-link.patch
URL:		http://search.cpan.org/dist/Tk/
BuildRequires:	perl-Tie-Watch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXft-devel
Obsoletes:	perl-Tk-JPEG
Obsoletes:	perl-Tk-PNG
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	WidgetDemo

%description
Perl Tk extension aims to provide a complete interface to the latest
production version of John Ousterhout's Tk GUI toolkit, while
providing an Object Oriented interface to Perl code.

%description -l pl.UTF-8
Rozszerzenie Perla Tk ma na celu udostępnienie pełnego interfejsu do
najnowszej produkcyjnej wersji toolkitu graficznego Tk Johna
Ousterhouta, jednocześnie zapewniając zorientowany obiektowo interfejs
dla kodu w Perlu.

%package devel
Summary:	Perl Tk - development files
Summary(pl.UTF-8):	Perl Tk - pliki programistyczne
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description devel
This package gives you the ability to develop Perl applications for
the Tk GUI.

%description devel -l pl.UTF-8
Ten pakiet umożliwia tworzenie aplikacji Perlowych przy użyciu
graficznego interfejsu użytkownika Tk.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# sync with current Xlib
ln -sf /usr/include/X11/Xlib.h pTk/Xlib.h

%{__perl} Makefile.PL \
	XFT=1 \
	INSTALLDIRS=vendor \
	X11LIB=/usr/%{_lib}
%{__sed} -i -e 's/<default.h>/"default.h"/g' pTk/tixDef.h
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_vendorlib}/Tk,%{_examplesdir}/%{name}-%{version}}

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# put demos to examples dir. do they work? don't know. didn't test
mv $RPM_BUILD_ROOT{%{perl_vendorarch}/Tk/demos,%{_examplesdir}/%{name}-%{version}}

# perl-Tie-Watch packaged in system
%{__rm} $RPM_BUILD_ROOT{%{_mandir}/man3/Tie::Watch.3pm,%{perl_vendorarch}/Tie/Watch.pm}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Tk{,/*}.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Tk/.packlist

# in %doc
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Tk/{Credits,README.*,license.terms}

find $RPM_BUILD_ROOT -type f | xargs sed -i -e "s|/usr/local/bin/perl|%{_bindir}/perl|g"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.linux ToDo Funcs.doc
%doc Tk/Credits Tk/license.terms Tk/README.Adjust
%attr(755,root,root) %{_bindir}/gedi
%attr(755,root,root) %{_bindir}/tkjpeg
%dir %{perl_vendorlib}/Tk
%{perl_vendorarch}/Tk.pm
%dir %{perl_vendorarch}/Tk
%{perl_vendorarch}/Tk/DragDrop
%{perl_vendorarch}/Tk/Event
%{perl_vendorarch}/Tk/Menu
%{perl_vendorarch}/Tk/Text
%{perl_vendorarch}/Tk/[A-L]*.pm
%{perl_vendorarch}/Tk/[N-Z]*.pm
%{perl_vendorarch}/Tk/M[a-z]*.pm
%{perl_vendorarch}/Tk/widgets.pm
# most of the bitmaps are used by demos
%{perl_vendorarch}/Tk/*.x[bp]m
%dir %{perl_vendorarch}/auto/Tk
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/Tk.so
%{perl_vendorarch}/auto/Tk/autosplit.ix
%{perl_vendorarch}/auto/Tk/*.al
%dir %{perl_vendorarch}/auto/Tk/[BHLMNPWXp]*
%dir %{perl_vendorarch}/auto/Tk/Canvas
%dir %{perl_vendorarch}/auto/Tk/C[lo]*
%dir %{perl_vendorarch}/auto/Tk/Entry
%dir %{perl_vendorarch}/auto/Tk/Event
%dir %{perl_vendorarch}/auto/Tk/Frame
%dir %{perl_vendorarch}/auto/Tk/IO
%dir %{perl_vendorarch}/auto/Tk/InputO
%dir %{perl_vendorarch}/auto/Tk/Sc*
%dir %{perl_vendorarch}/auto/Tk/T[Laeio]*
%dir %{perl_vendorarch}/auto/Tk/JPEG
%{perl_vendorarch}/auto/Tk/*/autosplit.ix
%{perl_vendorarch}/auto/Tk/*/*.al
%{perl_vendorarch}/auto/Tk/*/*.ld
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/*/*.so
%{_mandir}/man1/tkjpeg.1p*
%{_mandir}/man3/Tk*.3pm*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ptked
%attr(755,root,root) %{_bindir}/ptksh
%attr(755,root,root) %{_bindir}/widget
%{perl_vendorarch}/Tk/MMtry.pm
%{perl_vendorarch}/Tk/MMutil.pm
%{perl_vendorarch}/Tk/prolog.ps
%{perl_vendorarch}/Tk/typemap
%{perl_vendorarch}/Tk/tkGlue*
%{perl_vendorarch}/Tk/vtab.def
%{perl_vendorarch}/Tk/TkXSUB.def
%{perl_vendorarch}/Tk/install.pm
%{perl_vendorarch}/Tk/pTk
%{perl_vendorarch}/Tk/*.gif
%{_mandir}/man1/ptked.1p*
%{_mandir}/man1/ptksh.1p*
%{_mandir}/man1/widget.1p*
%{_examplesdir}/%{name}-%{version}
