import os
import platform
import textwrap

from test.examples_tools import run, replace

from conan import conan_version

print("- CMakeToolchain: Extending your CMakePresets with Conan generated ones -")

run("conan install .")
run("conan install . -s build_type=Debug")

if platform.system() == "Windows":
    run(f"cmake --preset default")
    run(f"cmake --build --preset release")
    run(f"cmake --build --preset debug")
else:
    run(f"cmake --preset release")
    run(f"cmake --build --preset release")
    run(f"cmake --preset debug")
    run(f"cmake --build --preset debug")

output = run(str(os.path.join("build", "Release", "foo")))
assert "Hello World Release!" in output

output = run(str(os.path.join("build", "Debug", "foo")))
assert "Hello World Debug!" in output
