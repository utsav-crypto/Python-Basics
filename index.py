class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


for num in [12, 34, 12]:
    print(num)

emp_1 = Employee('Utsav', 'Singh')

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
