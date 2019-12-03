package success;

import java.util.*;

public class {{ targetFile }} {

    public static void main() {

    }

    public static {% if targetMethodReturn == "" %}void{% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }}) {
        //TODO write your own solution
        {% if targetMethodReturn != "" %}return null;{% endif %}
    }
}
