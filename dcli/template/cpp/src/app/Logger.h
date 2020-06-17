#ifndef LOGGER_H
#define LOGGER_H
{% for asset in targetAssetsToImport %}
#include "{{ asset.fileName }}.{{ asset.extension }}"
{% endfor %}
#include <string>
using std::string;
using std::exception;


class Logger {
public:
    static void log_success();
    static void log_no_match();
    {%if targetMethodReturn != "" %}
    static void log({{ targetMethodReturn }} user, {{ targetMethodReturn }} expected);
    {% endif %}
    static void log_unexpected_error(const string& expected);
    static void log_exception(const exception& e);
};


#endif //LOGGER_H
