#include <iostream>
#include "say.h"

void say(){
    #ifdef NDEBUG
    std::cout << "say/1.0: Hello World Release!\n";
    #else
    std::cout << "say/1.0: Hello World Debug!\n";
    #endif
}
