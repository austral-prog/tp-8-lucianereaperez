def get_coordinate(record):
    treasure = record[0]
    coordenada = record[1]
    return coordenada
def convert_coordinate(coordinate):
    new_coordinate=(coordinate[0], coordinate[1])
    return new_coordinate
def create_record(azara_record, rui_record):
    tesoro= azara_record[0]
    coordenada= azara_record[1]
    new_coordinate=(coordenada[0], coordenada[1])
    ubicacion= rui_record[0]
    coordenadaR= rui_record[1]
    cuadrante= rui_record[2]
    if new_coordinate == coordenadaR :
        ubi_final = (tesoro, coordenada, ubicacion, coordenadaR, cuadrante)
        return ubi_final
    else:
        return "not a match"
