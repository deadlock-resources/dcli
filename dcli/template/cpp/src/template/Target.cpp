#include "Target.h"

{% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} Target::{{ targetMethod }}({{ targetMethodArgs }}) {
    {% if targetMethodReturn != "" %}return 0;{% endif %}
}
