#
# TODO:
# - descriptions and summaries
# - requires/provides/obsoletes
#
%define		snap 20040628
#
Summary:	debrix driver for ATI cards
Summary(pl):	Driver debriksa dla kart ATI
Name:		debrix-driver-ati
Version:	0.1.0
Release:	0.1
Epoch:		0
License:	??
Group:		X11/Xorg
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	ea4b79c0a37565857fa980052e1b8456
Patch0:		%{name}-modules.patch
# not really debrix URL, but there is no other...
URL:		http://xserver.freedesktop.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	debrix-devel
BuildRequires:	libtool
Requires:	debrix
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--enable-dri

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/lib*.so*
%{_mandir}/man3/*
