def sum_command(command):
    data=command.split()
    command_args=data[1:]
    result=0
    for num in command_args:
        result += int(num)
    responce="合計は「{}」です。".format(result)
    return responce