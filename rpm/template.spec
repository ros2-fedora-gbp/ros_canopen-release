%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-canopen-master
Version:        0.8.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS canopen_master package

License:        LGPLv3
URL:            http://wiki.ros.org/canopen_master
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       ros-noetic-class-loader
Requires:       ros-noetic-socketcan-interface
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-class-loader
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-socketcan-interface
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
CiA(r) CANopen 301 master implementation with support for interprocess master
synchronisation.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu May 07 2020 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.8.3-1
- Autogenerated by Bloom

