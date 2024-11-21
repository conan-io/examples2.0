#pragma once

#ifdef WIN32
  #define say_EXPORT __declspec(dllexport)
#else
  #define say_EXPORT
#endif

say_EXPORT void say();
