#
# Conditional build:
%bcond_without	kf5		# Qt5/KF5 packages
%bcond_without	kf6		# Qt6/KF6 packages
%bcond_with	tests		# test suite

%define		kdeframever	5.105
%define		qt5_ver		5.15.2
%define		kf5_ver		5.105.0
%define		qt6_ver		6.5.0
%define		kf6_ver		5.240.0

Summary:	Various text handling addons
Summary(pl.UTF-8):	Różne dodatki do obsługi tekstu
Name:		ktextaddons
Version:	1.5.4
Release:	2
License:	BSD
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz
# Source0-md5:	0f54cdc35860c7f9d3b6245037bf0b15
URL:		https://kde.org/
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= 5.105.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with kf5}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5Network-devel >= %{qt5_ver}
BuildRequires:	Qt5Speech-devel >= %{qt5_ver}
%if %{with tests}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
%endif
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	kf5-karchive-devel >= %{kf5_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf5_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf5_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:	kf5-kio-devel >= %{kf5_ver}
BuildRequires:	kf5-sonnet-devel >= %{kf5_ver}
BuildRequires:	kf5-syntax-highlighting-devel >= %{kf5_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf5_ver}
%endif
%if %{with kf6}
BuildRequires:	Qt6Core-devel >= %{qt6_ver}
BuildRequires:	Qt6Gui-devel >= %{qt6_ver}
BuildRequires:	Qt6Keychain-devel
BuildRequires:	Qt6Network-devel >= %{qt6_ver}
%if %{with tests}
BuildRequires:	Qt6Test-devel >= %{qt6_ver}
%endif
BuildRequires:	Qt6TextToSpeech-devel >= %{qt6_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt6_ver}
BuildRequires:	kf6-karchive-devel >= %{kf6_ver}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kf6_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf6_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf6_ver}
BuildRequires:	kf6-kio-devel >= %{kf6_ver}
BuildRequires:	kf6-sonnet-devel >= %{kf6_ver}
BuildRequires:	kf6-syntax-highlighting-devel >= %{kf6_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf6_ver}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various text handling addons.

%description -l pl.UTF-8
Różne dodatki do obsługi tekstu.

%package -n kf5-ktextaddons
Summary:	Various text handling addons for KF5
Summary(pl.UTF-8):	Różne dodatki do obsługi tekstu dla KF5
Group:		X11/Libraries
Requires:	Qt5Core >= %{qt5_ver}
Requires:	Qt5Gui >= %{qt5_ver}
Requires:	Qt5Network >= %{qt5_ver}
Requires:	Qt5Speech >= %{qt5_ver}
Requires:	Qt5Widgets >= %{qt5_ver}
Requires:	kf5-dirs
Requires:	kf5-karchive >= %{kf5_ver}
Requires:	kf5-kconfigwidgets >= %{kf5_ver}
Requires:	kf5-kcoreaddons >= %{kf5_ver}
Requires:	kf5-ki18n >= %{kf5_ver}
Requires:	kf5-kio >= %{kf5_ver}
Requires:	kf5-sonnet >= %{kf5_ver}
Requires:	kf5-syntax-highlighting >= %{kf5_ver}
Requires:	kf5-kwidgetsaddons >= %{kf5_ver}
Obsoletes:	ktextaddons < 1.5.3

%description -n kf5-ktextaddons
Various text handling addons for KF5.

%description -n kf5-ktextaddons -l pl.UTF-8
Różne dodatki do obsługi tekstu dla KF5.

%package -n kf5-ktextaddons-devel
Summary:	Header files for KF5 ktextaddons development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających KF5 ktextaddons
Group:		X11/Development/Libraries
Requires:	Qt5Core-devel >= %{qt5_ver}
Requires:	Qt5Widgets-devel >= %{qt5_ver}
Requires:	kf5-ktextaddons = %{version}-%{release}
Requires:	kf5-kconfigwidgets-devel >= %{kf5_ver}
Obsoletes:	ktextaddons-devel < 1.5.3

%description -n kf5-ktextaddons-devel
Header files for KF5 ktextaddons development.

%description -n kf5-ktextaddons-devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających KF5 ktextaddons.

