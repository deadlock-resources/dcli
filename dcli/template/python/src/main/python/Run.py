# File executed when user click on `Run` button
# Must not run any test, just run the user
if __name__ == "__main__":
    import template
    template.{{ targetMethod }}{% if targetMethodArgs != "" %} #TODO define your own args 
    {% endif %}
