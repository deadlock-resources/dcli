package template;

import java.util.*;

public class {{ targetFile }} {

    /**
     * Called when you Run your code
     */
    public static void main() {

    }

    /**
     * Called when you Submit your code
     */
    public static {% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }}) {
        {% if targetMethodReturn != "" %}return null;{% endif %}
    }
}
