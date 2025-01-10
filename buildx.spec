Name     : buildx
Version  : 0.16.1
Release  : 3
URL      : https://github.com/docker/buildx/archive/v0.16.1.tar.gz
Source0  : https://github.com/docker/buildx/archive/v0.16.1.tar.gz
Summary  : a Docker CLI plugin for extended build capabilities with BuildKit.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : glibc-staticdev
Requires : docker

# don't strip, these are not ordinary object files
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

%description
a Docker CLI plugin for extended build capabilities with BuildKit.

%prep
%setup -q -n buildx-%version

%build
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
GO111MODULE="auto"
unset CLEAR_DEBUG_TERSE

go build -mod=vendor -o docker-buildx ./cmd/buildx

%install
rm -rf %{buildroot}
install -Dm755 docker-buildx %{buildroot}/usr/lib/docker/cli-plugins/docker-buildx

%files
%defattr(-,root,root,-)
/usr/lib/docker/cli-plugins/docker-buildx
