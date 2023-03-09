cmake_minimum_required(VERSION 3.21)
project(Interface_Engine CXX)

set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE src "lib/ui/*.cpp" "lib/modules/appendix/*.cpp")

add_library(${PROJECT_NAME} ${src})

find_package(boost CONFIG nREQUIRED)
find_package(yaml-cpp CONFIG REQUIRED)

target_link_libraries(${PROJECT_NAME} PUBLIC sfml-graphics sfml-system yaml-cpp localisation)

add_executable(${PROJECT_NAME}_ex main.cpp)

target_link_libraries(${PROJECT_NAME}_ex PRIVATE ${PROJECT_NAME})

file(GLOB_RECURSE srcUnitTest "test/*.cpp")

include_directories(lib)

add_executable(unit_tests ${srcUnitTest})

target_link_libraries(unit_tests PUBLIC gtest gtest_main ${PROJECT_NAME})
