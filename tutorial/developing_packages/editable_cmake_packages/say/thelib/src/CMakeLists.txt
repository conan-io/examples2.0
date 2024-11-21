add_library(say say.cpp)
# target_include_directories(say PUBLIC include)

# set_target_properties(say PROPERTIES PUBLIC_HEADER "include/say.h")
install(TARGETS say)
install(FILES say.h DESTINATION "include/say")