%package -n kf6-ktextaddons
Summary:	Various text handling addons for KF6
Summary(pl.UTF-8):	Różne dodatki do obsługi tekstu dla KF6
Group:		X11/Libraries
Requires:	Qt6Core >= %{qt6_ver}
Requires:	Qt6Gui >= %{qt6_ver}
Requires:	Qt6Network >= %{qt6_ver}
Requires:	Qt6Speech >= %{qt6_ver}
Requires:	Qt6Widgets >= %{qt6_ver}
Requires:	kf6-dirs
Requires:	kf6-karchive >= %{kf6_ver}
Requires:	kf6-kconfigwidgets >= %{kf6_ver}
Requires:	kf6-kcoreaddons >= %{kf6_ver}
Requires:	kf6-ki18n >= %{kf6_ver}
Requires:	kf6-kio >= %{kf6_ver}
Requires:	kf6-sonnet >= %{kf6_ver}
Requires:	kf6-syntax-highlighting >= %{kf6_ver}
Requires:	kf6-kwidgetsaddons >= %{kf6_ver}
Obsoletes:	ktextaddons < 1.5.4-2

%description -n kf6-ktextaddons
Various text handling addons for KF6.

%description -n kf6-ktextaddons -l pl.UTF-8
Różne dodatki do obsługi tekstu dla KF6.

%package -n kf6-ktextaddons-devel
Summary:	Header files for KF6 ktextaddons development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających KF6 ktextaddons
Group:		X11/Development/Libraries
Requires:	Qt6Core-devel >= %{qt6_ver}
Requires:	Qt6Widgets-devel >= %{qt6_ver}
Requires:	kf6-ktextaddons = %{version}-%{release}
Requires:	kf6-kconfigwidgets-devel >= %{kf6_ver}
Obsoletes:	ktextaddons-devel < 1.5.4-2

%description -n kf6-ktextaddons-devel
Header files for KF6 ktextaddons development.

%description -n kf6-ktextaddons-devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających KF6 ktextaddons.

%prep
%setup -q

%build
%if %{with kf5}
%cmake -B build-kf5 \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=5

%ninja_build -C build-kf5

%if %{with tests}
ctest --test-dir build-kf5
%endif
%endif

%if %{with kf6}
%cmake -B build-kf6 \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6

%ninja_build -C build-kf6

%if %{with tests}
ctest --test-dir build-kf6
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with kf5}
%ninja_install -C build-kf5
%endif

%if %{with kf6}
%ninja_install -C build-kf6
%endif

# multiple domains; common for kf5 and kf6
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kf5-ktextaddons -p /sbin/ldconfig
%postun	-n kf5-ktextaddons -p /sbin/ldconfig

%post	-n kf6-ktextaddons -p /sbin/ldconfig
%postun	-n kf6-ktextaddons -p /sbin/ldconfig

%if %{with kf5}
%files -n kf5-ktextaddons -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKF5TextAddonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF5TextAddonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF5TextAutoCorrectionCore.so.*.*.*
%ghost %{_libdir}/libKF5TextAutoCorrectionCore.so.1
%attr(755,root,root) %{_libdir}/libKF5TextAutoCorrectionWidgets.so.*.*.*
%ghost %{_libdir}/libKF5TextAutoCorrectionWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF5TextCustomEditor.so.*.*.*
%ghost %{_libdir}/libKF5TextCustomEditor.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEditTextToSpeech.so.*.*.*
%ghost %{_libdir}/libKF5TextEditTextToSpeech.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEmoticonsCore.so.*.*.*
%ghost %{_libdir}/libKF5TextEmoticonsCore.so.1
%attr(755,root,root) %{_libdir}/libKF5TextEmoticonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF5TextEmoticonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF5TextGrammarCheck.so.*.*.*
%ghost %{_libdir}/libKF5TextGrammarCheck.so.1
%attr(755,root,root) %{_libdir}/libKF5TextTranslator.so.*.*.*
%ghost %{_libdir}/libKF5TextTranslator.so.1
%attr(755,root,root) %{_libdir}/libKF5TextUtils.so.*.*.*
%ghost %{_libdir}/libKF5TextUtils.so.1
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/textcustomeditor.so
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/texttranslatorwidgets5.so
%dir %{_libdir}/qt5/plugins/kf5/translator
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_bing.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_deepl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_google.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_libretranslate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_lingva.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/translator/translator_yandex.so
%{_datadir}/qlogging-categories5/ktextaddons.categories
%{_datadir}/qlogging-categories5/ktextaddons.renamecategories

