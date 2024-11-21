import os

from conan import ConanFile
from conan.tools.files import save, copy


class Pkg1(ConanFile):
    name = "pkg1"
    version = "1.0"

    requires = "pkg2/1.0"

    def source(self):
        save(self, os.path.join(self.recipe_metadata_folder, "logs", "src.log"), f"srclog {self.name}!!!")

    def build(self):
        save(self, "buildlog.txt", f"some logs {self.name}!!!")
        copy(self, "buildlog.txt", src=self.build_folder, dst=os.path.join(self.package_metadata_folder, "logs"))
