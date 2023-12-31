# This file is generated by Tools/cases_generator/generate_cases.py
# from:
#   Python/bytecodes.c
# Do not edit!

_specializations = {
    "RESUME": [
        "RESUME_CHECK",
    ],
    "TO_BOOL": [
        "TO_BOOL_ALWAYS_TRUE",
        "TO_BOOL_BOOL",
        "TO_BOOL_INT",
        "TO_BOOL_LIST",
        "TO_BOOL_NONE",
        "TO_BOOL_STR",
    ],
    "BINARY_OP": [
        "BINARY_OP_MULTIPLY_INT",
        "BINARY_OP_ADD_INT",
        "BINARY_OP_SUBTRACT_INT",
        "BINARY_OP_MULTIPLY_FLOAT",
        "BINARY_OP_ADD_FLOAT",
        "BINARY_OP_SUBTRACT_FLOAT",
        "BINARY_OP_ADD_UNICODE",
    ],
    "BINARY_SUBSCR": [
        "BINARY_SUBSCR_DICT",
        "BINARY_SUBSCR_GETITEM",
        "BINARY_SUBSCR_LIST_INT",
        "BINARY_SUBSCR_STR_INT",
        "BINARY_SUBSCR_TUPLE_INT",
    ],
    "STORE_SUBSCR": [
        "STORE_SUBSCR_DICT",
        "STORE_SUBSCR_LIST_INT",
    ],
    "SEND": [
        "SEND_GEN",
    ],
    "UNPACK_SEQUENCE": [
        "UNPACK_SEQUENCE_TWO_TUPLE",
        "UNPACK_SEQUENCE_TUPLE",
        "UNPACK_SEQUENCE_LIST",
    ],
    "STORE_ATTR": [
        "STORE_ATTR_INSTANCE_VALUE",
        "STORE_ATTR_SLOT",
        "STORE_ATTR_WITH_HINT",
    ],
    "LOAD_GLOBAL": [
        "LOAD_GLOBAL_MODULE",
        "LOAD_GLOBAL_BUILTIN",
    ],
    "LOAD_SUPER_ATTR": [
        "LOAD_SUPER_ATTR_ATTR",
        "LOAD_SUPER_ATTR_METHOD",
    ],
    "LOAD_ATTR": [
        "LOAD_ATTR_INSTANCE_VALUE",
        "LOAD_ATTR_MODULE",
        "LOAD_ATTR_WITH_HINT",
        "LOAD_ATTR_SLOT",
        "LOAD_ATTR_CLASS",
        "LOAD_ATTR_PROPERTY",
        "LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN",
        "LOAD_ATTR_METHOD_WITH_VALUES",
        "LOAD_ATTR_METHOD_NO_DICT",
        "LOAD_ATTR_METHOD_LAZY_DICT",
        "LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES",
        "LOAD_ATTR_NONDESCRIPTOR_NO_DICT",
    ],
    "COMPARE_OP": [
        "COMPARE_OP_FLOAT",
        "COMPARE_OP_INT",
        "COMPARE_OP_STR",
    ],
    "FOR_ITER": [
        "FOR_ITER_LIST",
        "FOR_ITER_TUPLE",
        "FOR_ITER_RANGE",
        "FOR_ITER_GEN",
    ],
    "CALL": [
        "CALL_BOUND_METHOD_EXACT_ARGS",
        "CALL_PY_EXACT_ARGS",
        "CALL_PY_WITH_DEFAULTS",
        "CALL_NO_KW_TYPE_1",
        "CALL_NO_KW_STR_1",
        "CALL_NO_KW_TUPLE_1",
        "CALL_BUILTIN_CLASS",
        "CALL_NO_KW_BUILTIN_O",
        "CALL_NO_KW_BUILTIN_FAST",
        "CALL_BUILTIN_FAST_WITH_KEYWORDS",
        "CALL_NO_KW_LEN",
        "CALL_NO_KW_ISINSTANCE",
        "CALL_NO_KW_LIST_APPEND",
        "CALL_NO_KW_METHOD_DESCRIPTOR_O",
        "CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS",
        "CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS",
        "CALL_NO_KW_METHOD_DESCRIPTOR_FAST",
        "CALL_NO_KW_ALLOC_AND_ENTER_INIT",
    ],
}

