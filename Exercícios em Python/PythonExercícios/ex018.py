from math import sin, cos, tan, radians

ang = float(input('Digite um número: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'O ângulo original é \033[30;41m{ang}\033[m\nSeu seno é \033[4;45m{sen:.2f}\033[m\nSeu cosseno é \033[1;36m{cos:.2f}\033[m\nSua tangente é \033[7;37m{tan:.2f}\033[m')
