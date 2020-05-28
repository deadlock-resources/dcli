
{% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }}) {
    {% if targetMethodReturn != "" %}return {{ targetMethodReturnValue }};{% endif %}
}