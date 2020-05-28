#include <iostream>
#include <vector>

using namespace std;

{% if targetMethodArgsHasCommonType %}
class {{ targetMethodArgsHasCommonType }} {};
{% endif %}

{% if targetMethodReturnHasCommonType %}
{% if targetMethodReturnHasCommonType != targetMethodArgsHasCommonType %}
class {{ targetMethodReturnHasCommonType }} {};
{% endif %}
{% endif %}


class Target {
public:
    {% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }});
};