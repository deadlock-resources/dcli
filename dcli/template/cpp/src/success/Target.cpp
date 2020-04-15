
{% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }}) {
    return 0;
}
