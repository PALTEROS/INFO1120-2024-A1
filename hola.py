import random

def generar_chiste():
    chistes = [
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
        "¿Cómo se dice pañuelo en japonés? Saka-moko.",
        "¿Por qué los pingüinos siempre llevan corbata? Porque les queda muy bien con su esmoquin.",
        "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
        "¿Por qué los esqueletos no pelean entre ellos? Porque no tienen agallas.",
        "¿Cómo se dice pañuelo en japonés? Saka-moko.",
        "¿Por qué los pingüinos siempre llevan corbata? Porque les queda muy bien con su esmoquin."
    ]

    return random.choice(chistes)

if __name__ == "__main__":
    print(generar_chiste())
