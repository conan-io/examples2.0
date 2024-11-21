from conan import ConanFile
from conan.tools.cmake import cmake_layout


class PoseEstimationRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("tensorflow-lite/2.12.0")
        self.requires("opencv/4.8.1")

    def layout(self):
        cmake_layout(self)
