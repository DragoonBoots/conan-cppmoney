from conans import ConanFile, tools
from versions import versions


class MoneycppConan(ConanFile):
    name = "moneycpp"
    version = "20200503"
    license = "MIT"
    url = "https://github.com/DragoonBoots/conan-cppmoney"
    description = "A C++ library for handling monetary values"
    no_copy_source = True
    exports = ("versions.py",)

    # No settings/options are necessary, this is header only

    def source(self):
        version = versions[self.version]
        tools.get('https://github.com/mariusbancila/moneycpp/archive/{}.zip'.format(version.commit),
                  sha256=version.sha256)

    def package(self):
        version = versions[self.version]
        self.copy("*.h", src='moneycpp-{}/include'.format(version.commit), dst="include")

    def package_id(self):
        self.info.header_only()
