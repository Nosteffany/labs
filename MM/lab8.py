
def prop(delta,gamma):
    exp = 60/delta
    prob = 26/60

    p0 = (1-prob)/(1-prob**11)
    gamma_p = (((1-prob)*(prob**10))/(1-prob**11))
    gamma_eff  = (1-gamma_p) * gamma
    Ls = (prob*(1-(11*prob**10)+10*prob**11)) / ((1-prob)*(1-prob**11))
    Ws = Ls / gamma_eff
    Wq = Ws - 1 / exp
    Lq = Wq * gamma_eff

    print(f"Ймовірність, що біля їдальні не буде жодного авто: {p0}")
    print(f"Середнє число кллієнтів, що чекають на обслуговування: {Lq}")
    print(f"Cередній час очікування від прибуття до початку обслуговування {Wq}")
    print(f"Частота того, що клієнт матиме місце: {1-gamma*gamma_p}")
    print(f"")

prop(1,26)

print("Завдання2\n")
def prop2(gamma):
    exp = 14
    prob = 24/exp

    p0 = (1-prob)/(1-prob**19)
    gamma_p = (((1-prob)*(prob**18))/(1-prob**19))
    gamma_eff  = (1-gamma_p) * gamma
    Ls = (prob*(1-(19*prob**18)+18*prob**19)) / ((1-prob)*(1-prob**19))
    Ws = Ls / gamma_eff
    print(f"Ефективна частота надходження хворих: {gamma_eff}")
    print(f"Частота того, що клієнт не матиме місця: {gamma_p*gamma}")
    print(f"середній час перебування в клініці: {Ws}")
prop2(24)
