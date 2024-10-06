import helper

helper.start_task(1)

print('Hello Python!'[2])

helper.end_task(1)

helper.start_task(2)

print('Hello Python!'[2])

helper.end_task(2)

helper.start_task(3)

print('Hello Python!'[0:2])
print('Hello Python!'[:2])

helper.end_task(3)

helper.start_task(4)

print('Hello Python!'[6:7] + 'at' + 'h')

helper.end_task(4)
