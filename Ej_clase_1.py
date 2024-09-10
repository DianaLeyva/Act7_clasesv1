print("introduccion a clases")
class animal:
    edad=3
    raza="poodle"
    def come():
        return "croquetas"
perro = animal()
print("creando el objeto de la clase animal")
print(f"edad de perro: {perro.edad}")
print(f"raza de perro: {perro.raza}")
comida=animal.come()
print(f"perro come: {comida}")
