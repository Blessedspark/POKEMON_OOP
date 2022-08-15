from classes.pokemon import Pokemon, print_heading
import cmd


def parse(arg):
    """Convert a series of zero or more arguments to an argument tuple"""
    return tuple(map(str, arg.split()))


class PokemonShell(cmd.Cmd):
    """
        Pokemon game command line shell created with the cmd class
        docs: https://docs.python.org/3/library/cmd.html
    """

    intro = 'Welcome to the OOP pokemon game.   Type help or ? to list commands.\n'
    prompt = '(Pokemon) '
    main_pokemon = None

    # ----- basic pokemon game commands -----
    def do_select(self, pokemon_nr):
        """Select main pokemon:  select (pokemon_nr)"""
        amount_of_pokemon = len(Pokemon.all)
        if amount_of_pokemon != 0:
            if pokemon_nr.isnumeric():
                pokemon_nr = int(pokemon_nr) - 1
                if 0 <= pokemon_nr < amount_of_pokemon:
                    selected_pokemon_name = list(Pokemon.all.keys())[pokemon_nr]
                    pokemon = Pokemon.all[selected_pokemon_name]
                    if pokemon.hp != 0:
                        print_heading('NEW MAIN POKEMON SELECTED')
                        self.main_pokemon = pokemon
                        self.main_pokemon.print_pokemon_specs()
                    else:
                        print("pokemon is dead, revive the pokemon first with 'revive'")
                else:
                    print("pokemon with this number does not exist, print all available pokemon with 'pokemon'")
            else:
                print("input a integer value")
        else:
            print("no pokemon exist yet, Create custom pokemon with 'custom' or get all first gen pokemon with "
                  "'firstgen'.")

    def do_custom(self, arg):
        """Create custom pokemon: custom"""
        Pokemon.create_via_terminal()

    def do_firstgen(self, arg):
        """Add all first gen pokemon to the available pokemon: firstgen"""
        print_heading('FIRST GEN POKEMON ARE ADDED TO THE GAME')
        Pokemon.instantiate_from_csv()

    def do_revive(self, pokemon_nr):
        """Revive pokemon: revive (pokemon_nr)"""
        amount_of_pokemon = len(Pokemon.all)
        if pokemon_nr.isnumeric():
            pokemon_nr = int(pokemon_nr) - 1
            if 0 <= pokemon_nr < amount_of_pokemon:
                selected_pokemon_name = list(Pokemon.all.keys())[pokemon_nr]
                pokemon = Pokemon.all[selected_pokemon_name]
                if pokemon.hp == 0:
                    Pokemon.revive(pokemon)
                    print_heading('POKEMON REVIVED')
                    print(f"{pokemon.name} is revived with {pokemon.hp} hp")
                else:
                    print(f"{selected_pokemon_name} is not knocked out, the hp of the pokemon needs to be 0 first")
            else:
                print("pokemon with this number does not exist, print all available pokemon with 'pokemon'")
        else:
            print("input a integer value")

    def do_pokemon(self, arg):
        """Print all available pokemon: pokemon"""
        Pokemon.print_all_pokemon()

    def do_fight(self, args):
        """Let main pokemon fight another pokemon: fight (opponent_pokemon_nr) (random_fight 1 = True, 0 = False)"""
        amount_of_pokemon = len(Pokemon.all)

        try:
            opponent_pokemon_nr, random_fight = [x for x in args.split()]
        except ValueError as e:
            print(e)
            print("the correct syntax is: fight (opponent_pokemon_nr) (random_fight True =1, False = 0)")
            return

        if isinstance(self.main_pokemon, Pokemon):
            if self.main_pokemon.hp != 0:
                if opponent_pokemon_nr.isnumeric() and random_fight.isnumeric():

                    random_fight = int(random_fight)
                    opponent_pokemon_nr = int(opponent_pokemon_nr) - 1  # pokemon numbers are from 1 and index from 0
                    if 0 <= opponent_pokemon_nr < amount_of_pokemon:

                        opponent_pokemon_name = list(Pokemon.all.keys())[opponent_pokemon_nr]
                        opponent_pokemon = Pokemon.all[opponent_pokemon_name]
                        if self.main_pokemon != opponent_pokemon:
                            if opponent_pokemon.hp != 0:

                                print_heading('FIGHT BEGINS:')
                                self.main_pokemon.fight(opponent_pokemon, random_fight=random_fight)
                            else:
                                print("opponent pokemon is dead, revive the pokemon first with 'revive'")
                        else:
                            print("you can't fight yourself, choose an other pokemon as opponent")
                    else:
                        print("pokemon with this number does not exist, print all available pokemon with 'pokemon'")
                else:
                    print("input integer values")
            else:
                print("the hp of your main pokemon is 0 revive the pokemon first with 'revive (pokemon_nr)' or choose "
                      "an other with 'select (pokemon_nr)'")
        else:
            print("no main pokemon selected, select a main pokemon with 'select (pokemon_nr)' to see all available "
                  "pokemon type 'pokemon' ")

    def do_close(self, arg):
        """Exit game window"""
        return True


def main():
    PokemonShell().cmdloop()


if __name__ == '__main__':
    main()
