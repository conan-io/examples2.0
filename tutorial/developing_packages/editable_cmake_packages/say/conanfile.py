from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class SayConan(ConanFile):
    name = "say"
    version = "1.0"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "something_custom": [True, False]}
    default_options = {"shared": False, "fPIC": True, "something_custom": False}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def validate(self):
        # ensure the consumer's options affect this dependency
        if not self.options.something_custom:
            raise ConanInvalidConfiguration("The consumer should set something_custom=True")

    def layout(self):
        cmake_layout(self)

        # adjust the includedirs location, for the editing-mode
        self.cpp.source.includedirs = [ os.path.join("thelib","src") ]
        self.cpp.build.libdirs = [ os.path.join("thelib","src",self.cpp.build.libdirs[0]) ]

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["say"]
