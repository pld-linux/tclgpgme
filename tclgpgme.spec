Summary:	Tcl interface to the GnuPG Made Easy library
Summary(pl):	Interfejs Tcl do biblioteki GnuPG Made Easy
Name:		tclgpgme
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://beepcore-tcl.sourceforge.net/%{name}-%{version}.tgz
# Source0-md5:	a718a6ee2ac65e79437c5d09a7382ce8
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gpgme-devel >= 1:0.3.11
BuildRequires:	gpgme-devel < 1:0.4.0
BuildRequires:	libtool
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl GPGME provides a Tcl interface to the GnuPG Made Easy library.

%description -l pl
Tcl GPGME udostêpnia interfejs Tcl do biblioteki GnuPG Made Easy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I config
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/*.html
%{_libdir}/gpgme*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*
