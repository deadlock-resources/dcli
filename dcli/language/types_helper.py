import json

import inquirer

from dcli.generator import file

PRIMITIVE_TYPE = 'Primitive type (eg int, character)'

DEFAULT_VALUE = 'defaultValue'

METHOD_NAME = 'METHOD_NAME'

FILE_NAME = 'FILE_NAME'

GENERIC = 'Generic (eg T, R)'

ARRAY_DIMENSION = 'number'

TYPE_NAME = 'name'

CLASS_NAME = 'className'

ARRAY = 'Array'

CONTINUE = 'continue'

YES = 'Yes'

NO = 'No'

PARAM_NAME = 'paramName'

TYPE = 'type'

PARAMETRIZED_TYPE = 'Type to parametrize (eg a list)'

KNOWN_LIB_LANGUAGE_TYPE = 'Existing type from language lib (eg InputStream in java)'
OWN_TYPE = 'Your own type (will be created at generation)'


def does_user_continue(parameter_="Do you want to continue"):
    continue_questions = [
        inquirer.List(CONTINUE,
                      message=parameter_,
                      choices=[YES, NO],
                      ),
    ]
    answer = inquirer.prompt(continue_questions)
    return answer[CONTINUE] == YES


def select_type_from_dict(question_msg='What type do you need ?', types_dict=[]):
    questions = [
        inquirer.List(TYPE,
                      message=question_msg,
                      choices=types_dict,
                      ),
    ]
    answers = inquirer.prompt(questions)
    return answers


def get_param_name():
    arg_questions = [
        inquirer.Text(PARAM_NAME, message="What is the parameter name ?")
    ]
    return inquirer.prompt(arg_questions)[PARAM_NAME]


def read_json_types(json_file):
    loaded_types = json.load(json_file)
    types_to_choose = {}
    for current_type in loaded_types:
        name_ = current_type[TYPE_NAME]
        default_value_ = current_type[DEFAULT_VALUE]
        my_val = StructDescription(type_name=name_, default_value=default_value_)

        types_to_choose.update({my_val.type_name: my_val.default_value})
    return types_to_choose


