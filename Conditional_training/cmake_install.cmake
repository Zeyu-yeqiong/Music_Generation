# Install script for directory: D:/fluidsynth-2.0.4/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/FluidSynth")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE EXECUTABLE FILES "D:/fluidsynth-2.0.4/build/src/fluidsynth.exe")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/fluidsynth.exe" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/fluidsynth.exe")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "D:/CMakeFiles/bin/strip.exe" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/fluidsynth.exe")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY OPTIONAL FILES "D:/fluidsynth-2.0.4/build/src/libfluidsynth.dll.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" TYPE SHARED_LIBRARY FILES "D:/fluidsynth-2.0.4/build/src/libfluidsynth-2.dll")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/libfluidsynth-2.dll" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/libfluidsynth-2.dll")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "D:/CMakeFiles/bin/strip.exe" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/bin/libfluidsynth-2.dll")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/fluidsynth" TYPE FILE FILES
    "D:/fluidsynth-2.0.4/include/fluidsynth/audio.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/event.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/gen.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/ladspa.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/log.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/midi.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/misc.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/mod.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/seq.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/seqbind.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/settings.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/sfont.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/shell.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/synth.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/types.h"
    "D:/fluidsynth-2.0.4/include/fluidsynth/voice.h"
    "D:/fluidsynth-2.0.4/build/include/fluidsynth/version.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES "D:/fluidsynth-2.0.4/build/include/fluidsynth.h")
endif()

