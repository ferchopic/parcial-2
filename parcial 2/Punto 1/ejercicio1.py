from cola import Cola


class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None):
        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value['number'] < root.value['number']:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

        __inorden_start_with(self.root, cadena)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)
    
    def bifurcar(self, heroes, villanos):
        def __preorden(root, heroes, villanos):
            if root is not None:
                if root.other_values is True:
                    heroes.insert_node(root.value, root.other_values)
                else:
                    villanos.insert_node(root.value, root.other_values)
                __preorden(root.left, heroes, villanos)
                __preorden(root.right, heroes, villanos)

        __preorden(self.root, heroes, villanos)

    def search_by_coincidence(self, cadena):
        def __buscar_por_coincidencia(root, cadena):
            if root is not None:
                if root.value['name'].startswith(cadena):
                    print(f"Nombre: {root.value['name']}")
                    print(f"Número: {root.value['number']}")
                    print(f"Tipos: {', '.join(root.value['types'])}")
                __buscar_por_coincidencia(root.left, cadena)
                __buscar_por_coincidencia(root.right, cadena)

        __buscar_por_coincidencia(self.root, cadena)

    def search_pokemon_by_name(self, name):
        def __search_by_name(root, name):
            if root is not None:
                if root.value['name'] == name:
                    print(f"Nombre: {root.value['name']}")
                    print(f"Número: {root.value['number']}")
                    print(f"Tipos: {', '.join(root.value['types'])}")
                __search_by_name(root.left, name)
                __search_by_name(root.right, name)

        __search_by_name(self.root, name)

    

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            root = self.balancing(root)
            self.update_height(root)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if value in root.other_values['types']:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    def altura_der(self):
        def __altura_der(root):
            if root is None:
                return 0
            else:
                return 1 + __altura_der(root.right)
        return __altura_der(self.root)
    
    def altura_izq(self):
        def __altura_izq(root):
            if root is None:
                return 0
            else:
                return 1 + __altura_izq(root.left)
        return __altura_izq(self.root)
    
    def contar_impar(self):
        def __contar_impar(root):
            if root is None:
                return 0
            elif root.value % 2!=0:
                return 1+ __contar_impar(root.right) + __contar_impar(root.left)
            else:
                return __contar_impar(root.right) + __contar_impar(root.left)
        return __contar_impar(self.root)
    
    def contar_par(self):
        def __contar_par(root):
            if root is None:
                return 0
            elif root.value % 2==0:
                return 1+ __contar_par(root.right) + __contar_par(root.left)
            else:
                return __contar_par(root.right) + __contar_par(root.left)
        return __contar_par(self.root)
    
    def par_impar(self):
        def __par_impar(root):
            count = 0
            count2 = 0 
            if root is not None:
                if root.value % 2 == 0:
                    count = 1
                else:
                    count2 = 1
                count += __par_impar(root.left)
                count2 += __par_impar(root.right)
            return count, count2

        return __par_impar(self.root)

    def hijoMinimo(self):
        if self.root is not None:
            nodo = self.root
            while nodo.left:
                nodo = nodo.left
            return nodo.value
        else:
            raise Exception('No se encontraron valores')

    def hijoMayor(self):
        if self.root is not None:
            nodo = self.root
            while nodo.right:
                nodo = nodo.right
            return nodo.value
        else:
            raise Exception('No se encontraron valores')

pokemon_data = [
    {"name": "Pikachu", "number": 25, "types": ["Electricp"]},
    {"name": "Bulbasaur", "number": 1, "types": ["Pasto", "Veneno"]},
    {"name": "Charizard", "number": 6, "types": ["Fuego", "Volador"]},
    {"name": "Jolteon", "number": 135, "types": ["Electrico"]},
    {"name": "Lycanroc", "number": 745, "types": ["Roca"]},
    {"name": "Tyrantrum", "number": 697, "types": ["Roca", "Dragon"]},
    {"name": "Steelix", "number": 208, "types": ["Acero"]}
]

pokemon_tree = BinaryTree()

print("a")
for pokemon in pokemon_data:
    name = pokemon["name"]
    number = pokemon["number"]
    types = pokemon["types"]
    pokemon_tree.insert_node(name, (number, types))

print("b")
cadena = input("Ingrese una cadena para buscar Pokémon por proximidad en el nombre: ")
print("Resultados de búsqueda:")
pokemon_tree.inorden_start_with(cadena)

print("c")
def listar_nombres_por_tipo(self, root, tipos):
    if root is not None:
        if root.value["types"][0] in tipos:
            print(root.value["name"])
        self.listar_nombres_por_tipo(root.left, tipos)
        self.listar_nombres_por_tipo(root.right, tipos)

tipos_a_buscar = ["Agua","Fuego", "Planta","Electrico"]
print("Nombres de Pokémon de tipo Agua:")
pokemon_tree.listar_nombres_por_tipo(pokemon_tree.root, tipos_a_buscar)

print("d")
print("Listado en orden ascendente por número de Pokémon:")
pokemon_tree.inorden()

print("\nListado por nivel por nombre de Pokémon:")
pokemon_tree.by_level()

print("e")
pokemon_name_to_search = input("Ingrese la parte del nombre del Pokémon que desea buscar: ")
print("Resultados de búsqueda por coincidencia en el nombre:")
pokemon_tree.search_pokemon_by_coincidence(pokemon_name_to_search)

print("f")
tipo_electrico = "Electrico"
tipo_acero = "Acero"

print(f"Cantidad de Pokémon de tipo eléctrico: {pokemon_tree.contar(tipo_electrico)}")
print(f"Cantidad de Pokémon de tipo acero: {pokemon_tree.contar(tipo_acero)}")