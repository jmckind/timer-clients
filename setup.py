from distutils.core import setup

setup(
    name='timer_clients',
    version='0.2.3',
    description='Python package that provides timer utility commands.',
    license='MIT',
    author='John McKenzie',
    author_email='jmckind@gmail.com',
    url='https://github.com/jmckind/timer-clients',
    packages=['timer_clients'],
    scripts=['scripts/countdown'],
)
