from conan import ConanFile


class App(ConanFile):
    name = "app"
    version = "1.0"

    def requirements(self):
        self.requires("pkg1/1.0")
