#include <iostream>
#include <vector>

using namespace std;

class Target {
public:
    {% if targetGenerics != "" %} template<{{ targetGenerics }}>{% endif %}
    {{ targetMethodReturn }} {{ targetMethod }}({{ targetMethodArgs }});
};
