import platform

from test.examples_tools import run, tmp_dir

# ############# Example ################
print("- Use the Android NDK Recipe from ConanCenter to cross-build a package -")


profile = """
[settings]
arch=armv8
build_type=Release
compiler=clang
compiler.cppstd=17
compiler.libcxx=c++_static
compiler.version=14
os=Android
os.api_level=31

[conf]
tools.cmake.cmaketoolchain:generator=Ninja

[tool_requires]
android-ndk/r25c
ninja/1.11.1
"""

with tmp_dir("tmp"):
    with open("android", "w") as _f:
        _f.write(profile)
    run("conan new -d name=foo -d version=1.0 cmake_lib")
    output = run("conan create . --profile ./android")
    # Since we are cross-building and no not run the binary
    # We can inspect it
    if platform.system() != "Windows":  # This is a *nix command for inspect binaries
        output = run("strings -a test_package/build/clang-14-armv8-17-release/example | head")
        assert "Android" in output
        assert "r25c" in output