class FormAnswersCollector:
    def __init__(self, language_id,
                 filename,
                 allow_typing=True,
                 have_generics=True,
                 have_parametrized=True,
                 allow_type_creation=True,
                 allow_lib=True):
        self.allow_typing = allow_typing
        json_file = file.openFile(language_id, 'resources' + '/' + filename)
        self.types_to_choose_dict = read_json_types(json_file)
        self.structure_holder = self.get_datatype_from_user(
            language_id=language_id,
            filename=filename,
            have_generics=have_generics,
            have_parametrized=have_parametrized,
            allow_type_creation=allow_type_creation,
            allow_lib=allow_lib)

    def get_datatype_from_user(self, language_id,
                               filename,
                               have_generics=True,
                               have_parametrized=True,
                               allow_type_creation=True,
                               allow_lib=True):
        return self.select_types_from_json(have_generics=have_generics,
                                           have_parametrized=have_parametrized,
                                           allow_type_creation=allow_type_creation,
                                           allow_lib=allow_lib)

    def select_types_from_json(self,
                               have_generics=True,
                               have_parametrized=True,
                               allow_type_creation=True,
                               allow_lib=True):
        types_to_choose = self.read_and_store_types_from_file(allow_lib, allow_type_creation, have_generics,
                                                              have_parametrized)
        file_question = [
            inquirer.Text(FILE_NAME,
                          message='Type the Main file name for the user, (e.g. MainFile) without extension:'),
            inquirer.Text(METHOD_NAME,
                          message='Type the method name, Main method for the user, entry point of the program (e.g. mainMethod):')
        ]
        answers = inquirer.prompt(file_question)
        file_name = answers[FILE_NAME]
        method_name = answers[METHOD_NAME]
        method_return_type = self.handle_param_or_return(False, types_to_choose)
        parameters = self.handle_param_or_return(True, types_to_choose)
        ret = StructureHolder(structure_name=file_name,
                              file_names=[file_name],
                              methods=[MethodHolder(method_name=method_name,
                                                    return_type=method_return_type[0],
                                                    method_parameters=parameters)])
        print(str(ret.methods[0].get_generics_types()))
        return ret;

    def read_and_store_types_from_file(self, allow_lib, allow_type_creation, have_generics, have_parametrized):
        # types_to_choose = list(self.types_to_choose_dict.keys())
        types_to_choose = [PRIMITIVE_TYPE, ARRAY]
        if have_generics:
            types_to_choose.append(GENERIC)
        if allow_lib:
            types_to_choose.append(KNOWN_LIB_LANGUAGE_TYPE)
        if have_parametrized:
            types_to_choose.append(PARAMETRIZED_TYPE)
        if allow_type_creation:
            types_to_choose.append(OWN_TYPE)

        return types_to_choose

    def handle_param_or_return(self, is_arg, types_dict, fresh_start=False):
        if is_arg:
            if fresh_start is True:
                ret = self.handle_method_param(is_arg, types_dict, previous_arg=[])
            else:
                ret = self.handle_method_param(is_arg, types_dict)

        else:
            ret = [self.get_user_type(is_it_param=is_arg, types_dict=types_dict, current_type_kind='method return',
                                      suffix_text='the return type of the previous entered method, what the user will have to return (e.g. String)')]
        current_res = ''.join(map(str, ret))
        if not does_user_continue('Are you sure of your choice  ' + current_res + ' ?'):
            print('Restart choice')
            ret = self.handle_param_or_return(is_arg, types_dict, True)
        else:
            print(current_res)
        return ret

    def handle_method_param(self, is_arg, current_dict, previous_arg=[]):
        print("current args : " + str(previous_arg))
        previous_arg.append(
            self.get_user_type(is_it_param=is_arg, types_dict=current_dict,
                               current_type_kind='method parameter',
                               suffix_text='( for the parameter number ' + str(len(previous_arg) + 1) + ' )'))
        if does_user_continue("Do you need an other parameter ?"):
            self.handle_method_param(is_arg, current_dict, previous_arg)
        return previous_arg

    def get_user_type(self, is_it_param, types_dict, is_sub_type=False, sub_types_dic=None, parent_name='',
                      current_type_kind='required', suffix_text=''):
        types_to_display = sub_types_dic if is_sub_type is True or sub_types_dic else types_dict
        if self.allow_typing:
            answers = select_type_from_dict(
                question_msg='What is the ' + current_type_kind + ' type' + ' ' + suffix_text + ' ?',
                types_dict=types_to_display)
            type_ = answers[TYPE]
        else:
            type_ = ''
        type_need_creation = False
        type_need_import = False
        is_array = False
        array_dim = 0
        array_type = ''
        parametrized_root_type = ''
        parametrized_types = []
        param_name = ''
        is_generic = False
        default_value = None
        if type_ == OWN_TYPE:
            new_questions = [
                inquirer.Text(TYPE, message='Type your new full type name')
            ]
            type_ = inquirer.prompt(new_questions)[TYPE]
            type_need_creation = True
            type_need_import = True

        elif type_ == KNOWN_LIB_LANGUAGE_TYPE:
            new_questions = [
                inquirer.Text(TYPE, message='Type the lib language full type name')
            ]
            type_ = inquirer.prompt(new_questions)[TYPE]
            type_need_creation = False
            type_need_import = True

        elif type_ == PRIMITIVE_TYPE:
            reduced_type_list = self.types_to_choose_dict.copy()
            type_ = self.get_user_type(is_it_param=is_it_param, types_dict=types_dict,
                                       is_sub_type=True,
                                       sub_types_dic=reduced_type_list,
                                       current_type_kind=' to select').type_name
        elif type_ == GENERIC:
            new_questions = [
                inquirer.Text(TYPE, message='Type the generic type name')
            ]
            is_generic = True
            type_ = inquirer.prompt(new_questions)[TYPE]

        elif type_ == ARRAY:
            reduced_type_list = types_dict.copy()
            reduced_type_list.remove(ARRAY)
            array_question = [inquirer.List(ARRAY_DIMENSION,
                                            message="What is the number of dimension of your array ?",
                                            choices=[1, 2, 3, 4, 5],
                                            )]
            array_dim = inquirer.prompt(array_question)[ARRAY_DIMENSION]
            array_type = self.get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                            sub_types_dic=reduced_type_list, current_type_kind='array')

            is_array = True

        elif type_ == PARAMETRIZED_TYPE:
            reduced_type_list = types_dict.copy()
            reduced_type_list.remove(ARRAY)
            reduced_type_list.remove(PARAMETRIZED_TYPE)
            parametrized_root_type = self.get_user_type(is_it_param=is_it_param, types_dict=types_dict,
                                                        is_sub_type=True,
                                                        sub_types_dic=reduced_type_list,
                                                        current_type_kind='to parametrize')
            parametrized_types.append(
                self.get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                   sub_types_dic=reduced_type_list,
                                   current_type_kind='parametrized'))
            while does_user_continue("Do you need an other parameter type"):
                parametrized_types.append(
                    self.get_user_type(is_it_param=is_it_param, types_dict=types_dict, is_sub_type=True,
                                       sub_types_dic=reduced_type_list,
                                       current_type_kind='parametrized'))
        if self.allow_typing:
            default_value = self.types_to_choose_dict.get(type_)
            print('default value is :' + str(default_value))
        if is_it_param and not is_sub_type:
            param_name = get_param_name()
        elif is_sub_type:
            param_name = parent_name
        print('type is :' + type_)

        ret = DataTypeHolder(type_name=type_,
                             need_import=type_need_import,
                             need_creation=type_need_creation,
                             is_arg=is_it_param,
                             arg_name=param_name,
                             is_array=is_array,
                             array_dim=array_dim,
                             array_type=array_type,
                             parametrized_root_type=parametrized_root_type,
                             param_types=parametrized_types,
                             is_generic=is_generic,
                             default_value=default_value)

        return ret


