cmake_minimum_required(VERSION 3.15)

project(Hello)

find_package(say REQUIRED)

add_executable(hello src/hello.cpp)
target_link_libraries(hello say::say)
