#ifndef TARGET_H_
#define TARGET_H_
#include <stdbool.h>

{% if targetMethodArgsHasCommonType %}
typedef struct {{ targetMethodArgsHasCommonType }} {{ targetMethodArgsHasCommonType }};
struct {{ targetMethodArgsHasCommonType }} {};
{% endif %}

{% if targetMethodReturnHasCommonType %}
{% if targetMethodReturnHasCommonType != targetMethodArgsHasCommonType %}
typedef struct {{ targetMethodReturnHasCommonType }} {{ targetMethodReturnHasCommonType }};
struct {{ targetMethodReturnHasCommonType }} {};
{% endif %}
{% endif %}

{{ targetMethodReturn }} {{ targetMethod }}({{ targetMethodArgs }});

void run();

#endif // TARGET_H_