class DataTypeHolder:
    def __init__(self, type_name, need_import, need_creation, is_arg, arg_name='', is_generic=False, param_types=[],
                 parametrized_root_type=None,
                 is_array=False, array_dim=1, array_type='', default_value=None):
        if isinstance(default_value, str) and len(str(default_value)) > 0:
            default_value = r"'0'"

        self.default_value = default_value
        self.parametrized_root_type = parametrized_root_type
        self.array_type = array_type
        self.type_name = type_name
        self.need_import = need_import
        self.need_creation = need_creation
        self.is_arg = is_arg
        self.arg_name = arg_name
        self.is_generic = is_generic
        self.parameters_types = param_types
        self.is_array = is_array
        self.array_dim = array_dim

    def add_parameter_type(self, type_name):
        self.parameters_types.append(type_name)

    def __str__(self):
        ret = ''
        ret += '['
        if self.is_array:
            ret += self.array_type.type_name
            for i in range(0, self.array_dim):
                ret += '[]'
        elif len(self.parameters_types) > 0:
            ret += self.parametrized_root_type.type_name + '<'
            param_length = len(self.parameters_types)
            for i in range(0, param_length):
                if param_length > 1 and i > 0:
                    ret += ',' + self.parameters_types[i].type_name
                else:
                    ret += self.parameters_types[i].type_name
            ret += '>'
        else:
            ret += self.type_name
        if self.is_arg:
            ret += ' ' + self.arg_name
        ret += ']'
        return ret


class StructureHolder:
    def __init__(self, structure_name, file_names, methods, attributes=[]):
        self.file_names = file_names
        self.structure_name = structure_name
        self.methods = methods
        self.attributes = attributes

    def __str__(self):
        return json.dumps(self, default=lambda x: x.__dict__)


class MethodHolder:
    def __init__(self, method_name, return_type, method_parameters=[]):
        self.return_type = return_type
        self.method_parameters = method_parameters
        self.method_name = method_name

    def get_generics_types(self):
        all_types = self.method_parameters + [self.return_type]
        print(str(all_types))
        my_array = []
        for my_type in all_types:
            get_gens_from(my_type, my_array)
        return my_array
        # return map(lambda current: get_gens_from(current), all_types)


def get_gens_from(current_type, ret=[]):
    print('try to add ' + current_type.type_name + 'in return generics array, is_generic = ' + str(
        current_type.is_generic))
    if current_type.is_generic:
        print('adding ' + current_type.type_name + 'in return generics array')
        ret.append(current_type.type_name)
    elif current_type.is_array:
        get_gens_from(current_type.array_type, ret)

    for currentParam in current_type.parameters_types:
        get_gens_from(currentParam, ret)
    return ret


class StructDescription:
    def __init__(self, type_name='', default_value=None):
        self.default_value = default_value
        self.type_name = type_name
