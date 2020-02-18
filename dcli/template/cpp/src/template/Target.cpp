#include "Target.h"

{% if targetGenerics != "" %} template<{{ targetGenerics }}>{% endif %}
{{ targetMethodReturn }} Target::{{ targetMethod }}({{ targetMethodArgs }}) {
    return {% if targetDefaultReturn == None %} NULL {% elif targetDefaultReturn is sameas false %} false {% else %}{{ targetDefaultReturn }}{% endif %};
}
