//
// Created by Guillaume Danguy on 22/06/17.
//

/**
 * This class provides log wrappers for the classic system signals.
 */
#include "Logger.h"
#include <iostream>
#include <string>

using std::string;
using std::endl;
using std::cout;
using std::cerr;
using std::exception;

void Logger::log_success() {
    cout << "----------------------------------------------------" << endl;
    cout << "Good Job!" << endl;
    cout << "----------------------------------------------------" << endl;
}

void Logger::log({{ targetMethodReturn }} user, {{ targetMethodReturn }} expected) {
    cout << "----------------------------------------------------" << endl;
    cout << "Your result: " << user << endl;
    cout << "Expected: " << expected << endl;
    cout << "----------------------------------------------------" << endl;
}

void Logger::log_no_match() {
    cerr << "----------------------------------------------------" << endl;
    cerr << "It does not match, not expected result." << endl;
    cerr << "----------------------------------------------------" << endl;
}

void Logger::log_unexpected_error(const string& expected) {
    cerr << "----------------------------------------------------" << endl;
    cerr << "An error occurred at runtime." << endl;
    cerr << "Details:" << endl;
    cerr << "Expected: " << expected << endl;
    cerr << "----------------------------------------------------" << endl;
}

void Logger::log_exception(const exception& e) {
    cerr << "----------------------------------------------------" << endl;
    cerr << "Something bad happened." << endl;
    cerr << "Details: " << e.what() << endl;
    cerr << "----------------------------------------------------" << endl;
}


