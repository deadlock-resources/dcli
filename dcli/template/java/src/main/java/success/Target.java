package success;

import java.util.*;

public class {{ targetFile }} {

    public static void main() {

    }

    public static {% if targetGenerics != "" %}<{{ targetGenerics }}> {% endif %}{% if targetMethodReturn == "" %}void {% else %}{{ targetMethodReturn }}{% endif %} {{ targetMethod }}({{ targetMethodArgs }}) {
        //TODO write your own solution
        return {% if targetDefaultReturn == None %} null {% else %}{{ targetDefaultReturn }}{% endif %};
    }
}
