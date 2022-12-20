
import sqlite3
class classCRUDEPeli:
  def __init__(self):
    pass
  def CreaPeli(self,BD,titulo,duracion,director,clasificacion):
    self.exito=False
    conn = sqlite3.connect(BD)
    cur = conn.cursor()
    query =f"insert into pelicula (titulo, duracion,clasificacion, director) values ('{titulo}','{duracion}','{clasificacion}', '{director}')"
    cur.execute(query)
    conn.commit()
    conn.close
    self.exito=True
    return self.exito
  
  def modificarPelicula(self,BD,titulo,duracion,director,clasificacion,id_peli):
    self.exito=False
    conn = sqlite3.connect(BD)
    cur = conn.cursor()
    query =f"update pelicula set titulo='{titulo}', duracion='{duracion}',clasificacion='{clasificacion}', director='{director}' where id_pelicula='{id_peli}'"
    cur.execute(query)
    conn.commit()
    conn.close
    self.exito=True
    return self.exito

  def eliminarPelicula (BD,id_pelicula): 
    pass
    

  def nuevaPelicula (BD,id_pelicula):
    pass