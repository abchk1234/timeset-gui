Maintainer: aaditya	  aaditya_gnulinux@zoho.com

pkgname=timeset-gui
pkgver=1.1
pkgrel=1
_git=4c91651acc22100977ce4923d52959485627ef01
pkgdesc="A python-gui for managing system date and time."
url="http://forum.manjaro.org/index.php?topic=7067.0
arch=('any')
license=('GPL')
depends=('gksudo' 'python' 'python-gobject' 'pywebkitgtk')
optdepends=('ntp')
source=("http://git.manjaro.org/aadityabagga/timeset-gui/raw/$_git/timeset-gui")
md5sums=('fe90faa43a668f592a3475ef0e7e5021067a8256')
package() {
  cd "${srcdir}"
  install -Dm755 "${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}

# vim:set ts=2 sw=2 et:
