# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/arun/abhiyaan/Section_A/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/arun/abhiyaan/Section_A/build

# Utility rule file for welcome_gennodejs.

# Include the progress variables for this target.
include welcome/CMakeFiles/welcome_gennodejs.dir/progress.make

welcome_gennodejs: welcome/CMakeFiles/welcome_gennodejs.dir/build.make

.PHONY : welcome_gennodejs

# Rule to build all files generated by this target.
welcome/CMakeFiles/welcome_gennodejs.dir/build: welcome_gennodejs

.PHONY : welcome/CMakeFiles/welcome_gennodejs.dir/build

welcome/CMakeFiles/welcome_gennodejs.dir/clean:
	cd /home/arun/abhiyaan/Section_A/build/welcome && $(CMAKE_COMMAND) -P CMakeFiles/welcome_gennodejs.dir/cmake_clean.cmake
.PHONY : welcome/CMakeFiles/welcome_gennodejs.dir/clean

welcome/CMakeFiles/welcome_gennodejs.dir/depend:
	cd /home/arun/abhiyaan/Section_A/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/arun/abhiyaan/Section_A/src /home/arun/abhiyaan/Section_A/src/welcome /home/arun/abhiyaan/Section_A/build /home/arun/abhiyaan/Section_A/build/welcome /home/arun/abhiyaan/Section_A/build/welcome/CMakeFiles/welcome_gennodejs.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : welcome/CMakeFiles/welcome_gennodejs.dir/depend
