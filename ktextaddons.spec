#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.105
%define		qtver		5.15.2

Summary:	Various text handling addons
Name:		ktextaddons
Version:	1.2.0
Release:	1
License:	BSD-3-Clause
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz
# Source0-md5:	3f59edfc605796fae3c5b814d2a1c00b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel >= 5.15.9
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Speech-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.103.0
BuildRequires:	kf5-karchive-devel >= 5.103.0
BuildRequires:	kf5-kauth-devel >= 5.105.0
BuildRequires:	kf5-kcodecs-devel >= 5.105.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.103.0
BuildRequires:	kf5-ki18n-devel >= 5.103.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf5-kxmlgui-devel >= 5.103.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Various text handling addons.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5DBus-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}
Requires:	cmake >= 3.16

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{name} --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5TextAddonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF5TextAddonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF5TextAutoCorrection.so.1
%attr(755,root,root) %{_libdir}/libKF5TextAutoCorrection.so.*.*.*
%ghost %{_libdir}/libKF5TextEditTextToSpeech.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEditTextToSpeech.so.*.*.*
%ghost %{_libdir}/libKF5TextEmoticonsCore.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEmoticonsCore.so.*.*.*
%ghost %{_libdir}/libKF5TextEmoticonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEmoticonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF5TextGrammarCheck.so.1
%attr(755,root,root) %{_libdir}/libKF5TextGrammarCheck.so.*.*.*
%ghost %{_libdir}/libKF5TextTranslator.so.1
%attr(755,root,root) %{_libdir}/libKF5TextTranslator.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/texttranslatorwidgets5.so
%dir %{_libdir}/qt5/plugins/kf5/translator
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_bing.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_deepl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_google.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_libretranslate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_lingva.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_yandex.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/TextAddonsWidgets
%{_includedir}/KF5/TextAutoCorrection
%{_includedir}/KF5/TextEditTextToSpeech
%{_includedir}/KF5/TextEmoticonsCore
%{_includedir}/KF5/TextEmoticonsWidgets
%{_includedir}/KF5/TextGrammarCheck
%{_includedir}/KF5/TextTranslator
%{_libdir}/cmake/KF5TextAddonsWidgets
%{_libdir}/cmake/KF5TextAutoCorrection
%{_libdir}/cmake/KF5TextEditTextToSpeech
%{_libdir}/cmake/KF5TextEmoticonsCore
%{_libdir}/cmake/KF5TextEmoticonsWidgets
%{_libdir}/cmake/KF5TextGrammarCheck
%{_libdir}/cmake/KF5TextTranslator
%{_libdir}/libKF5TextAddonsWidgets.so
%{_libdir}/libKF5TextAutoCorrection.so
%{_libdir}/libKF5TextEditTextToSpeech.so
%{_libdir}/libKF5TextEmoticonsCore.so
%{_libdir}/libKF5TextEmoticonsWidgets.so
%{_libdir}/libKF5TextGrammarCheck.so
%{_libdir}/libKF5TextTranslator.so
%{_libdir}/qt5/mkspecs/modules/qt_TextAutoCorrection.pri
%{_libdir}/qt5/mkspecs/modules/qt_TextEditTextToSpeech.pri
%{_libdir}/qt5/mkspecs/modules/qt_TextGrammarCheck.pri
%{_libdir}/qt5/mkspecs/modules/qt_TextTranslator.pri
%{_libdir}/qt5/mkspecs/modules/qt_textaddonswidgets.pri
%{_libdir}/qt5/mkspecs/modules/qt_textemoticonscore.pri
%{_libdir}/qt5/mkspecs/modules/qt_textemoticonswidgets.pri
