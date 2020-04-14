package template

class {{ targetFile }} {
    companion object {
        /**
        * Called when you Run your code
        */
        fun main() {

        }

        /**
        * Called when you Submit your code
        */
        fun {{ targetMethod }}({{ targetMethodArgs }}): {% if targetMethodReturn == "" %}Unit{% else %}{{ targetMethodReturn }}{% endif %} {
            {% if targetMethodReturn != "" %}return {{ targetMethodReturnValue }};{% endif %}
        }
    }
}