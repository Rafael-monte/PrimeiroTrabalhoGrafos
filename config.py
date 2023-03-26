# Local do arquivo de entrada. Colocar r'input\grafo.txt' caso seja windows
INPUT_FILE_LOCATION: str = r'input/grafo.txt'
# Permite vertices que se relacionam consigo mesmos?
ALLOW_REFLEXIVE_RELATIONSHIP: bool = False
# Valor "infinito" para as distancias dos vértices
INFINITE: int = 2**63