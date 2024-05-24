#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.105
%define		qtver		5.15.2

Summary:	Various text handling addons
Name:		ktextaddons
Version:	1.5.4
Release:	1
License:	BSD-3-Clause
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz
# Source0-md5:	0f54cdc35860c7f9d3b6245037bf0b15
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= 5.15.9
BuildRequires:	Qt6Keychain-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6TextToSpeech-devel
BuildRequires:	Qt6UiTools-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.103.0
BuildRequires:	kf6-karchive-devel >= 5.103.0
BuildRequires:	kf6-kauth-devel >= 5.105.0
BuildRequires:	kf6-kcodecs-devel >= 5.105.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.103.0
BuildRequires:	kf6-ki18n-devel >= 5.103.0
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf6-kxmlgui-devel >= 5.103.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Various text handling addons.

%package devel
Summary:	Header files for %{name} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Xml-devel >= %{qtver}
Requires:	cmake >= 3.16

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{name}.

%prep
%setup -q

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6

%ninja_build -C build

%if %{with tests}
cd build
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
%ghost %{_libdir}/libKF6TextAddonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextAddonsWidgets.so.*.*
%ghost %{_libdir}/libKF6TextAutoCorrectionCore.so.1
%attr(755,root,root) %{_libdir}/libKF6TextAutoCorrectionCore.so.*.*
%ghost %{_libdir}/libKF6TextAutoCorrectionWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextAutoCorrectionWidgets.so.*.*
%ghost %{_libdir}/libKF6TextCustomEditor.so.1
%attr(755,root,root) %{_libdir}/libKF6TextCustomEditor.so.*.*
%ghost %{_libdir}/libKF6TextEditTextToSpeech.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEditTextToSpeech.so.*.*
%ghost %{_libdir}/libKF6TextEmoticonsCore.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEmoticonsCore.so.*.*
%ghost %{_libdir}/libKF6TextEmoticonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEmoticonsWidgets.so.*.*
%ghost %{_libdir}/libKF6TextGrammarCheck.so.1
%attr(755,root,root) %{_libdir}/libKF6TextGrammarCheck.so.*.*
%ghost %{_libdir}/libKF6TextTranslator.so.1
%attr(755,root,root) %{_libdir}/libKF6TextTranslator.so.*.*
%ghost %{_libdir}/libKF6TextUtils.so.1
%attr(755,root,root) %{_libdir}/libKF6TextUtils.so.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/textcustomeditor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/texttranslatorwidgets6.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_bing.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_deepl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_google.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_libretranslate.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_lingva.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_yandex.so
%{_datadir}/qlogging-categories6/ktextaddons.categories
%{_datadir}/qlogging-categories6/ktextaddons.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/TextAddonsWidgets
%{_includedir}/KF6/TextAutoCorrectionCore
%{_includedir}/KF6/TextAutoCorrectionWidgets
%{_includedir}/KF6/TextCustomEditor
%{_includedir}/KF6/TextEditTextToSpeech
%{_includedir}/KF6/TextEmoticonsCore
%{_includedir}/KF6/TextEmoticonsWidgets
%{_includedir}/KF6/TextGrammarCheck
%{_includedir}/KF6/TextTranslator
%{_includedir}/KF6/TextUtils
%{_libdir}/cmake/KF6TextAddonsWidgets
%{_libdir}/cmake/KF6TextAutoCorrectionCore
%{_libdir}/cmake/KF6TextAutoCorrectionWidgets
%{_libdir}/cmake/KF6TextCustomEditor
%{_libdir}/cmake/KF6TextEditTextToSpeech
%{_libdir}/cmake/KF6TextEmoticonsCore
%{_libdir}/cmake/KF6TextEmoticonsWidgets
%{_libdir}/cmake/KF6TextGrammarCheck
%{_libdir}/cmake/KF6TextTranslator
%{_libdir}/cmake/KF6TextUtils
%{_libdir}/libKF6TextAddonsWidgets.so
%{_libdir}/libKF6TextAutoCorrectionCore.so
%{_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_libdir}/libKF6TextCustomEditor.so
%{_libdir}/libKF6TextEditTextToSpeech.so
%{_libdir}/libKF6TextEmoticonsCore.so
%{_libdir}/libKF6TextEmoticonsWidgets.so
%{_libdir}/libKF6TextGrammarCheck.so
%{_libdir}/libKF6TextTranslator.so
%{_libdir}/libKF6TextUtils.so
