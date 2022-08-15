from classes.pokemon import Pokemon
from pathlib import Path
import csv


def test_instantiate_from_csv():
    """
    Test instantiate_from_csv Method from the pokemon Class

    ...

    Raises
    ------
    Instance error
        pokemon.name is not the correct type
    Move set error
        If move set does not have 4 moves
    Length error
        If the amount of pokémon are not the expected amount of pokémon
    Name error
        If pokémon names are not the expected names
    """
    Pokemon.instantiate_from_csv()
    base_path = Path(__file__).parent
    with open(base_path / '../data/FirstGenPokemon.csv', 'r') as f:
        reader = csv.DictReader(f)
        pokemons_in_csv = list(reader)

    expected_pokemon_name_list = []
    for pokemon in pokemons_in_csv:
        expected_pokemon_name_list.append(pokemon.get('Name'))

    actual_pokemon_name_list = []
    for pokemon in list(Pokemon.all.values()):
        assert isinstance(pokemon.name, object)
        actual_pokemon_name_list.append(pokemon.name)
        # check if pokémon has 4 moves moves
        assert any(x is not None for x in [pokemon.moves.move1, pokemon.moves.move2,
                                           pokemon.moves.move3, pokemon.moves.move4])

    assert len(actual_pokemon_name_list) == len(expected_pokemon_name_list)
    assert all([a == b for a, b in zip(actual_pokemon_name_list, expected_pokemon_name_list)])
