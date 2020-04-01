# Copy this template to your opencv module folder, then replace "module_name_here"

cmake_minimum_required(VERSION 3.12.0)
set(MODULE_NAME "module_name_here")

project( ${MODULE_NAME} )

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

set(REPO_ROOT "..")

find_package(OpenCV REQUIRED)

# The target
add_executable( ${MODULE_NAME} ${MODULE_NAME}.cpp )
TARGET_LINK_LIBRARIES ( ${MODULE_NAME} ${OpenCV_LIBS}) 