# An irregular case:
_specializations["BINARY_OP"].append("BINARY_OP_INPLACE_ADD_UNICODE")

_specialized_opmap = {
    'BINARY_OP_ADD_FLOAT': 3,
    'BINARY_OP_ADD_INT': 4,
    'BINARY_OP_ADD_UNICODE': 5,
    'BINARY_OP_INPLACE_ADD_UNICODE': 6,
    'BINARY_OP_MULTIPLY_FLOAT': 7,
    'BINARY_OP_MULTIPLY_INT': 8,
    'BINARY_OP_SUBTRACT_FLOAT': 9,
    'BINARY_OP_SUBTRACT_INT': 10,
    'BINARY_SUBSCR_DICT': 13,
    'BINARY_SUBSCR_GETITEM': 14,
    'BINARY_SUBSCR_LIST_INT': 15,
    'BINARY_SUBSCR_STR_INT': 16,
    'BINARY_SUBSCR_TUPLE_INT': 18,
    'RESUME_CHECK': 47,
    'STORE_ATTR_INSTANCE_VALUE': 51,
    'STORE_ATTR_SLOT': 52,
    'STORE_SUBSCR_DICT': 55,
    'STORE_SUBSCR_LIST_INT': 56,
    'TO_BOOL_ALWAYS_TRUE': 58,
    'TO_BOOL_BOOL': 59,
    'TO_BOOL_INT': 60,
    'TO_BOOL_LIST': 61,
    'TO_BOOL_NONE': 62,
    'TO_BOOL_STR': 63,
    'CALL_BOUND_METHOD_EXACT_ARGS': 77,
    'CALL_BUILTIN_CLASS': 78,
    'CALL_BUILTIN_FAST_WITH_KEYWORDS': 79,
    'CALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS': 83,
    'CALL_NO_KW_ALLOC_AND_ENTER_INIT': 84,
    'CALL_NO_KW_BUILTIN_FAST': 85,
    'CALL_NO_KW_BUILTIN_O': 86,
    'CALL_NO_KW_ISINSTANCE': 87,
    'CALL_NO_KW_LEN': 88,
    'CALL_NO_KW_LIST_APPEND': 89,
    'CALL_NO_KW_METHOD_DESCRIPTOR_FAST': 90,
    'CALL_NO_KW_METHOD_DESCRIPTOR_NOARGS': 91,
    'CALL_NO_KW_METHOD_DESCRIPTOR_O': 92,
    'CALL_NO_KW_STR_1': 93,
    'CALL_NO_KW_TUPLE_1': 94,
    'CALL_NO_KW_TYPE_1': 95,
    'CALL_PY_EXACT_ARGS': 96,
    'CALL_PY_WITH_DEFAULTS': 97,
    'COMPARE_OP_FLOAT': 99,
    'COMPARE_OP_INT': 100,
    'COMPARE_OP_STR': 101,
    'FOR_ITER_GEN': 116,
    'FOR_ITER_LIST': 117,
    'FOR_ITER_RANGE': 118,
    'FOR_ITER_TUPLE': 119,
    'LOAD_ATTR_CLASS': 131,
    'LOAD_ATTR_GETATTRIBUTE_OVERRIDDEN': 132,
    'LOAD_ATTR_INSTANCE_VALUE': 133,
    'LOAD_ATTR_METHOD_LAZY_DICT': 134,
    'LOAD_ATTR_METHOD_NO_DICT': 135,
    'LOAD_ATTR_METHOD_WITH_VALUES': 136,
    'LOAD_ATTR_MODULE': 137,
    'LOAD_ATTR_NONDESCRIPTOR_NO_DICT': 138,
    'LOAD_ATTR_NONDESCRIPTOR_WITH_VALUES': 139,
    'LOAD_ATTR_PROPERTY': 140,
    'LOAD_ATTR_SLOT': 141,
    'LOAD_ATTR_WITH_HINT': 142,
    'LOAD_GLOBAL_BUILTIN': 152,
    'LOAD_GLOBAL_MODULE': 153,
    'LOAD_SUPER_ATTR_ATTR': 156,
    'LOAD_SUPER_ATTR_METHOD': 157,
    'SEND_GEN': 170,
    'STORE_ATTR_WITH_HINT': 175,
    'UNPACK_SEQUENCE_LIST': 185,
    'UNPACK_SEQUENCE_TUPLE': 186,
    'UNPACK_SEQUENCE_TWO_TUPLE': 187,
}