%files -n kf5-ktextaddons-devel
%defattr(644,root,root,755)
%{_libdir}/libKF5TextAddonsWidgets.so
%{_libdir}/libKF5TextAutoCorrectionCore.so
%{_libdir}/libKF5TextAutoCorrectionWidgets.so
%{_libdir}/libKF5TextCustomEditor.so
%{_libdir}/libKF5TextEditTextToSpeech.so
%{_libdir}/libKF5TextEmoticonsCore.so
%{_libdir}/libKF5TextEmoticonsWidgets.so
%{_libdir}/libKF5TextGrammarCheck.so
%{_libdir}/libKF5TextTranslator.so
%{_libdir}/libKF5TextUtils.so
%{_includedir}/KF5/TextAddonsWidgets
%{_includedir}/KF5/TextAutoCorrectionCore
%{_includedir}/KF5/TextAutoCorrectionWidgets
%{_includedir}/KF5/TextCustomEditor
%{_includedir}/KF5/TextEditTextToSpeech
%{_includedir}/KF5/TextEmoticonsCore
%{_includedir}/KF5/TextEmoticonsWidgets
%{_includedir}/KF5/TextGrammarCheck
%{_includedir}/KF5/TextTranslator
%{_includedir}/KF5/TextUtils
%{_libdir}/cmake/KF5TextAddonsWidgets
%{_libdir}/cmake/KF5TextAutoCorrectionCore
%{_libdir}/cmake/KF5TextAutoCorrectionWidgets
%{_libdir}/cmake/KF5TextCustomEditor
%{_libdir}/cmake/KF5TextEditTextToSpeech
%{_libdir}/cmake/KF5TextEmoticonsCore
%{_libdir}/cmake/KF5TextEmoticonsWidgets
%{_libdir}/cmake/KF5TextGrammarCheck
%{_libdir}/cmake/KF5TextTranslator
%{_libdir}/cmake/KF5TextUtils
%endif

%if %{with kf6}
%files -n kf6-ktextaddons -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKF6TextAddonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF6TextAddonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextAutoCorrectionCore.so.*.*.*
%ghost %{_libdir}/libKF6TextAutoCorrectionCore.so.1
%attr(755,root,root) %{_libdir}/libKF6TextAutoCorrectionWidgets.so.*.*.*
%ghost %{_libdir}/libKF6TextAutoCorrectionWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextCustomEditor.so.*.*.*
%ghost %{_libdir}/libKF6TextCustomEditor.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEditTextToSpeech.so.*.*.*
%ghost %{_libdir}/libKF6TextEditTextToSpeech.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEmoticonsCore.so.*.*.*
%ghost %{_libdir}/libKF6TextEmoticonsCore.so.1
%attr(755,root,root) %{_libdir}/libKF6TextEmoticonsWidgets.so.*.*.*
%ghost %{_libdir}/libKF6TextEmoticonsWidgets.so.1
%attr(755,root,root) %{_libdir}/libKF6TextGrammarCheck.so.*.*.*
%ghost %{_libdir}/libKF6TextGrammarCheck.so.1
%attr(755,root,root) %{_libdir}/libKF6TextTranslator.so.*.*.*
%ghost %{_libdir}/libKF6TextTranslator.so.1
%attr(755,root,root) %{_libdir}/libKF6TextUtils.so.*.*.*
%ghost %{_libdir}/libKF6TextUtils.so.1
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/textcustomeditor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/texttranslatorwidgets6.so
%dir %{_libdir}/qt6/plugins/kf6/translator
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_bing.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_deepl.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_google.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_libretranslate.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_lingva.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/translator/translator_yandex.so
%{_datadir}/qlogging-categories6/ktextaddons.categories
%{_datadir}/qlogging-categories6/ktextaddons.renamecategories

%files -n kf6-ktextaddons-devel
%defattr(644,root,root,755)
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
%endif
