%define    packager           Damir Porobic <damir.porobic@gmx.com>
%define  __spec_install_post %{nil}
%define    debug_package     %{nil}
%define  __os_install_post   %{_dbpath}/brp-compress
%define  _topdir             %(pwd)
%define  _tmppath            %{_topdir}/tmp
%define  _rpmtopdir          %{_topdir}
%define  _builddir           %{_rpmtopdir}/BUILD
%define  _rpmdir             %{_rpmtopdir}/RPMS
%define  _sourcedir          %{_rpmtopdir}/SOURCES
%define  _specdir            %{_rpmtopdir}/SPECS
%define  _srcrpmdir          %{_rpmtopdir}/SRPMS
%define  _signature           gpg
%define  _gpg_name            Ksnip


Name:    ksnip
Summary: Screenshot Tool
Version: 1.3.2
Release: 1
Source0: %{name}-%{version}.tar.gz
URL:     https://github.com/DamirPorobic/ksnip
License: GPLV2+
Group:   Application/Utility
BuildRequires: update-desktop-files


%description
Screenshot tool inspired by Windows Snipping Tool and made with Qt for Linux

%prep
%setup

%build
cmake .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%suse_update_desktop_file -r %{name} Utility DesktopUtility

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/bin/%{name}
%{_usr}/share/applications/%{name}.desktop
%{_usr}/share/pixmaps/%{name}.png

%changelog
* Sun Dec 09 2017 Damir Porobic <damir.porobic@gmx.com> 1.3.2-1
-- Fixed: When compositor is disabled, rect are capture shows only black screen. Fix for Qt4 Ksnip version. (#35)

* Sun Mar 31 2017 Damir Porobic <damir.porobic@gmx.com> 1.3.1-1
-- Fixed bug #29 - Ksnip 1.3.0 fails to build - due to missing cmath library.

* Sun Mar 29 2017 Damir Porobic <damir.porobic@gmx.com> 1.3.0-1
-- New: Drawing two shapes, ellipse and rectangle, with and without fill.
-- New: Customizable color and size (thickness) for drawing tools via button on main tool bar.
-- New: Writing text on screenshots, with customizable font, size, color etc.
-- New: Undo/Redo for paint and crop operations.
-- New: Smooth out free hand pen and marker lines (can be disabled in settings).
-- New: Print screenshot or save is to prf/ps.
-- Fixed: Confirming crop via enter or return didn't close crop panel.
-- Fixed: Paint items not correctly positioned after second and subsequent crops.

* Sun Jan 20 2017 Damir Porobic <damir.porobic@gmx.com> 1.2.1-1
-- Fixed: Binary segfaults when compiled in x86_64 with -fPIC in gcc-5.4.0. (#20)
-- Fixed incorrect version number in "About" dialog.

* Sun Jan 16 2017 Damir Porobic <damir.porobic@gmx.com> 1.2.0-1
-- New: Added functionality to upload screenshots to Imgur.com in anonymous or account mode.
-- New: Capture mouse cursor on screenshot (feature can be enabled or disabled in settings).
-- New: In crop window the crop position, width and height can be entered in numeric values, to provide a more precise crop.
-- New: Settings Window Layout was changed and reorganized.
-- Fixed: Paint cursor was visible when capturing new screenshot.
-- Fixed: Crop could leave scene area.

* Sun Oct 23 2016 Damir Porobic <damir.porobic@gmx.com> 1.1.0-1
-- New: Cropping captured image to desired size.
-- New: Command line support, screenshots can be taken now from command line too.
-- New: Moving drawn lines to desired position by dragging.
-- New: Setting default save location, filename and format from settings window.

* Sun Oct 02 2016 Damir Porobic <damir.porobic@gmx.com> 1.0.0-1
-- New: Screenshots from a custom drawn rectangular area.
-- New: Screenshots from the screen where ksnip is currently located (for multi monitor environments).
-- New: Screenshots from the whole screen, including all monitors.
-- New: Screenshot of currently active (on top) window.
-- New: Delayed captures.
-- New: Drawing on the captured screenshot with Pen or Marker with changeable color and size.
-- New: Saving ksnip location and selected tool and loading on startup.
