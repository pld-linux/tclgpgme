Summary:	Tcl interface to the GnuPG Made Easy library
Summary(pl):	Interfejs Tcl do biblioteki GnuPG Made Easy
Name:		tclgpgme
Version:	1.0
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://beepcore-tcl.sourceforge.net/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-automake.patch
BuildRequires:	tcl-devel
BuildRequires:	gpgme-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tcl GPGME provides a Tcl interface to the GnuPG Made Easy library.

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

%{__make} install DESTDIR="$RPM_BUILD_ROOT"
rm -f $RPM_BUILD_ROOT%{_includedir}/*


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/*.html
%{_libdir}/*