opmap = {
    'CACHE': 0,
    'BEFORE_ASYNC_WITH': 1,
    'BEFORE_WITH': 2,
    'BINARY_SLICE': 11,
    'BINARY_SUBSCR': 12,
    'RESERVED': 17,
    'CHECK_EG_MATCH': 19,
    'CHECK_EXC_MATCH': 20,
    'CLEANUP_THROW': 21,
    'DELETE_SUBSCR': 22,
    'END_ASYNC_FOR': 23,
    'END_FOR': 24,
    'END_SEND': 25,
    'EXIT_INIT_CHECK': 26,
    'FORMAT_SIMPLE': 27,
    'FORMAT_WITH_SPEC': 28,
    'GET_AITER': 29,
    'GET_ANEXT': 30,
    'GET_ITER': 31,
    'GET_LEN': 32,
    'GET_YIELD_FROM_ITER': 33,
    'INTERPRETER_EXIT': 34,
    'LOAD_ASSERTION_ERROR': 35,
    'LOAD_BUILD_CLASS': 36,
    'LOAD_LOCALS': 37,
    'MAKE_FUNCTION': 38,
    'MATCH_KEYS': 39,
    'MATCH_MAPPING': 40,
    'MATCH_SEQUENCE': 41,
    'NOP': 42,
    'POP_EXCEPT': 43,
    'POP_TOP': 44,
    'PUSH_EXC_INFO': 45,
    'PUSH_NULL': 46,
    'RETURN_GENERATOR': 48,
    'RETURN_VALUE': 49,
    'SETUP_ANNOTATIONS': 50,
    'STORE_SLICE': 53,
    'STORE_SUBSCR': 54,
    'TO_BOOL': 57,
    'UNARY_INVERT': 64,
    'UNARY_NEGATIVE': 65,
    'UNARY_NOT': 66,
    'WITH_EXCEPT_START': 67,
    'BINARY_OP': 68,
    'BUILD_CONST_KEY_MAP': 69,
    'BUILD_LIST': 70,
    'BUILD_MAP': 71,
    'BUILD_SET': 72,
    'BUILD_SLICE': 73,
    'BUILD_STRING': 74,
    'BUILD_TUPLE': 75,
    'CALL': 76,
    'CALL_FUNCTION_EX': 80,
    'CALL_INTRINSIC_1': 81,
    'CALL_INTRINSIC_2': 82,
    'COMPARE_OP': 98,
    'CONTAINS_OP': 102,
    'CONVERT_VALUE': 103,
    'COPY': 104,
    'COPY_FREE_VARS': 105,
    'DELETE_ATTR': 106,
    'DELETE_DEREF': 107,
    'DELETE_FAST': 108,
    'DELETE_GLOBAL': 109,
    'DELETE_NAME': 110,
    'DICT_MERGE': 111,
    'DICT_UPDATE': 112,
    'ENTER_EXECUTOR': 113,
    'EXTENDED_ARG': 114,
    'FOR_ITER': 115,
    'GET_AWAITABLE': 120,
    'IMPORT_FROM': 121,
    'IMPORT_NAME': 122,
    'IS_OP': 123,
    'JUMP_BACKWARD': 124,
    'JUMP_BACKWARD_NO_INTERRUPT': 125,
    'JUMP_FORWARD': 126,
    'KW_NAMES': 127,
    'LIST_APPEND': 128,
    'LIST_EXTEND': 129,
    'LOAD_ATTR': 130,
    'LOAD_CONST': 143,
    'LOAD_DEREF': 144,
    'LOAD_FAST': 145,
    'LOAD_FAST_AND_CLEAR': 146,
    'LOAD_FAST_CHECK': 147,
    'LOAD_FAST_LOAD_FAST': 148,
    'LOAD_FROM_DICT_OR_DEREF': 149,
    'LOAD_FROM_DICT_OR_GLOBALS': 150,
    'LOAD_GLOBAL': 151,
    'LOAD_NAME': 154,
    'LOAD_SUPER_ATTR': 155,
    'MAKE_CELL': 158,
    'MAP_ADD': 159,
    'MATCH_CLASS': 160,
    'POP_JUMP_IF_FALSE': 161,
    'POP_JUMP_IF_NONE': 162,
    'POP_JUMP_IF_NOT_NONE': 163,
    'POP_JUMP_IF_TRUE': 164,
    'RAISE_VARARGS': 165,
    'RESUME': 166,
    'RERAISE': 167,
    'RETURN_CONST': 168,
    'SEND': 169,
    'SET_ADD': 171,
    'SET_FUNCTION_ATTRIBUTE': 172,
    'SET_UPDATE': 173,
    'STORE_ATTR': 174,
    'STORE_DEREF': 176,
    'STORE_FAST': 177,
    'STORE_FAST_LOAD_FAST': 178,
    'STORE_FAST_STORE_FAST': 179,
    'STORE_GLOBAL': 180,
    'STORE_NAME': 181,
    'SWAP': 182,
    'UNPACK_EX': 183,
    'UNPACK_SEQUENCE': 184,
    'YIELD_VALUE': 188,
    'INSTRUMENTED_RESUME': 237,
    'INSTRUMENTED_END_FOR': 238,
    'INSTRUMENTED_END_SEND': 239,
    'INSTRUMENTED_RETURN_VALUE': 240,
    'INSTRUMENTED_RETURN_CONST': 241,
    'INSTRUMENTED_YIELD_VALUE': 242,
    'INSTRUMENTED_LOAD_SUPER_ATTR': 243,
    'INSTRUMENTED_FOR_ITER': 244,
    'INSTRUMENTED_CALL': 245,
    'INSTRUMENTED_CALL_FUNCTION_EX': 246,
    'INSTRUMENTED_INSTRUCTION': 247,
    'INSTRUMENTED_JUMP_FORWARD': 248,
    'INSTRUMENTED_JUMP_BACKWARD': 249,
    'INSTRUMENTED_POP_JUMP_IF_TRUE': 250,
    'INSTRUMENTED_POP_JUMP_IF_FALSE': 251,
    'INSTRUMENTED_POP_JUMP_IF_NONE': 252,
    'INSTRUMENTED_POP_JUMP_IF_NOT_NONE': 253,
    'INSTRUMENTED_LINE': 254,
    'JUMP': 256,
    'JUMP_NO_INTERRUPT': 257,
    'LOAD_CLOSURE': 258,
    'LOAD_METHOD': 259,
    'LOAD_SUPER_METHOD': 260,
    'LOAD_ZERO_SUPER_ATTR': 261,
    'LOAD_ZERO_SUPER_METHOD': 262,
    'POP_BLOCK': 263,
    'SETUP_CLEANUP': 264,
    'SETUP_FINALLY': 265,
    'SETUP_WITH': 266,
    'STORE_FAST_MAYBE_NULL': 267,
}
MIN_INSTRUMENTED_OPCODE = 237
HAVE_ARGUMENT = 68
