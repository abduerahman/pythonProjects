from dis import dis

def max(x,y):
    if x > y:
        return x
    return y

s = ['United','States', 'of','America']
out = [i for i in s if i.__contains__('Sta')]
print()