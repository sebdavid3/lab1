from datetime import date
from validate_email import validate_email
from PIL import ImageTk, Image
import copy
from multipledispatch import dispatch 

class Cliente: 
    
    soyHoja = True 
    
    keys = ["id","nombre","apellido","edad","fechaDeNacimiento","genero","estadoCivil","telefono","celular","email",
            "nivelEducativo","rangoDeIngresos","direcciones","noContactoPorEmail","noContactoPorTelefono","noContactoPorSMS","noContactoPorCorreoFisico"]

    
    def __init__(self, datos:list,ruta) -> None:
        self.informacion = dict(zip(self.keys,datos))
        self.ruta = ruta
        
    def __str__(self) -> str:
        a = self.informacion.get("nombre")
        b = self.informacion.get("apellido")
        c = self.informacion.get("id")
        return f"Nombre: {b}, {a} ID: {c}"    
        
    def actualizar(self,**kwargs):
        for x in kwargs:
            self.informacion.update(x)

class Producto:
    
    soyHoja = True
    
    keys = ["id","nombre","shortDescription","longDescription","image"]
    
    def __init__(self, datos:list, ruta) -> None:
        self.informacion = dict(zip(self.keys,datos))
        self.ruta = ruta
        
    def __str__(self) -> str:
        a = self.informacion.get("nombre")
        b = self.informacion.get("id")
        c = self.informacion.get("shortDescription")
        return f"Nombre: {a}, id: {b}, descripción: {c}"
        
    def actualizar(self,**kwargs):
        for x in kwargs:
            self.informacion.update(x)
            
# La clase categorías es implementada tanto en la jerarquia de clientes
# como en la de productos 
    
class Categoria:
    
    soyHoja = False
    
    def __init__(self,id:int,name:str,hijos:list=[],ruta:list=[]) -> None:
        self.id = id
        self.name = name
        self.hijos = hijos
        self.ruta = ruta
 
# agregar categorías, clientes y productos:
# faltan validar que agrege clientes en el arbol de clientes y productos en el arbol de productos, pero digo yo que de eso
# nos aseguramos en la GUI ["ropa", "hombre"]
       
# def agregar(root:Categoria,objeto):
#     aux=copy.copy(objeto)
#     if not aux.ruta:
#         for x in aux.ruta:
#             for hijo in root.hijos:
#                 if(x==hijo.name):
#                     aux.ruta.pop(0)
#                     agregar(hijo,aux)
#         return False
#     else:  
#         hijo.hijos.append(objeto)
#         return True     
    
def agregar(id:int,objeto:Categoria):
    x=buscarPorId(root,id)  
    x.hijos.append(objeto)  
              
def buscarPorId(root:Categoria,id:int):
    if(root.id==id):
        return root
    else:
        for x in root.hijos:
            if(x.id==id):
                return x
            else:
                return buscarPorId(x,id)
    
    return None

def buscarPorName(root:Categoria,Name:str):
    if(root.name==Name):
        return root    
    for x in root.hijos:
        if(x.name.strip() == Name.strip()):
            return x
        else:
            return buscarPorName(x,Name)
    
    return None
@dispatch(int)
def editar(id:int, **kwargs):        
    target = buscarPorId(id)
    if (None==target):
        return "El objeto que desea editar no existe"
    else:
        target.actualizar(kwargs)
@dispatch(str)       
def editar(name:str, **kwargs):        
    target = buscarPorName(name)
    if (None==target):
        return "El objeto que desea editar no existe"
    else:
        target.actualizar(kwargs)

#da un array tal que [cantidad de clientes/productos, lista de dichos clientes/productos]
def cantidadHojas(nodo:Categoria, cantHojas = 0, hojas:list=[]):
    aux=copy.copy(nodo)
    for x in aux.hijos:
        if(x.soyHoja):
            cantHojas += 1
            hojas.append(x)
        else:
            cantidadHojas(x,cantHojas,hojas)
    
    return [cantHojas, hojas]            
        
#prueba    
root = Categoria(id=10000, name="root")
hijo1 = Categoria(id=100001, name="hijo1",ruta=["root"])
agregar(10000,hijo1)
print(root.hijos[0].name)
producto1=Producto([100001,"hijonuevo","producto nuevo", "producto realmente nuevo","imagen"])


    
