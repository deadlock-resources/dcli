from .language import Language

TEMPLATE_PATH = '/src/main/java/template'
SUCCESS_PATH = '/src/main/java/success'
APP_PATH = '/src/main/java/app'

SOLVE_PATH = '/src/main/java/app/Solve.java'
RUN_PATH = '/src/main/java/app/Run.java'

ASSET_PATHS = ['/src/main/java/app/Logger.java']

TARGET_FILE = 'Target'
BLANK = ' '

TEMPLATE_SEPARATOR = ','

CLOSE_TEMPLATE = '>'

OPEN_TEMPLATE = '<'

ARRAY_REPRESENTATION = '[]'


class Java(Language):
    def __init__(self):
        Language.__init__(self,
                          'java',
                          TEMPLATE_PATH,
                          SUCCESS_PATH,
                          APP_PATH,
                          SOLVE_PATH,
                          RUN_PATH,
                          TARGET_FILE,
                          'java',
                          ASSET_PATHS
                          )

    def addType(self, name):
        self.addNewAsset(self.templateDirPath, name, f'package template;\n\nclass {name} {{}}')
        self.addNewAsset(self.successDirPath, name, f'package success;\n\nclass {name} {{}}')

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
        return type_name
