from .language import Language

TEMPLATE_PATH = '/src/template'
SUCCESS_PATH = '/src/success'
APP_PATH = '/src/app'

SOLVE_PATH = '/src/app/main.c'
RUN_PATH = '/src/app/main.c'

ASSET_PATHS = ['src/Makefile', 'src/template/Target.h', 'src/app/Logger.c', 'src/app/Logger.h']

TARGET_FILE = 'Target'

BLANK = ' '

TEMPLATE_SEPARATOR = ','

CLOSE_TEMPLATE = '>'

OPEN_TEMPLATE = '<'

ARRAY_REPRESENTATION = '[]'


class C(Language):
    def __init__(self):
        Language.__init__(self,
                          'c',
                          TEMPLATE_PATH,
                          SUCCESS_PATH,
                          APP_PATH,
                          SOLVE_PATH,
                          RUN_PATH,
                          TARGET_FILE,
                          'c',
                          ASSET_PATHS
                          )

    def format_data(self, datatype_holder):
        formatted_data = ''
        if datatype_holder.is_array:
            formatted_data += datatype_holder.array_type.type_name
            for i in range(0, datatype_holder.array_dim):
                formatted_data += ARRAY_REPRESENTATION
        elif len(datatype_holder.parameters_types) > 0:
            formatted_data += datatype_holder.parametrized_root_type.type_name + OPEN_TEMPLATE
            param_length = len(datatype_holder.parameters_types)
            for i in range(0, param_length):
                if param_length > 1 and i > 0:
                    formatted_data += TEMPLATE_SEPARATOR + datatype_holder.parameters_types[i].type_name
                else:
                    formatted_data += datatype_holder.parameters_types[i].type_name
            formatted_data += CLOSE_TEMPLATE
        else:
            formatted_data += datatype_holder.type_name
        if datatype_holder.is_arg:
            formatted_data += BLANK + datatype_holder.arg_name
        return formatted_data
