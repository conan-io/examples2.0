import platform
import os

from conan import conan_version

from test.examples_tools import run, chdir, replace


print("- Editable packages (cmake_layout with separate build folders, and an unusual layout) -")


# FIXME: remove once 2.0-beta10 is out
prefix_preset_name = "" if "beta9" in str(conan_version) else "conan-"
editable_add_argument = "say/1.0" if "beta9" in str(conan_version) else "--name=say --version=1.0"
editable_remove_argument = "say/1.0" if "beta9" in str(conan_version) else "--refs=say/1.0"

run(f"conan editable add --output-folder build_say say {editable_add_argument}")

# Set up the conan generators folders
# Use the consumer to generate the ../build_say/*/generators folders
with chdir("hello"):
    if platform.system() == "Windows":
        run("conan install . -s build_type=Release --output-folder ../build_hello")
    else:
        run("conan install . -s build_type=Release --output-folder ../build_hello")

# Build the dependency explicitly (no need for conan-install, that was done by consumer in previous step)
# This step could be skipped if conan install (above) included --build=editable
with chdir("say"):
    if platform.system() == "Windows":
        # This step was done by hello ... run("conan install . -s build_type=Release")
        run(f"cmake --preset {prefix_preset_name}default")
        run(f"cmake --build --preset {prefix_preset_name}release")
    else:
        # This step was done by hello ... run("conan install . -s build_type=Release")
        run(f"cmake --preset {prefix_preset_name}release")
        run(f"cmake --build --preset {prefix_preset_name}release")

# Build the consumer
with chdir("hello"):
    if platform.system() == "Windows":
        run(f"cmake --preset {prefix_preset_name}default")
        run(f"cmake --build --preset {prefix_preset_name}release")
        cmd_out = run("../build_hello/build/Release/hello.exe")
        assert "say/1.0: Hello World Release!" in cmd_out
    else:
        run(f"cmake --preset {prefix_preset_name}release")
        run(f"cmake --build --preset {prefix_preset_name}release")
        cmd_out = run("../build_hello/build/Release/hello")
        assert "say/1.0: Hello World Release!" in cmd_out

# Edit 'say' source code
with chdir("say"):
    replace(os.path.join("thelib/src", "say.cpp"), "Hello World", "Bye World")
    if platform.system() == "Windows":        
        run(f"cmake --build --preset {prefix_preset_name}release")
    else:
        run(f"cmake --build --preset {prefix_preset_name}release")

with chdir("hello"):
    if platform.system() == "Windows":        
        run(f"cmake --build --preset {prefix_preset_name}release")
        cmd_out = run("../build_hello/build/Release/hello.exe")
        assert "say/1.0: Bye World Release!" in cmd_out
    else:
        run(f"cmake --build --preset {prefix_preset_name}release")
        cmd_out = run("../build_hello/build/Release/hello")
        assert "say/1.0: Bye World Release!" in cmd_out

run(f"conan editable remove {editable_remove_argument}")
