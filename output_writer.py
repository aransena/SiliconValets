from classes import Command


def write_output(commands, output_file_name):
    if len(commands) == 0:
        raise ValueError('The number of commands is 0.')

    for i, command in enumerate(commands):
        if not isinstance(command, Command):
            raise TypeError('Command #%i is not of type Command.' % i)

    with open(output_file_name, 'w') as f:
        f.write('%d\n' % len(commands))
        for command in commands:
            f.write('%d %s %d %d %d\n' % (command.drone_id, command.command_type, command.warehouse_or_customer_id,
                                          command.product_id, command.num_products))


if __name__ == '__main__':

    commands = []
    commands.append(Command(0, 'load', 0, 0, 1))
    commands.append(Command(0, 'load', 0, 1, 1))
    commands.append(Command(0, 'deliver', 0, 0, 1))
    commands.append(Command(0, 'load', 1, 2, 1))
    commands.append(Command(0, 'deliver', 0, 2, 1))
    commands.append(Command(1, 'load', 1, 2, 1))
    commands.append(Command(1, 'deliver', 2, 2, 1))
    commands.append(Command(1, 'load', 0, 0, 1))
    commands.append(Command(1, 'deliver', 1, 0, 1))
    write_output(commands, 'test_output.txt')
