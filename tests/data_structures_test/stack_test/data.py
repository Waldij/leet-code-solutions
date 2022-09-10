class StackBaseTestData:
    BASE = [1, 'some string', True, 4.123, [1, 2, 3]]
    BASE_LENGTH = 5


class StackMethodsTestData(StackBaseTestData):
    class AsList:
        AS_LIST = StackBaseTestData.BASE

    class Pop:
        AFTER_POP = StackBaseTestData.BASE[1:]

    class Append:
        TO_APPEND = 'SOME_APPENDED_STRING'
        AFTER_APPEND = [1, 'some string', True, 4.123, [1, 2, 3]] + [TO_APPEND]

    class Peek:
        PEEKED = 1
        AFTER_PEEK = StackBaseTestData.BASE

    class Length:
        TO_APPEND = 'SOME_APPENDED_STRING'
        LENGTH_AFTER_APPEND = StackBaseTestData.BASE_LENGTH + 1

    class String:
        AS_STRING = f'Stack({StackBaseTestData.BASE})'
