
{{ targetMethodReturn }} {{ targetMethod }}({{ targetMethodArgs }}) {
    return {% if targetDefaultReturn == None %} NULL {% elif targetDefaultReturn is sameas false %} false {% else %}{{ targetDefaultReturn }}{% endif %};
}
