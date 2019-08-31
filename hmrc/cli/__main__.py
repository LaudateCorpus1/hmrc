"""Command line entry point"""

from .base import Command

__all__ = [
    'main',
]


def main(args=None):
    """Command line entry point"""
    command = Command(args)
    output = command()
    if output is not None:
        print('\n'.join(output) if isinstance(output, list) else output)


if __name__ == '__main__':
    main()
