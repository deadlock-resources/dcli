#include <iostream>
#include <vector>

using namespace std;

class Target {
public:
    {% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }});
};
