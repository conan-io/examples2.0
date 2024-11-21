import os
import shutil
from test.examples_tools import run, tmp_dir

with tmp_dir("metadata_tmp"):
    shutil.copytree("../pkg1", "./pkg1")
    shutil.copytree("../pkg2", "./pkg2")
    shutil.copy("../conanfile.py", "./conanfile.py")
    shutil.copy("../metadata_deploy.py", "./metadata_deploy.py")
    run("conan create pkg1")
    run("conan create pkg2")
    output = run("conan install . --deployer=metadata_deploy")
    # Our requirements should now be in here
    dependency_folders = os.listdir("dependencies_metadata")
    assert "recipes" in dependency_folders
    assert "packages" in dependency_folders

    recipe_folders = os.listdir("dependencies_metadata/recipes")
    assert "pkg1" in recipe_folders
    assert "pkg2" in recipe_folders

    package_folders = os.listdir("dependencies_metadata/packages")
    assert "pkg1" in package_folders
    assert "pkg2" in package_folders
