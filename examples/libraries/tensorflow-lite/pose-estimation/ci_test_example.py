import platform
from test.examples_tools import run

print("Pose estimation example with Tensorflow Lite and OpenCV")

install_cmd = "conan install . -c tools.system.package_manager:mode=install " \
              "-c tools.system.package_manager:sudo=True -s compiler.cppstd=17 --build=missing "

if platform.system() == "Windows":
    install_cmd += "-c tools.cmake.cmaketoolchain:system_version=10.0" # to force CMake pick a newer SDK
#elif platform.system() == "Linux":
    # affected by this: https://github.com/conan-io/conan-center-index/issues/18951
#    install_cmd += "--build=libx26* --build=openjpeg*"
    # install_cmd += "--build=libx26* -c \"libx26*:tools.build:cxxflags=+['-fno-finite-math-only']\" " \
    #                "--build=openjpeg* -c \"openjpeg*:tools.build:cxxflags=+['-fno-finite-math-only']\""

run(install_cmd)

# with presets

if platform.system() == "Windows":
    run("cmake --preset conan-default")
    run("cmake --build --preset conan-release")
    run("build\Release\pose-estimation.exe --no-windows --image=assets/dancing.png")
else:
    run("cmake --preset conan-release")
    run("cmake --build --preset conan-release")
    run("build/Release/pose-estimation --no-windows --image=assets/dancing.png")

if platform.system() == "Windows":
    run("rd /s /q build")
else:
    run("rm -rf build")

run(install_cmd)

# calling CMake directly

if platform.system() == "Windows":
    run("cmake . -G \"Visual Studio 17 2022\" -DCMAKE_TOOLCHAIN_FILE=./build/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW")
    run("cmake --build . --config Release")
    run("Release\pose-estimation.exe --no-windows --image=assets/dancing.png")
else:
    run("cmake . -G \"Unix Makefiles\" -DCMAKE_TOOLCHAIN_FILE=build/Release/generators/conan_toolchain.cmake -DCMAKE_POLICY_DEFAULT_CMP0091=NEW -DCMAKE_BUILD_TYPE=Release")
    run("cmake --build .")
    run("./pose-estimation --no-windows --image=assets/dancing.png")
