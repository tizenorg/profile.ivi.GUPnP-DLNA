Name:       gupnp-dlna
Summary:    Utility library for easing DLNA-related tasks
Version:    0.10.2
Release:    0
Group:      Applications/Multimedia
License:    LGPLv2.1
URL:        http://www.gupnp.org
Source0:    http://download.gnome.org/sources/%{name}/0.10/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)


%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and
libsoup. The GUPnP API is intended to be easy to use, efficient and
flexible.

GUPnP DLNA is a small utility library that aims to ease the
DLNA-related tasks such as media profile guessing, transcoding to a
given profile, etc.


%package devel
Summary:    Development files for gupnp-dlna
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Files for development with gupnp-dlna


%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static 
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

rm -rf  $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/gupnp-dlna-info-2.0
%{_bindir}/gupnp-dlna-ls-profiles-2.0
%{_libdir}/libgupnp-dlna-2.0.so.*
%{_libdir}/libgupnp-dlna-gst-2.0.so.*
%{_libdir}/gupnp-dlna/libgstreamer.so
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/aac.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/ac3.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/amr.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/avc.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/common.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/dlna-profiles.rng
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/jpeg.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/lpcm.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mp3.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mpeg-ts.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mpeg1.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mpeg4.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/png.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/wma.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mpeg-common.xml
%{_datadir}/gupnp-dlna-2.0/dlna-profiles/mpeg-ps.xml

%files devel
%defattr(-,root,root,-)
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-audio-information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-container-information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-gst-utils.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-g-values.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-image-information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-profile.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-profile-guesser.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-restriction.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-value-list.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-values.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/gupnp-dlna-video-information.h
%{_includedir}/gupnp-dlna-2.0/libgupnp-dlna/metadata/gupnp-dlna-metadata-extractor.h
%{_libdir}/pkgconfig/gupnp-dlna-2.0.pc
%{_libdir}/pkgconfig/gupnp-dlna-metadata-2.0.pc
%{_libdir}/pkgconfig/gupnp-dlna-gst-2.0.pc
%{_libdir}/libgupnp-dlna-2.0.so
%{_libdir}/libgupnp-dlna-gst-2.0.so
%{_libdir}/gupnp-dlna/libgstreamer.so

