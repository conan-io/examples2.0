from conan import ConanFile

class Pkg(ConanFile):
    name = "ai"
    version = "1.0"

    requires = "math/2.0"