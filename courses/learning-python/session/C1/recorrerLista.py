peliculas = ["película1", "película2", "película3"]
print(peliculas)
print(peliculas[0])
print(len(peliculas))
# Con append agregamos datos al final de una lista
peliculas.append("película4")
print(peliculas)
# Con pop removemos el último dato de una lista
peliculas.pop()
print(peliculas)
# Con extend agregamos un grupo de datos al final de la lista
peliculas.extend(["película4", "película5"])
print(peliculas)
# Con remove removemos un dato específico de la lista
peliculas.remove("película4")
print(peliculas)
# Con insert insertamos un dato en un lugar especifico de la lista
peliculas.insert(0, "película0")
print(peliculas)
+eval(input())
