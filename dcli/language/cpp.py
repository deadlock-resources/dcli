from .language import Language

BLANK = ' '

TEMPLATE_SEPARATOR = ','

CLOSE_TEMPLATE = '>'

OPEN_TEMPLATE = '<'

ARRAY_REPRESENTATION = '[]'

TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.cpp'
RUN_PATH = '/src/app/main.cpp'

ASSET_PATHS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.cpp', 'src/app/Logger.h']

TARGET_FILE = 'Target'


class Cpp(Language):
    def __init__(self):
        Language.__init__(self,
                          'cpp',
                          TEMPLATE_PATH,
                          SUCCESS_PATH,
                          APP_PATH,
                          SOLVE_PATH,
                          RUN_PATH,
                          TARGET_FILE,
                          'cpp',
                          ASSET_PATHS
                          )

    def format_data(self, datatype_holder):
        ret = ''
        if datatype_holder.is_array:
            ret += datatype_holder.array_type.type_name
            for i in range(0, datatype_holder.array_dim):
                ret += ARRAY_REPRESENTATION
        elif len(datatype_holder.parameters_types) > 0:
            ret += datatype_holder.parametrized_root_type.type_name + OPEN_TEMPLATE
            param_length = len(datatype_holder.parameters_types)
            for i in range(0, param_length):
                if param_length > 1 and i > 0:
                    ret += TEMPLATE_SEPARATOR + datatype_holder.parameters_types[i].type_name
                else:
                    ret += datatype_holder.parameters_types[i].type_name
            ret += CLOSE_TEMPLATE
        else:
            ret += datatype_holder.type_name
        if datatype_holder.is_arg:
            ret += BLANK + datatype_holder.arg_name
        return ret

    def format_generic_declaration(self, type_name):
        return 'typename ' + type_name
