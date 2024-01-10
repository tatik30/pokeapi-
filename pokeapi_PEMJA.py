import requests

def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    url = f"{base_url}{pokemon_name.lower()}/"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        
        pokemon_data = response.json()
        return pokemon_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    pokemon_name = input("Masukkan nama Pokemon: ")
    
    pokemon_data = get_pokemon_data(pokemon_name)
    
    if pokemon_data:
        print("\nData Pokemon:")
        print(f"Nama: {pokemon_data['name']}")
        print(f"ID: {pokemon_data['id']}")
        print("Tipe:")
        for type_info in pokemon_data["types"]:
            print(f" - {type_info['type']['name']}")
            print(f"Berat: {pokemon_data['weight']}")
            print(f"Tinggi: {pokemon_data['height']}")

        print("Ability:")
        for ability_info in pokemon_data['abilities']:
            print(f" - {ability_info['ability']['name'].capitalize()}")   
    else:
        print("Gagal mendapatkan data Pokemon.")
if __name__ == "__main__":
    main()