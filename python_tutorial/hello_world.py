def fib(n):
    """Print a Fibbonacci series up to n."""
    a,b = 0,1
    while a<n:
        print(a,end=',')
        a,b = b, a+b
    # print()

# fib(2000)

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# ask_ok("are you sure?")

def arg_test(name,*questions,**starring):
    print('Hello' + name)
    for q in questions:
        print(q)
    print('-'*40)
    for role in sorted(starring.keys()):
        print(role + ':' + starring[role])

# arg_test('Adrian', 'How are you?', 'Ryly?', waiter = 'Michal', client = 'Adrian')


def make_incrementator(n):
    return lambda x: x+n
# f = make_incrementator(42)
# f(0)
# f(1)

# 5 data structures
