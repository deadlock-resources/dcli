package app

import template.{{ targetFile }}

/**
 * Class executed when user click on `Run` button.
 */
class Run {
    companion object {
        fun main() {
            try {
                // just run user code
                {{ targetFile }}.main();
            } catch (e: RuntimeException) {
                Logger.logException(e);
            }
        }
    }

}
