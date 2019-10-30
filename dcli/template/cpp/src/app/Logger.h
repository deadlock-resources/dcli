//
// Created by Guillaume Danguy on 22/06/17.
//

#ifndef LOGGER_H
#define LOGGER_H

#include <string>
using std::string;
using std::exception;


class Logger {
public:
    static void log_success();
    static void log_no_match();
    static void log({{ targetMethodReturn }} user, {{ targetMethodReturn }} expected);
    static void log_unexpected_error(const string& expected);
    static void log_exception(const exception& e);
};


#endif //LOGGER_H
