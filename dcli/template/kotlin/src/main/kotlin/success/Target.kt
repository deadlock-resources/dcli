package success

import java.util.*

class {{ targetFile }} {
    companion object {
        fun {{ targetMethod }}({{ targetMethodArgs }}): {% if targetMethodReturn == "" %}Unit{% else %}{{ targetMethodReturn }}{% endif %} {
            //TODO write your own solution
            {% if targetMethodReturn != "" %}return {{ targetMethodReturnValue }};{% endif %}
        }
    }
}
