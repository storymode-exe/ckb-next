# Maintainer: storymode-exe <story.mode@icloud.com>
# Fork of ckb-next with mode shift enhancements
# https://github.com/storymode-exe/ckb-next

pkgname=ckb-next-modeshift
pkgver=0.6.2
pkgrel=1
pkgdesc="Open Source driver for Corsair keyboards and mice (with mode shift enhancement)"
arch=('x86_64')
url="https://github.com/storymode-exe/ckb-next"
license=('GPL2')
depends=(
    'qt6-base'
    'quazip-qt6'
    'libxcb'
    'xcb-util-wm'
    'libusb'
    'systemd-libs'
    'zlib'
)
makedepends=(
    'cmake'
    'git'
    'qt6-tools'
    'wayland-protocols'
)
conflicts=('ckb-next')
provides=('ckb-next')
backup=()
source=("${pkgname}::git+https://github.com/storymode-exe/ckb-next.git")
sha256sums=('SKIP')

build() {
    cmake -B build -S "${pkgname}" \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -Wno-dev
    cmake --build build --parallel
}

package() {
    DESTDIR="${pkgdir}" cmake --install build
}
