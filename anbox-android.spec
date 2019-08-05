Summary: Android image for use with the Anbox VM
License: Mostly Apache 2.0
Name: anbox-android
Version: 7.1.1
Release: 1
# Unfortunately, abf file-store can't deal with gigantic files such
# as a tarball containing the entire AOSP source tree.
# So we've split the sources:
# mkdir anbox
# cd anbox
# repo init -u https://github.com/anbox/platform_manifests.git -b anbox
# repo sync
# for i in *; do [ -d $i ] && tar cJf /tmp/anbox-android-$i.tar.xz $i; done
# cd ..
# tar cJf /tmp/anbox-android.tar.xz anbox/Android.bp anbox/bootstrap.bash anbox/Makefile
# (We intentionally exclude .repo -- not needed for building, and
# HUGE).
Source0: anbox-android.tar.xz
Source1: anbox-android-abi.tar.xz
Source2: anbox-android-art.tar.xz
Source3: anbox-android-bionic.tar.xz
Source4: anbox-android-bootable.tar.xz
Source5: anbox-android-build.tar.xz
Source6: anbox-android-cts.tar.xz
Source7: anbox-android-dalvik.tar.xz
Source8: anbox-android-developers.tar.xz
Source9: anbox-android-development.tar.xz
Source10: anbox-android-device.tar.xz
Source11: anbox-android-docs.tar.xz
Source12: anbox-android-external.tar.xz
Source13: anbox-android-frameworks.tar.xz
Source14: anbox-android-hardware.tar.xz
Source15: anbox-android-libcore.tar.xz
Source16: anbox-android-libnativehelper.tar.xz
Source17: anbox-android-ndk.tar.xz
Source18: anbox-android-packages.tar.xz
Source19: anbox-android-pdk.tar.xz
Source20: anbox-android-platform_testing.tar.xz
Source21: anbox-android-prebuilts.tar.xz
Source22: anbox-android-sdk.tar.xz
Source23: anbox-android-system.tar.xz
Source24: anbox-android-toolchain.tar.xz
Source25: anbox-android-tools.tar.xz
Source26: anbox-android-vendor.tar.xz

Group: Emulators

BuildRequires: bison flex make ninja
# Unfortunately won't work with newer JDKs...
BuildRequires: java-1.8.0-openjdk-devel
# Stupid, stupid prebuilt binaries...
BuildRequires: %mklibname ncurses 6
BuildRequires: %mklibname tinfo 6
BuildRequires: python2

%description
Android image for use with the Anbox VM

%prep
%setup -n anbox -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26
%autopatch -p1

%build
ln -s %{_bindir}/python2 python
export JAVA_HOME=%{_prefix}/lib/jvm/java-1.8.0
export PATH=$JAVA_HOME/bin:`pwd`:$PATH

. build/envsetup.sh
%ifarch %{x86_64}
lunch anbox_x86_64-userdebug
%else
%ifarch %{arm}
lunch anbox_armv7a_neon-userdebug
%else
%ifarch %{aarch64}
lunch anbox_arm64-userdebug
%else
echo "This package hasn't been ported to %{_arch} yet."
exit 1
%endif
%endif
%endif
%make_build droidcore

%install
# TBD

%files
# TBD
