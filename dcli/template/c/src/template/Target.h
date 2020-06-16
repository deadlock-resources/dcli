#ifndef TARGET_H_
#define TARGET_H_
{% for asset in targetAssetList %}
#include "{{ asset.fileName }}.{{ asset.extension }}"
{% endfor %}
#include <stdbool.h>

{{ targetMethodReturn }} {{ targetMethod }}({{ argetMethodArgs }});

void run();

#endif // TARGET_H_