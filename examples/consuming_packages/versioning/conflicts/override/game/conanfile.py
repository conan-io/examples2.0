from conan import ConanFile

class Pkg(ConanFile):
    name = "game"
    version = "1.0"

    def requirements(self):  
        self.requires("engine/1.0")
        self.requires("ai/1.0")
